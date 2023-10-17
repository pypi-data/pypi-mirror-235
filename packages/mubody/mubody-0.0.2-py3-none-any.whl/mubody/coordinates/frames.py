import numpy as np
import mubody.numeric as nm
from typing import Union


class frame:
    """
    This is the basic frame class from which all other frame classes are derived

    The position and the center of the frame regarding the Sun (in FK5) can be retrieved

    """

    ftype: Union[str, None] = None

    def __init__(self, origin):
        """
        Constructor

        Parameters
        ----------
        origin : str
            Name of celestial body/point used as origin
        dynamical_system : dynamical_system class
            Dynamical system with bodies and their properties
        """

        self.origin = origin

    def r_origin(self, t):
        """
        Retrieves the position of the frame origin regarding the Sun in FK5

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position of the origin regarding the Sun expressed in FK5
        """

        r = self.origin.r(t)

        return r

    def v_origin(self, t):
        """
        Retrieves the velocity of the frame origin regarding the Sun in FK5

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Velocity of the origin regarding the Sun expressed in FK5
        """

        v = self.origin.v(t)

        return v


class J2000Eq(frame):
    """
    This is the default inertial frame used in mubody. The system
    is also called FK5.

    The J2000Eq system is referenced to the Earth's equator and the
    Earth's orbit about the sun. Because neither of these two planes
    are fixed in space, we must pick an epoch and define an inertial
    system based on the geometry at that epoch. This epoch is commonly
    chosen as the J2000 epoch.

    The rigorous mathematical definition of J2000Eq is complex. The
    nominal X-axis points  the line formed by the intersection of the
    Earth's equatorial plane and the ecliptic plane, in the direction of
    Aries. The nominal Y-axis completes the right-handed system. Both
    the equatorial and ecliptic planes move slowly with respect to
    inertial space. The rigorous definition of J2000Eq uses the mean
    planes of the ecliptic and equator, at the J2000 epoch.
    (from GMATMathSpec)

    References
    ----------
    .. [1] GMAT Math Specification 2020a.

    """

    ftype = "FK5"

    def R(self, t):
        """
        Computes rotation matrix from this frame to FK5, wich results in
        the identity matrix.

        Rotation matrix R12 is built with the basis vectors of S2 in
        columns [i j k] expressed in S1.  u1 = R12 @ u2

        Parameters
        ----------
        t : 1D-array
            Instants of interest

        Returns
        -------
        C : ndarray (3,3,n)
            Rotation matrix from FK5 to FK5
        """

        r = len(t)

        C = np.broadcast_to(np.identity(3)[:, :, None], (3, 3, r))

        return C

    def Rp(self, t):
        """
        Computes the derivate of the rotation matrix from this frame to
        FK5, wich results in null matrix

        Rotation matrix Rp12 is built with the basis vectors derivate of
        S2 in columns [ip jp kp] expressed in S1.  u1 = R12 @ u2

        Parameters
        ----------
        t : 1D-array
            Instants of interest

        Returns
        -------
        Cp : ndarray (3,3,n)
            Derivate of rotation matrix of FK5 to FK5
        """

        r = len(t)

        Cp = np.broadcast_to(np.zeros(3)[:, :, None], (3, 3, r))

        return Cp


