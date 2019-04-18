from random import randint
matrix = []
n = int(input('--->  '))
summ = 0

for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(1, 9))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if matrix[i][j] % 3 == 0:
            summ += matrix[i][j]
print(summ)




