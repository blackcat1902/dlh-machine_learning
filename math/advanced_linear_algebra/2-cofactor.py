#!/usr/bin/env python3
def determinant(matrix):
    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        minor = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def cofactor(matrix):
    """Calculates the cofactor matrix"""

    # Validate matrix is a list of lists
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Validate non-empty square matrix
    if (len(matrix) == 0 or
            any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case: 1x1 matrix
    if len(matrix) == 1:
        return [[1]]

    n = len(matrix)
    cofactor_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            # Build minor (submatrix)
            submatrix = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]

            # Compute cofactor with sign
            sign = (-1) ** (i + j)
            value = sign * determinant(submatrix)
            row.append(value)

        cofactor_matrix.append(row)

    return cofactor_matrix
