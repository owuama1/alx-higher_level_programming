#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = []

    # Iterate through each row of the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through each elem in row, get square, append to result row
        for element in row:
            result_row.append(element ** 2)

        # Append the result row to the result matrix
        result_matrix.append(result_row)

    return result_matrix
