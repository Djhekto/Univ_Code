#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define N 4 // Размер матрицы
#define M 4

void criticalSection(int world_rank) {
    if (world_rank == 0) {  // =========================== координатор
        FILE *file;
        const char *filename = "critical.txt";

        file = fopen(filename, "r");
        if (file) {
            // Файл существует
            fclose(file);
            printf("Ошибка: файл %s уже существует.\n", filename);
            exit(EXIT_FAILURE);
        } else {
            // Файл не существует
            file = fopen(filename, "w");
            if (!file) {
                printf("Ошибка при создании файла %s\n", filename);
                exit(EXIT_FAILURE);
            }
            fclose(file);

            srand(time(NULL));
            int sleepTime = rand() % 4;
            printf("Спим на %d секунд\n", sleepTime);
            sleep(sleepTime);

            if (remove(filename) != 0) {
                printf("Ошибка при удалении файла %s\n", filename);
                exit(EXIT_FAILURE);
            }
        }
    } else { // ======================================================= не координатор
        // сигнал процесс координатору
        MPI_Send(NULL, 0, MPI_INT, 0, 0, MPI_COMM_WORLD);
        // ждем обратный сигнал
        MPI_Recv(NULL, 0, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        int row = world_rank / N;
        int column = world_rank % M;
        printf("[%d,%d] Критическая секция  %d успешно выполнена.\n",row,column, world_rank);
    }
}

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    if (world_size != 16) {
            printf("Запущено %d процессов. Ожидалось 16 процессов\n", world_size);
            printf("Попробуйте mpirun -np 16 --oversubscribe ./a.out");
            MPI_Finalize();
            return EXIT_FAILURE;
            }

    if (world_rank == 0) { // =========================== координатор
        for (int i = 1; i < world_size; i++) {
            MPI_Recv(NULL, 0, MPI_INT, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE); //ждем сигнал от других процессов
            MPI_Send(NULL, 0, MPI_INT, i, 0, MPI_COMM_WORLD); // координатор отправляет сигнал другому процессу
        }
    } else { // ======================================================= не координатор
        criticalSection(world_rank);
    }

    MPI_Finalize();
}
