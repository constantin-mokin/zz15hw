

def summ_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in matrix:
            summ += elem
    return summ


def get_max_elem(matrix):
    max_element = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_element:
                max_element = elem
    return max_element


def get_min_elem(matrix):
    min_element = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_element:
                min_element = elem
    return min_element
