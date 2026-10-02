import numpy as np
import matplotlib.pyplot as plt

def comptens(M, alpha_deg, beta_deg, g=9.81):

    # convert from degrees to radians
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    
    # coefficient matrix A
    A = np.array([
        [-np.cos(alpha), np.cos(beta)],
        [np.sin(alpha), np.sin(beta)]
    ])
    
    # constant matrix B
    B = np.array([0, M * g])
    
    # Ax = B
    tensions = np.linalg.solve(A, B)
    return tensions[0], tensions[1]