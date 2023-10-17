import numpy as np
import mubody.constants as cte
from mubody.utilities.eclipse import detect_eclipse


def _acceleration_srp(
    time,
    state,
    area,
    mass,
    reflectivity_coeff,
    solar_pressure,
    alpha,
    L,
    T,
    get_sun_position
):
    """Computes acceleration due to SRP

    Parameters
    ----------
    time : float
        Time [s], [-].
    state : ndarray
        State vector time series in inertial frame [km, km/s] or [-, -].
    area : float
        Area of the spacecraft surface exposed to the solar radiation [m2]
    mass : float
        Mass of the spacecraft [kg]
    reflectivity_coeff : float
        Coefficient of reflectivity.
    solar_pressure : float
        Solar pressure exerted by the solar radiation at 1 AU from the Sun [N/m2].
    alpha : float
        Angle between the surface and the Sun direction [deg].
    L : float
        Distance parameter, semi-major axis of m2 [km].
    T : float
        Time parameter, orbital period of m2 [s].
    get_sun_position : function
        Computes Sun position.

    Returns
    -------
    a : ndarray
        Acceleration [km/s2] or [-]
    """

    r_sun = get_sun_position(time)
    r_sun_from_sat = r_sun - state[:3].flatten()
    d_sun = np.linalg.norm(r_sun_from_sat)
    u_sun = r_sun_from_sat / d_sun

    # adimensionalization factor for acceleration [s2/m]
    # TODO for NBP this must change
    a_star = L / (T**2 / (2 * np.pi) ** 2)

    a = (
        solar_pressure
        * reflectivity_coeff
        * np.cos(alpha * np.pi / 180) ** 2
        * area
        / mass
        / (d_sun * L / cte.AU) ** 2
        / a_star
        * u_sun
    )

    return a


def _shadow_fraction(R_body, r_body, r_sun, r_sat, L):
    _, p = detect_eclipse(R_body, r_body, r_sun, r_sat, L)
    return p


class SRP:
    """Solar Radiation Pressure class

    This class computes the acceleration caused by the solar radiation pressure over
    a spacecraft with the given characteristics of area, mass, angle and reflectivity
    coefficient.

    Attributes
    ----------
    area : float
        Area of the spacecraft surface exposed to the solar radiation [m2]
    mass : float
        Mass of the spacecraft [kg]
    rc : float
        Coefficient of reflectivity.
    alpha : float
        Angle between the surface and the Sun direction [deg].
    ode : FunctionType
        Function that computes dot_state due to the perturbation
    solar_pressure : float
        Solar pressure exerted by the solar radiation at 1 AU from the Sun [N/m2].

    Methods
    -------
    _acceleration(state)
        Computes the value of the potential at a given state.
    _dot_state(state)
        Computes the first partial derivatives of the potential at a given state.
    """

    def __init__(self, area=1.0, mass=1.0, reflection_coeff=1.0, alpha=0.0):
        """Solar Radiation Pressure class

        This class computes the acceleration caused by the solar radiation pressure over
        a spacecraft with the given characteristics of area, mass, angle and reflectivity
        coefficient.

        Parameters
        ----------
        area : float
            Area of the spacecraft surface exposed to the solar radiation [m2]
        mass : float
            Mass of the spacecraft [kg]
        reflectivity_coeff : float
            Coefficient of reflectivity.
        alpha : function
            Decorated equations of motion.

        Methods
        -------
        _acceleration(state)
            Computes the acceleartion due to the solar radiation pressure.
        _dot_state(state)
            Computes the derivate of the 6-dim state for the perturbation.
        """

        self.area = area
        self.mass = mass
        self.rc = reflection_coeff
        self.alpha = alpha

        # Solar radiation pressure at 1 AU (Solar constant divided by light speed) [N/m2]
        self.solar_pressure = cte.SOLAR_PRESSURE

    def _acceleration(self, time, state, L, T, sun_function, bodies):
        """Computes acceleration due to SRP

        Parameters
        ----------
        time : float
            Time [s], [-].
        state : ndarray
            State vector time series in inertial frame [km, km/s] or [-, -].
        L : float
            Distance parameter, semi-major axis of m2 [km].
        T : float
            Time parameter, orbital period of m2 [s].
        get_sun_position : function
            Computes Sun position.
        bodies : list
            List of bodies that can cause eclipse.

        Returns
        -------
        a : ndarray
            Acceleration [km/s2] or [-]
        """

        # Compute acceleration
        a_no_shadow = _acceleration_srp(
            time,
            state,
            self.area,
            self.mass,
            self.rc,
            self.solar_pressure,
            self.alpha,
            L,
            T,
            sun_function,
        )

        # Sun position
        r_sun = sun_function(time)

        # Get primaries positions and radius
        p1, p2 = bodies
        mu = p2.mass / (p1.mass + p2.mass)

        r = []
        R = []

        # P1 is added only if it is not the Sun
        if p1.id != "10":
            r.append(np.array([-mu, 0, 0]))
            R.append(p1.radius)

        r.append(np.array([1 - mu, 0, 0]))
        R.append(p2.radius)

        p_bodies = []

        # Compute shadows
        for idx in range(len(R)):
            p_bodies.append(_shadow_fraction(R[idx], r[idx], r_sun, state[:3], L))

        # In case of multiple eclipse, keeps the larger
        p = max(p_bodies)

        # Apply shadow fraction to acceleration
        a = (1 - p) * a_no_shadow

        return a

    def _dot_state(self, time, state, L, T, sun_function, bodies):
        """Builds dot state from acceleration due to SRP

        Parameters
        ----------
        time : float
            Time [s], [-].
        state : ndarray
            State vector time series in inertial frame [km, km/s] or [-, -].
        L : float
            Distance parameter, semi-major axis of m2 [km].
        T : float
            Time parameter, orbital period of m2 [s].
        get_sun_position : function
            Computes Sun position.
        bodies : list
            List of bodies that can cause eclipse.

        Returns
        -------
        dot_state : ndarray
            Computes the derivate of the 6-dim state for the perturbation.
        """

        dot_state = np.zeros(6)
        dot_state[3:6] = self._acceleration(time, state, L, T, sun_function, bodies)

        return dot_state
