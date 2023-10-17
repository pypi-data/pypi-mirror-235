import numpy as np
from mubody import constants as cte


def apparent_radius(R, d):
    """Computes apparent radius of a body of radius R and at a d distance

    Parameters
    ----------
    R : float
        Radius of the body [km] or [-].
    d : float
        Distance from the body [km] or [-].

    Returns
    -------
    Rp : float
        Apparent radius [rad]
    """

    Rp = np.arcsin(R / d)

    return Rp


def detect_eclipse(R_body, r_body, r_sun, r_sat, L=1.0):
    """Detects eclipses caused by a potential occulting body and computes
    the fraction of the apparent solar disk that is in view from the
    perspective of a spacecraft

    Parameters
    ----------
    R_body : Primary
        Occulting body radius [km].
    r_body : ndarray
        Position of the occulting body [km] or [-].
    r_sun : ndarray
        Position of the Sun [km] or [-].
    r_sat : ndarray
        Position of the satellite [km] or [-].
    L : float
        Adimensionalization factor for distance

    Returns
    -------
    eclipse : bool
        If True, there is an eclipse.
    p : float
        Fraction of the apparent solar disk that is in view from the
        perspective of a spacecraft.

    """

    # Normalize bodies radius
    R_sun = cte.R_sun / L
    R_body /= L

    # Position vectors from the occulting body to the satellite and the sun
    s_sat = r_sat.flatten() - r_body
    s_sun = r_sun - r_body

    # Apparent radius
    Rp_sun = apparent_radius(R_sun, np.linalg.norm(s_sun))
    Rp_body = apparent_radius(R_body, np.linalg.norm(s_sat))

    # Apparent separation
    Dp = np.arccos(
        -np.dot(s_sat, (r_sun - r_sat.flatten()))
        / (np.linalg.norm(s_sat) * np.linalg.norm(r_sun - r_sat.flatten()))
    )

    if Dp >= Rp_sun + Rp_body:
        p = 0
        eclipse = False
    elif Dp <= Rp_body - Rp_sun:
        p = 1
        eclipse = True
    else:
        eclipse = True
        if Dp > abs(Rp_sun - Rp_body) and Dp < Rp_sun + Rp_body:
            c1 = (Dp**2 + Rp_sun**2 - Rp_body**2) / (2 * Dp)
            c2 = np.sqrt(Rp_sun**2 - c1**2)

            A = (
                Rp_sun**2 * np.arccos(c1 / Rp_sun)
                + Rp_body**2 * np.arccos((Dp - c1) / Rp_body)
                - Dp * c2
            )
            p = A / (np.pi * Rp_sun**2)
        else:
            p = Rp_body**2 / Rp_sun**2

    return eclipse, p
