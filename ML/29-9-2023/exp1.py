import numpy as np


def input_matrix(matrix_name):
    rows = int(input(f"Enter the number of rows for {matrix_name}: "))
    cols = int(input(f"Enter the number of columns for {matrix_name}: "))
    matrix = []
    print(f"Enter the elements for {matrix_name}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter the element in row {i + 1}, column {j + 1}: "))
            row.append(element)
        matrix.append(row)

    return np.array(matrix)


matrix1 = input_matrix("matrix1")
matrix2 = input_matrix("matrix2")

sum_result = np.add(matrix1, matrix2)
print("Sum of matrices:")
print(sum_result)