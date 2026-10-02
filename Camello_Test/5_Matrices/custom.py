import numpy as np
import matplotlib.pyplot as plt


def createZerosArray(rowZeros, columnZeros):
    return np.zeros((rowZeros, columnZeros))

def tension(alpha_deg, beta_deg, mass_kilograms):

    alpha_rad = np.radians(alpha_deg)
    beta_rad = np.radians(beta_deg)
    grav = 9.81

    angles = [[np.sin(alpha_rad), np.sin(beta_rad)],[-np.cos(alpha_rad), np.cos(beta_rad)]]
    solution = [mass_kilograms * grav, 0]

    tension = np.linalg.solve(angles, solution)
    return tension