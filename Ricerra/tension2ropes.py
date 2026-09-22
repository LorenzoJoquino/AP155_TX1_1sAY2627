import numpy as np

def coef(alpha,beta):
    r1 = np.array([np.cos(alpha),-np.cos(beta)])
    r2 = np.array([np.sin(alpha),np.sin(beta)])
    return np.array([r1,r2])

def solve(coef, extForces):
    return np.linalg.solve(coef, extForces)
    