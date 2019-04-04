from random import randint

n = 0
matrix = []

while n < 19:
    matrix.append(randint(0,9))
    n += 1

max_a = max(matrix)
print(max_a)
for i in range(0, len(matrix), 2):
    matrix[i] = max_a
print(matrix)
