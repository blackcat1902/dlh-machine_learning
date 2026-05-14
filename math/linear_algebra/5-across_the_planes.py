#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    """The function adds two matrices element-wise."""
    if len(mat1) != len(mat2):
        return None 

    result = []

    for i in range(len(mat1)):
        if len(mat1(i)) != len(mat2(i)):
            return None
            
        a = []
        for j in range (len(mat1[j]))
            a.append(mat1[i][j] + mat2[i][j])
        result.append(a)
    return result
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))