#!/usr/bin/python3
"""
Returns a list of lists of integers representing
the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """Generates the Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
