import numpy as np

gravity = 9.81

def compute_tension(alpha, beta, mass):
    A = np.array([[-np.cos(alpha), np.cos(beta)],
              [np.sin(alpha), np.sin(beta)]])
    b = np.array([0, mass*gravity])
    return np.linalg.solve(A,b)
