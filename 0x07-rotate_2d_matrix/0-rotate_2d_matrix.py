#!/usr/bin/python3
""" This module contains a function that roates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    """
    len_mat = len(matrix)

    # Transpose the matrix
    for i in range (len_mat):
        for j in range(i, len_mat):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the 2d array    
    for i in range(len_mat):
        matrix[i].reverse()
