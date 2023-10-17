import numpy as np
from astropy import units as u
from scipy import optimize
import mubody.constants as cte


def Bm(rper, Vinf, mu):
    """
    Module of B-point vector.

    Calculated from the Vinf of the incoming trajectory and the periapsis radius
    of the target orbit.

    Parameters
    ----------
    rper : float
        Perigee radius [km]
    Vinf : float
        Hyperbolic excess of velocity [km/s]
    mu : float
        Standard gravitational parameter [km3/s2]

    Returns
    -------
    Bmod : float
        Module of the B-point vector [km]
    """

    Bmod = rper / Vinf * np.sqrt(Vinf**2 + 2 * mu / rper)

    return Bmod


def DeltaV_fb(rper, Vinf, mu):
    """
    Delta-v obtained during a flyby.

    Calculated from the Vinf of the incoming trajectory and the periapsis radius
    of the flyby trajectory.

    Parameters
    ----------
    rper : float
        Perigee radius [km]
    Vinf : float
        Hyperbolic excess of velocity [km/s]
    mu : float
        Standard gravitational parameter [km3/s2]

    Returns
    -------
    DV : float
        Delta-v gained by the S/C [km/s]
    """

    DV = 2 * Vinf / (1 + rper * Vinf**2 / mu)

    return DV


def rocket_eq(Isp, mi, mf):
    """
    Tsiolkovsky rocket equation.

    Computes the DeltaV obtained from a rocket which has consumed a certain
    amount of propellant.

    Parameters
    ----------
    Isp : float
        Engine specific impulse [s]
    mi : float
        Initial mass (m0 + mp) [kg]
    mf : float
        Final mass after burn (m0) [kg]

    Returns
    -------
    DV : float
        Resulting delta-v [km/s]
    """

    DV = Isp * cte.g0 * np.log(mi / mf)/1000

    return DV


def rocket_eq_mi(Isp, DV, mf):
    """
    Tsiolkovsky rocket equation inverse to obtain initial mass.

    Computes the propellant mass required to obtain a given delta-v in a rocket
    with a fixed dry mass.

    Parameters
    ----------
    Isp : float
        Engine specific impulse [s]
    DV : float
        Delta-v performed [km/s]
    mf : float
        Final mass after burn (m0) [kg]

    Returns
    -------
    mi : float
        Initial mass (m0 + mp) [kg]
    """

    mi = mf * np.exp(1000 * DV / (Isp * cte.g0))

    return mi


def reqins(Isp, DV, mf):
    """
    Tsiolkovsky rocket equation inverse applied to a sequence of delta-v.

    Computes the propellant mass required to obtain each delta-v in a rocket
    with a fixed dry mass.

    Parameters
    ----------
    Isp : float
        Engine specific impulse [s]
    DV : float, list
        Delta-v performed [km/s]
    mf : float
        Final mass after burn (m0) [kg]

    Returns
    -------
    mi : float, list
        Initial mass (m0 + mp) [kg]
    """

    mi = [mf]

    for impulse in DV:
        mi.append(rocket_eq_mi(Isp, impulse, mi[-1]))

    mi.reverse()

    return mi


