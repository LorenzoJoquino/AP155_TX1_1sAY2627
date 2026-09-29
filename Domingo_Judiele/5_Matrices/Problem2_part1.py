"""
M = mass
let T1 = tension of rope with angle alpha (left rope), T2 = tension of rope with angle Beta (right rope)
from equilibrium equations:
x-axis: -T1cos(a) + T2cos(b) = 0
y-axis = T1sin(a) + T2cos(a) = Mg

let coefficient vector = A
x = [T1, T2]
b = [0,Mg]
"""
import numpy as np
def get_Tensions (M, alpha, beta, g):
    rad_alpha = np.radians(alpha)
    rad_beta = np.radians(beta)
    A = np.array([[-np.cos(rad_alpha),np.cos(rad_beta)],
                  [np.sin(rad_alpha),np.sin(rad_beta)]])
    b = np.array([0, M*g])
    T1, T2 = np.linalg.solve (A,b)
    return T1, T2
