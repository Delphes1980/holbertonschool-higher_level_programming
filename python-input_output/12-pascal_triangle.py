#!/usr/bin/python3
""" This module defines a Student """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    of n

    Args:
    n: an integer
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range (n - 1):
        current_line = []
        for j in range(i):
            if j == 0 or j == i:
                current_line = current_line[1]
            else:
                previous_line = triangle[i - 1]
                value = previous_line[j - 1] + previous_line[j]
                current_line.append(value)
        triangle.append(current_line)
    return triangle
