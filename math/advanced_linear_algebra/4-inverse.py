#!/usr/bin/env python3

def inverse(matrix):
    """
    Compute the inverse of a square matrix using
    determinant and adjugate method.
    """

    # Type checks
    if not isinstance(matrix, list) or any(not isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists")

    # Empty or non-square check
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if any(len(r) != size for r in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Compute determinant
    det_val = determinant(matrix)

    # If determinant is zero → no inverse
    if det_val == 0:
        return None

    # Get adjugate matrix
    adj_matrix = adjugate(matrix)

    # Build inverse matrix
    inverse_mat = []

    for row in range(size):
        new_row = []
        for col in range(size):
            new_row.append(adj_matrix[row][col] / det_val)
        inverse_mat.append(new_row)

    return inverse_mat