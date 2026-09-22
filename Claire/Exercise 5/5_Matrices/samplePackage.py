
# Making the function that calculates tension on each of the ropes
import numpy as np

def solve_rope_tensions(M, alpha_deg, beta_deg, g=9.8):
    alpha_rad = np.radians(alpha_deg)
    beta_rad = np.radians(beta_deg)

    A = np.array([[np.cos(alpha_rad), -np.cos(beta_rad)], [np.sin(alpha_rad), np.sin(beta_rad)]])
    b = np.array([0, M*g])

    b_transpose = np.transpose(b)

    T1, T2 = np.linalg.solve(A, b_transpose)

    return T1, T2
