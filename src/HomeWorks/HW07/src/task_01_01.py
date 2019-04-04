#create
#print
#summ_elem
#max_elem
#min_elem



from random import randint

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(1, 9))
        matrix.append(row)
    return matrix



a = create_matrix(5)
print(a)
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ') ###
        print()



def sum_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in matrix:
            summ += elem
    return summ



def max_elem(matrix):
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem

def min_elem(matrix):
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem



matrix_a = create_matrix(5)
print_matrix(matrix_a)
print(max_elem(matrix_a))
print(min_elem(matrix_a))

