#HalfTranspose

def HalfTranspose(m):
    mm = len(m)-1
    for i in range(len(m)):
        ii=0
        while ii<i:
            print(m[i][ii],end='')
            ii+=1
            print(",",end='')
        print(m[i][i],end='')
        if i!=0: print(",",end='')
        ii=0
        while ii<i:
            print(m[i-1-ii][i],end='')
            ii+=1 
            if (i-ii)>0:    
                print(",",end='')
       
        print("")
    
#HalfTranspose([[1,2,3],[4,5,6],[7,8,9]])
# Initialize matrix
govnina = list(eval(input()))
#print(govnina)
R = len(govnina)
#print(R)
matrix = []
matrix.append(govnina)
i=1
while i<R:
    govnina = list(eval(input()))
    matrix.append(govnina)
    i+=1
#print(matrix)
HalfTranspose(matrix)

    



