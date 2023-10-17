import mubody.constants as cte
from mubody import numeric as nm
import numpy as np
from numba import jit


def gravity_law(m, r):
    """
    Law of universal gravitation

    Parameters
    ----------
    m : float
        mass of celestial body source of gravity
    r : ndarray (3,n)
        object position vector

    Returns
    -------
    a : ndarray (3,n)
        gravitational acceleration

    References
    ----------
    .. [1] Elices T. (1991). Introduccion a la Dinanica Espacial. INTA.

    """

    a = - cte.G * m * r/np.linalg.norm(r, axis=0)**3

    return a


def gravity_jacobian(m, r):
    """
    Jacobian of two body problem equations

    Parameters
    ----------
    m : float
        mass of celestial body source of gravity
    r : ndarray (3,1)
        object position vector

    Returns
    -------
    M : ndarray (3,3)
        Jacobian

    References
    ----------
    .. [1] Elices T. (1991). Introduccion a la Dinanica Espacial. INTA.

    """

    M = np.zeros([6, 6])
    _, n = r.shape

    if n > 1:
        raise ValueError("ValueError exception thrown")

    x, y, z = r[:, 0]

    r_mod = np.sqrt(x * x + y * y + z * z)

    mu = cte.G * m

    Uxx = mu * (3 * x**2/r_mod**5 - 1/r_mod**3)
    Uyy = mu * (3 * y**2/r_mod**5 - 1/r_mod**3)
    Uzz = mu * (3 * z**2/r_mod**5 - 1/r_mod**3)

    Uxy = 3 * mu * x * y/r_mod**5
    Uyx = Uxy
    Uxz = 3 * mu * x * z/r_mod**5
    Uzx = Uxz
    Uyz = 3 * mu * y * z/r_mod**5
    Uzy = Uyz

    M[3, 0] = Uxx
    M[4, 1] = Uyy
    M[5, 2] = Uzz

    M[3, 1] = Uxy
    M[4, 0] = Uyx

    M[3, 2] = Uxz
    M[5, 0] = Uzx

    M[4, 2] = Uyz
    M[5, 1] = Uzy

    M[0, 3] = 1
    M[1, 4] = 1
    M[2, 5] = 1

    return M


@jit
def U_gradient(mu, state):
    """Returns gradient from gravity potential"""

    x, y, z, _, _, _ = state

    r1 = nm.norm_sc(x + mu, y, z)
    r2 = nm.norm_sc(x + mu - 1, y, z)

    r1_pow_3 = r1**3
    r2_pow_3 = r2**3

    Ux = x - (1 - mu) * (x + mu)/r1_pow_3 - mu * (x + mu - 1)/r2_pow_3
    Uy = y - (1 - mu) * y/r1_pow_3 - mu * y/r2_pow_3
    Uz = -(1 - mu) * z/r1_pow_3 - mu * z/r2_pow_3

    return Ux, Uy, Uz


@jit
def F(mu, t, U):
    """
    Equation of motion for N-body problem

    Parameters
    ----------
    t : float
        time
    U : ndarray
        state vector

    Returns
    -------
    Up : ndarray (6, n)
        derivate of state vector
    """

    _, _, _, vx, vy, vz = U

    Ux, Uy, Uz = U_gradient(mu, U)

    return vx, vy, vz, 2 * vy + Ux, -2 * vx + Uy, Uz
