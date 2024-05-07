#include <mpi.h>
#include <math.h>
#include <stdio.h>
#include <time.h>

#define A 0.0
#define B 31.41592653589793 // pi*10

double f(double x) { return 1.57 * (fabs(sin(x))); } // pi/2 * |sin| -> f(k*pi) = k*pi

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int segnum = 200000000;
    int local_segnum = segnum / world_size;
    double otvet = 0.0;
    double x_l, x_r, x_mid; // точка (слева, справа, центр) на интервале
    double h = (B - A) / (double) segnum; // шаг

    clock_t start = clock(); // Start timing

    for (int i = world_rank * local_segnum; i < (world_rank + 1) * local_segnum; i++) {
        x_l = A + h * (double) i;
        x_mid = A + h * (double) (i + 0.5);
        x_r = A + h * (double) (i + 1);
        otvet += h / 6.0 * (f(x_l) + 4.0 * f(x_mid) + f(x_r));
    }

    double total_otvet = 0.0;
    MPI_Reduce(&otvet, &total_otvet, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (world_rank == 0) {
        clock_t end = clock(); // End timing
        double time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Time used: %.6f seconds\n", time_used);
        printf("Number of processes: %d\n", world_size);
        printf("%.20f ~~ pi*10\n", total_otvet);
    }

    MPI_Finalize();
    return 0;
}