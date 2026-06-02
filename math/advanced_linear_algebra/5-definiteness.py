import numpy as np

def definiteness(matrix):
    # Check if input is numpy array
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    # Check if matrix is valid (must be square)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    
    try:
        # Compute eigenvalues
        eigenvalues = np.linalg.eigvals(matrix)
    except Exception:
        return None
    
    tol = 1e-8
    
    # Check conditions
    if np.all(eigenvalues > tol):
        return "Positive definite"
    
    elif np.all(eigenvalues >= -tol) and np.any(np.abs(eigenvalues) <= tol):
        return "Positive semi-definite"
    
    elif np.all(eigenvalues < -tol):
        return "Negative definite"
    
    elif np.all(eigenvalues <= tol) and np.any(np.abs(eigenvalues) <= tol):
        return "Negative semi-definite"
    
    elif np.any(eigenvalues > tol) and np.any(eigenvalues < -tol):
        return "Indefinite"
    
    else:
        return None