class Synodic(frame):
    """
    Basic synodic frame class

    This is a rotating frame, whose axes are defined by the motion of
    one object with respect to another object. It is adapted for the
    RTBP, using the primaries as these reference objects. The first
    primary (P1) is used as center and the line connecting it with the
    second primary (P2) defines the X-axis. The Z-axis is the primaries
    orbit plane normal and the Y-axis completes the right-handed frame.

    """

    ftype = "Synodic"

    def __init__(self, origin, p1, p2, DS):
        """
        Constructor

        Parameters
        ----------
        origin : str
            Name of celestial body/point used as origin
        dynamical_system : dynamical_system class
            Dynamical system with bodies and their properties
        """

        frame.__init__(self, origin)
        self.p1 = p1
        self.p2 = p2
        self.DS = DS

    def R(self, t):
        """
        Computes rotation matrix from this frame to FK5

        Rotation matrix R12 is built with the basis vectors of S2 in
        columns [i j k] expressed in S1.  u1 = R12 @ u2

        Parameters
        ----------
        t : 1D-array
            Instants of interest

        Returns
        -------
        C : ndarray (3,3,n)
            Rotation matrix from Synodic frame to FK5
        """

        # position and velocity matrix are transposed for cross product
        r = self.r_primary_2(t).T
        v = self.v_primary_2(t).T

        x_syn_norm = r / nm.norm(r.T)
        y_syn_norm = v / nm.norm(v.T)

        z_syn = np.cross(x_syn_norm, y_syn_norm)
        z_syn_norm = z_syn / nm.norm(z_syn.T)

        y_syn_norm = np.cross(z_syn_norm, x_syn_norm)

        # resulting array of vectors is reshaped to (3,1,n) before concatenating
        x_syn_norm = x_syn_norm.T.reshape(3, 1, -1)
        y_syn_norm = y_syn_norm.T.reshape(3, 1, -1)
        z_syn_norm = z_syn_norm.T.reshape(3, 1, -1)

        C = np.concatenate((x_syn_norm, y_syn_norm, z_syn_norm), axis=1)

        return C

    def Rp(self, t):
        """
        Computes the derivate of the rotation matrix from this frame to
        FK5, wich results in null matrix

        Rotation matrix Rp12 is built with the basis vectors derivate of
        S2 in columns [ip jp kp] expressed in S1.  u1 = R12 @ u2

        Parameters
        ----------
        t : 1D-array
            Instants of interest

        Returns
        -------
        Cp : ndarray (3,3,n)
            Derivate of rotation matrix from synodic frame to FK5
        """

        # position and velocity matrix are transposed for cross product
        r = self.r_primary_2(t).T
        v = self.v_primary_2(t).T
        a = self.a_primary_2(t).T

        x_syn_norm = r / nm.norm(r.T)
        # y_syn_norm = v/nm.norm(v.T)

        z_syn = np.cross(r, v)
        z_syn_norm = z_syn / nm.norm(z_syn.T)

        xp_syn_norm = v / nm.norm(r.T) - np.einsum(
            "i,ij->ij", np.einsum("ij,ij->i", x_syn_norm, v), x_syn_norm / nm.norm(r.T)
        )  # noqa

        zp_syn_norm = np.cross(r, a) / nm.norm(z_syn.T) - np.einsum(
            "i,ij->ij",
            np.einsum("ij,ij->i", np.cross(r, a), z_syn_norm),
            z_syn_norm / nm.norm(z_syn.T),
        )  # noqa

        yp_syn_norm = np.cross(zp_syn_norm, x_syn_norm) + np.cross(
            z_syn_norm, xp_syn_norm
        )

        # resulting array of vectors is reshaped to (3,1,n) before concatenating
        xp_syn_norm = xp_syn_norm.T.reshape(3, 1, -1)
        yp_syn_norm = yp_syn_norm.T.reshape(3, 1, -1)
        zp_syn_norm = zp_syn_norm.T.reshape(3, 1, -1)

        Cdot = np.concatenate((xp_syn_norm, yp_syn_norm, zp_syn_norm), axis=1)

        return Cdot

    def r_primary_2(self, t):
        """
        Retrieves the position of the second primary (P2) regarding first (P1).
        Expressed in FK5

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position of P2 regarding the Sun expressed in FK5
        """

        r = self.p2.r(t) - self.p1.r(t)

        return r

    def v_primary_2(self, t):
        """
        Retrieves the velocity of the second primary (P2) regarding first (P1).
        Expressed in FK5

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position of P2 regarding the Sun expressed in FK5
        """

        v = self.p2.v(t) - self.p1.v(t)

        return v

    def a_primary_2(self, t):
        """
        Computes the acceleration of the second primary (P2) regarding the Sun in FK5

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        a : ndarray (3,n)
            Acceleration of P2 in the dynamical system considered expressed in FK5
        """

        # get list of bodies considered in the dynamical model
        bodies = self.DS.bodies[:]
        bodies.remove(self.p2.name)

        a = np.zeros((3, len(t)))

        # assumed to be zero
        # for body in bodies:
        #     a += phy.gravity_law(self.DS.ss.bodies_dict[body].mass, self.r_primary_2(t))

        return a


class SynodicIdeal(Synodic):
    """
    This is a subclass of the Synodic class adapted for the CRTBP

    In the CRTBP it is assumed that the primaries have circular orbits. Therefore, to
    translate the results to J2000Eq or any other frame based on ephemeris, it is
    required to correct the ideal position of L2.
    """

    ftype = "SynodicIdeal"

    def __init__(self, origin, p1, p2, DS):
        """
        Constructor

        Parameters
        ----------
        origin : str
            Name of celestial body/point used as origin (Sun/L2)
        dynamical_system : dynamical_system class
            Dynamical system with bodies and their properties
        """

        Synodic.__init__(self, origin, p1, p2, DS)

        # origin to P1 distance
        if self.p1 is origin:
            d = 0
        if self.p2 is origin:
            d = DS.L
        if self.origin.cetype == "libration_point":
            d = (self.origin.xL + DS.mu) * DS.L

        self.r_origin_ideal = d

    def r_origin(self, time, ideal=False):
        """
        Retrieves the position of the frame origin regarding the Sun in FK5

        This method incorporates the correction to transforma between IdealSynodic
        and other frames

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position of the origin regarding the Sun expressed in FK5
        """

        if ideal:
            r = np.zeros((3, len(time)))
            r[0, :] = np.ones((1, len(time))) * self.r_origin_ideal
        else:
            r = self.origin.r(time)

        return r

    def v_origin(self, time):
        """
        Retrieves the velocity of the frame origin regarding the Sun in FK5

        This method incorporates the correction to transforma between IdealSynodic
        and other frames

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Velocity of the origin regarding the Sun expressed in FK5
        """

        v = self.origin.v(time)

        return v
