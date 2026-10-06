import numpy as np

def tension(a, b, M):
    A = np.array([[np.cos(a), -np.cos(b)], [np.sin(a), np.sin(b)]]) #coefficient matrix
    w = np.array([0, 9.81*M]) #product matrix
   
    return np.linalg.solve(A, w) 

