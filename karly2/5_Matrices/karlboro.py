import numpy as np

def calc_T(alpha, beta, M):
    # convert angles to radians
    a = np.radians(alpha)
    b = np.radians(beta)
    x = np.array([[np.cos(a), np.cos(b)],[np.sin(a), np.sin(b)]]) # coeff matrix
    y = np.array([0, M*9.81]) # output vector
    Ts = np.linalg.solve(x,y)
    for i, Ti in enumerate(Ts, start=1):
        print(f"T{i}={Ti}")
    return Ts
