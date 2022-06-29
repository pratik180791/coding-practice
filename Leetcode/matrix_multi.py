
rows = 3
cols = 3
matrix_A = [1,2,3,4,5,6,7,8,9]
matrix_B = [0,2,4,1,4.5,2.2,1.1,4.3,5.2]
processed_matrix_a = [[0]*rows ] * cols
processed_matrix_b = [[0]*rows ] * cols
result_matrix = [[0]*rows ] * cols

processed_matrix_a[0] = matrix_A[0:3]
processed_matrix_a[1] = matrix_A[3:6]
processed_matrix_a[2] = matrix_A[6:9]

processed_matrix_b[0] = matrix_B[0:3]
processed_matrix_b[1] = matrix_B[3:6]
processed_matrix_b[2] = matrix_B[6:9]

print(processed_matrix_a)
print(processed_matrix_b)
print(result_matrix)
result_matrix = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(processed_matrix_a)):
    for j in range(len(processed_matrix_b[0])):
        for k in range(len(processed_matrix_b)):
            result_matrix[i][j] += processed_matrix_a[i][k] * processed_matrix_b[k][j]
print(result_matrix)
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[0,2,4],
    [1,4.5,2.2],
    [1.1,4.3,5.2]]
# result is 3x4
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
print(X)
print(Y)
# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)