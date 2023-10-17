import numpy as np


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def cosine_law(a, b, gamma):
    """
    Computes the missing side of the triangle

    Parameters
    ----------
    a : float
        Lenght of side a
    b : float
        Length of side b
    gamma : float
        Angle between sides a and b (rad)


    Returns
    -------
    c : float
        Length of the missing side c

    """

    c = np.sqrt(a**2 + b**2 - 2 * a * b * np.cos(gamma))

    return c


def cosine_law_inverse(a, b, c):
    """
    Computes the angle opposed to the c side

    Parameters
    ----------
    a : float
        Lenght of side a
    b : float
        Length of side b
    c : float
        Length of side c

    Returns
    -------
    gamma : float
        Angle between a and b sides (rad)

    """

    gamma = np.arccos((a**2 + b**2 - c**2) / (2 * a * b))

    return gamma
