
#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis."""

    # axis = 0 → concatenate along rows
    if axis == 0:
        # check if number of columns is the same
        if len(mat1[0]) != len(mat2[0]):
            return None

        result = []

        # copy mat1
        for row in mat1:
            result.append(row[:])

        # add mat2
        for row in mat2:
            result.append(row[:])

        return result

    # axis = 1 → concatenate along columns
    if axis == 1:
        # check if number of rows is the same
        if len(mat1) != len(mat2):
            return None

        result = []

        for i in range(len(mat1)):
            new_row = []

            # add elements from mat1
            for x in mat1[i]:
                new_row.append(x)

            # add elements from mat2
            for x in mat2[i]:
                new_row.append(x)

            result.append(new_row)

        return result

    return None
