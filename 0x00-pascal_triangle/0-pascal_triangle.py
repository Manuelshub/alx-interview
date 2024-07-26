#!/usr/bin/python3
"""
This module contains my implementation of the pascal's triangle
"""


def pascal_triangle(n):
    """
    This method implements the pascal's triangle
    """
    triangle = []

    if n <= 0:
        return []

    for row in range(n):
        inner = [combs(row, col) for col in range(row + 1)]
        triangle.append(inner)

    return triangle


def fact(n):
    """
    This method implements factorial.
    """
    if n < 1:
        return 1
    return n * fact(n - 1)


def combs(n, m):
    """
    This method implements combination(nCm = n! / m! * (n - m)!​)
    """
    return fact(n) // (fact(m) * fact(n - m))
