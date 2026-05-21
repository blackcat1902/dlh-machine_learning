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
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if (len(matrix) == 0 or
            any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    n = len(matrix)
    cof = []

    for i in range(n):
        row = []
        for j in range(n):
            submatrix = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]
            value = ((-1) ** (i + j)) * determinant(submatrix)
            row.append(value)
        cof.append(row)

    return cof


def adjugate(matrix):
    """Calculates the adjugate matrix"""

    # Validate matrix
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if (len(matrix) == 0 or
            any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    # Get cofactor matrix
    cof = cofactor(matrix)

    # Transpose cofactor matrix
    n = len(cof)
    adj = []

    for j in range(n):
        row = []
        for i in range(n):
            row.append(cof[i][j])
        adj.append(row)

    return adj