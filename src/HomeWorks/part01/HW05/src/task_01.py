import random
matrix = []
n = 5
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 9))
    matrix.append(row)
    print(matrix[i])
print('and now i am making a new matrix: ')
new_matrix = []
max_row_matrix = max(matrix)
max_element = max(max_row_matrix)
#print(max_element)
for i in range(n):
    row.append(matrix[i][j] / max_element)
    for j in range(n):
        row.append(matrix[i][j] / max_element)
    new_matrix.append(row)
    print(new_matrix[i])