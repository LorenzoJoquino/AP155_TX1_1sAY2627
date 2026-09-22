import numpy as np
import math

alpha = math.pi / 4
beta = math.pi / 4
m , g = 10, 9.81
A = np.array([[np.sin(alpha), np.sin(beta)],[np.cos(alpha), -np.cos(beta)]])
b = np.array([m*g, 0])

def getTensions(A = A, b = b):
    x = np.linalg.solve(A, b)
    return x