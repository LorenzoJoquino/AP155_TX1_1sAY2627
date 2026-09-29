import numpy as np
import matplotlib.pyplot as plt


def createZerosArray(rowZeros, columnZeros):
    return np.zeros((rowZeros, columnZeros))

def T_solver(alpha, beta, M):  #M has unit [kg]
    B = np.array([[np.sin(alpha), np.sin(beta)], [-np.cos(alpha), np.cos(beta)]])
    F_vec = np.array([[M*9.81], [0]])
    return np.linalg.solve(B, F_vec).tolist()
