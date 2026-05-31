#!/usr/bin/env python3
"""Calculate the inverse of a matrix"""

def inverse(matrix):
    # Validate: must be a list of lists
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Validate: non-empty square matrix
    if (len(matrix) == 0 or
        any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    # Create augmented matrix [A | I]
    A = [row[:] for row in matrix]
    I = [[float(i == j) for j in range(n)] for i in range(n)]

    for i in range(n):
        # Find pivot
        pivot = A[i][i]

        # If pivot is zero, try to swap with a lower row
        if pivot == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    I[i], I[j] = I[j], I[i]
                    pivot = A[i][i]
                    break
            else:
                return None  # Singular matrix

        # Normalize pivot row
        for j in range(n):
            A[i][j] /= pivot
            I[i][j] /= pivot

        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]

    return I
