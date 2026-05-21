def determinant(matrix):
    # Validate matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Special case: [[]] → determinant = 1
    if matrix == [[]]:
        return 1

    # Validate matrix is square
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)

    # Base cases
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive Laplace expansion
    det = 0
    for col in range(n):
        # Build minor matrix
        minor = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]

        # Cofactor expansion
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det
