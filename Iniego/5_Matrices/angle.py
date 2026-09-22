import numpy as np
import math

def tension_ab(a,b,m,g):
    """ The parameters are ([angle 1], [angle 2], [mass], [aceleration due to gravity])"""
    # Left hand side vector
    A = np.array([[np.cos(a), -np.cos(b)],[np.sin(a), np.sin(b)]], dtype=float)

    # Right hand side vector
    b = np.array([0, m*g], dtype=float)

    T = np.linalg.solve(A,b)
    return float(T[0]), float(T[1])