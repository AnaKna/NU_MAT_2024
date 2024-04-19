import numpy as np
import os
import sys

# Add the path to the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now you can import modules from the src directory
from src.Data_type import ZgornjaDvodiagonalna
from src.Data_type import Givens

def QR_Givens_OPT(matrix):
    # Ensure that the matrix is in the form of np.array()
    matrix = np.array(matrix)
    (num_rows, num_cols) = np.shape(matrix)
    
    # Initialize Q as the identity matrix and R as a copy of the input matrix
    Q = np.identity(num_rows)
    R = matrix.copy()
    
    # Store the Givens rotations and their indices
    Q_givens_rotations = []
    Q_givens_index = []
    
    # Iterate over each column
    for col in range(num_cols):
        # Iterate over each row below the diagonal of the current column
        for row in range(col + 1, num_rows):
            # Compute the Givens rotation for the current element and the corresponding element above the diagonal
            a = R[col, col]
            b = R[row, col]
            if b != 0:
                r = np.hypot(a, b)
                c = a / r
                s = -b / r
                
                # Update the elements of the R matrix with the Givens rotation
                R[col:col+2] = np.array([[c, -s], [s, c]]) @ R[col:col+2]
                
                # Update the elements of the Q matrix with the Givens rotation
                Q[:, col:col+2] = Q[:, col:col+2] @ np.array([[c, -s], [s, c]])
                
                # Store the Givens rotation and its indices
                Q_givens_rotations.append([c, s])
                Q_givens_index.append([row, col])
    
    # Convert R to upper bidiagonal form
    R = ZgornjaDvodiagonalna(R)
    
    # Create the Givens object
    Q_givens = Givens(Q_givens_rotations, Q_givens_index)
    
    return Q, R, Q_givens
