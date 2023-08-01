matrix1=[[1,2,3,4,5],
        [5,6,7,8]]
matrix2=[[1,2,3,4],
        [5,6,7,8,9]]




for j in range(2):
    for i in range(4):
        if matrix1[j][i]>matrix2[j][i]:
            matrix1.append(int(0))
        elif matrix1[j][i]<matrix2[j][i]:
            matrix2.append(int(0))
        print(matrix1[j][i]+matrix2[j][i])