def lambert(r1, r2, alpha, TOF, nu_guess=0):
    """
    Solves lambert problem for circular and coplanar orbits.

    Parameters
    ----------
    r1 : float
        Semi-major axis of departure planet [km]
    r2 : float
        Semi-major axis of arrival planet [km]
    alpha : float
        Angle between r1 and r2 vectors [rad]
    TOF : float
        Time of flight [days]
    nu_guess : float, optional
        Initial guess for departure TA [rad]

    Returns
    -------
    a : float
        Semi-major axis of transfer orbit [km]
    e : ndarray
        Eccentricity of transfer orbit [-]
    nu : float, optional
        TA of departure [rad]

    """

    def lambert_equation(nu0):
        """
        Computes difference between desired TOF and current TOF.

        Parameters
        ----------
        nu0 : float
            Departure TA [rad]

        Returns
        -------
        residue : float
            Difference between TOFs [days]

        References
        ----------
        .. [1] Elices T. (1991). Introduccion a la Dinamica Espacial. INTA. (Corrected)
        """

        e = (r2 - r1) / (r1 * np.cos(nu0) - r2 * np.cos(nu0 + alpha))

        f = np.sqrt(1 - e**2)

        q1 = 2 * np.arctan(f * np.tan((alpha + nu0) / 2) / (1 + e))
        q2 = (e * f * np.sin(alpha + nu0)) / (1 + e * np.cos(alpha + nu0))
        q3 = 2 * np.arctan((f * np.tan(nu0 / 2)) / (1 + e))
        q4 = e * f * np.sin(nu0) / (1 + e * np.cos(nu0))

        residue = TOF - 365.25 / (2 * np.pi) * (q1 - q2 + q3 - q4)

        return residue

    nu = optimize.fsolve(lambert_equation, x0=nu_guess)[0]

    e = (r2 - r1) / (r1 * np.cos(nu) - r2 * np.cos(nu + alpha))
    p = r1 * (1 + e * np.cos(nu))
    a = p / (1 - e**2)

    return a, e, nu


def energy(mu, a):
    """
    Computes orbit energy.

    Parameters
    ----------
    mu : float
        Standard gravitational parameter of the central body [km3/s2]
    a : float
        Semi-major axis of the orbit [km]

    Returns
    -------
    energy : float
        Orbit energy [km2/s2]
    """

    energy = -mu / (2 * a)

    return energy


def velocity_from_energy(mu, energy, r):
    """
    Computes velocity in a given orbital position from energy.

    Parameters
    ----------
    mu : float
        Standard gravitational parameter of the central body [km3/s2]
    energy : float
        Orbital energy [km2/s2]
    r : float
        Distance to central body [km]

    Returns
    -------
    v : float
        Orbital velocity [km/s]
    """

    v = np.sqrt(2 * (energy + mu / r))

    return v


def velocity_circular_orbit(mu, a):
    """
    Computes velocity of a circular orbit.

    Parameters
    ----------
    mu : float
        Standard gravitational parameter of the central body [km3/s2]
    a : float
        Semi-major axis of the orbit [km]

    Returns
    -------
    v : float
        Orbital velocity [km/s]
    """

    v = np.sqrt(mu / a)

    return v


def solve_kepler_equation(n, e, TOF, E=0.1):
    """
    Solves kepler equation iteratively

    Parameters
    ----------
    n : float
        Mean angular motion [rad/s]
    e : float
        Orbit eccentricity [-]
    E : float
        Eccentric anomaly, staring guess [rad]

    Returns
    -------
    E : float
        Eccentric anomaly, converged value [rad]
    """

    error_threshold = 1e-3
    error = 1

    while error > error_threshold:
        E0 = E
        E = (n * TOF + e * np.sin(E)) * u.rad
        error = abs((E0 - E) / E0)

    return E


def ss_inclination(a, e=0):
    """
    Calculates critical inclination for a sunsynchronous orbit around Earth.

    Parameters
    ----------
    a : float
        semi-major axis of the orbit [km]
    e : float
        Orbit eccentricity [-] (optional)

    Returns
    -------
    i : float
        Inclination of the sunsynchronous orbit [deg]
    """

    mu = 3.986e5  # Earth standard gravitational parameter [km3/s2]
    T = 365.25 * 86400  # Earth orbital period around Sun [days]
    J2 = 1.0826e-3  # Earth J2
    Re = 6378  # Earth radius [km]

    omega_sun = 2 * np.pi / T
    n = np.sqrt(mu / a**3)
    p = a * (1 - e**2)

    i = np.arccos(-2 * omega_sun * p**2 / (3 * n * Re**2 * J2)) * 180 / np.pi

    return i
