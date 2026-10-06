
import numpy as np

G = 9.81  # gravitational acceleration, m/s^2


def rope_tensions(M, alpha_deg, beta_deg, g=G):
    """Tensions in two ropes holding a mass M (kg) at rest.

    Rope 1 makes angle alpha_deg and rope 2 angle beta_deg with the ceiling,
    in degrees, on opposite sides of the mass. Returns (T1, T2) in newtons
    by solving the force balance on the knot:
        -T1 cos(alpha) + T2 cos(beta) = 0
         T1 sin(alpha) + T2 sin(beta) = M g
    """
    a, b = np.radians(alpha_deg), np.radians(beta_deg)
    A = np.array([[-np.cos(a), np.cos(b)],
                  [ np.sin(a), np.sin(b)]])
    rhs = np.array([0.0, M*g])
    return tuple(np.linalg.solve(A, rhs))
