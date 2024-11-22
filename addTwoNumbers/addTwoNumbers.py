import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
rows, cols = matrix.shape


matrix = matrix.T

for i  in range(rows):
    for j in range(cols//2):
        tmp=matrix[i][j]
        matrix[i][j]=matrix[i][cols-j-1]
        matrix[i][cols-1-j]=tmp
        
print(matrix)