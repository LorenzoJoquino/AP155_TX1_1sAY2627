import numpy as np
import matplotlib.pyplot as plt


def createZerosArray(rowZeros, columnZeros):
    return np.zeros((rowZeros, columnZeros))

def calc_T(A, B, M):
    a = np.radians(A)
    b = np.radians(B)
    x = np.array([[np.cos(a), np.cos(b)],[np.sin(a), np.sin(b)]])
    y = np.array([0, M*9.81])
    return np.linalg.solve(x,y)