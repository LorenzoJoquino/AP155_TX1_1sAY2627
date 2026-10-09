import numpy as np

def solve_rope_tensions(M, alpha_deg, beta_deg, g=9.81):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    
    A = np.array([
        [-np.cos(alpha),  np.cos(beta)],
        [ np.sin(alpha),  np.sin(beta)]
    ])
    
    b = np.array([0, M * g])
    
    T1, T2 = np.linalg.solve(A, b)
    return T1, T2