#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Squares all elements of a matrix.
    Args:
    matrix: A 2-dimensional array.
    Returns:
    A new matrix of the same size as the input matrix,
    with each element squared.
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    return new_matrix
