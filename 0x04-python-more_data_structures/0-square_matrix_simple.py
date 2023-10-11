#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.
    Args:
    matrix: A 2-dimensional array of integers.
    Returns:
    A new 2-dimensional array of the same size as `matrix`, where each value is
    the square of the corresponding value in `matrix`.
    """
    # Create a new matrix to store the squared values.
    squared_matrix = []
    for row in matrix:
        squared_row = []
    for value in row:
        squared_row.append(value ** 2)
    squared_matrix.append(squared_row)
    return squared_matrix
