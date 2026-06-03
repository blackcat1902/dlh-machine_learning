#!/usr/bin/env python3

def poly_derivative(poly):

    # 1. Check if poly is a list
    if not isinstance(poly, list):
        return None

    # 2. Check if the list is empty
    if len(poly) == 0:
        return None

    # 3. Check if all elements are numbers
    for element in poly:
        if not isinstance(element, (int, float)):
            return None

    # 4. Create an empty list for the derivative
    derivative = []

    # 5. Compute the derivative
    for i in range(1, len(poly)):
        new_value = i * poly[i]
        derivative.append(new_value)

    # 6. If derivative is empty, return [0]
    if len(derivative) == 0:
        return [0]

    # 7. Check if all values in derivative are 0
    all_zero = True
    for value in derivative:
        if value != 0:
            all_zero = False
            break

    if all_zero:
        return [0]

    # 8. Return the result
    return derivative
