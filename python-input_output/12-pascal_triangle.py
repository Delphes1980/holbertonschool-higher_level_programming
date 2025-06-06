#!/usr/bin/python3
""" This module defines a function to generate a Pascal's triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    of n rows

    Args:
    n: the number of rows to generate

    Returns:
    A list of lists of integers representing Pascal's triangle
    Return an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = []
    # Iteration through the row to be generated (from 0 to n-1)
    for i in range(n):
        current_line = []
        # Iteration through the current row (each row 'i' has 'i + 1' elements
        for j in range(i + 1):
            # first & last element of every row are always 1
            if j == 0 or j == i:
                current_line.append(1)
            else:
                # for middle elements, sum the 2 numbers from the previous row
                previous_line = triangle[i - 1]
                value = previous_line[j - 1] + previous_line[j]
                current_line.append(value)
        # Add the completed current row to the main triangle list
        triangle.append(current_line)
    return triangle
