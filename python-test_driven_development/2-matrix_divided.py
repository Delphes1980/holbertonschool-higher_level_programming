#!/usr/bin/python3
"""
    Module description: module that contains a function called matrix_divided
that divide a matrix by a given number

    Functions: matrix_divided(matrix, div):
    divide a matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    Description: Divide all elements of a matrix
    matrix must be a list of lists of integers or floats
    each row of the matrix must be of the same size
    div must be a number (integer or float) and can't be equal to 0
    all elements of the matrix should be divided by div

    Parameters:
    matrix: the matrix of integers or floats
    div: the number to divide by

    Returns: a new matrix rounded to 2 decimal places

    Raises:
    TypeError if inputs are not integer or float
    TypeError if the row of the matrix are not the same size
    TypeError if div is not an integer or a float
    ZeroDivisionError if div is equal to 0
    """
    # Check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if there are lists inside the list
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if elements in row are int or float
    if not all(isinstance(elem, (int, float)) for row in matrix
               for elem in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if rows are the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([round(x / div, 2) for x in matrix[i]])
    return new_matrix
