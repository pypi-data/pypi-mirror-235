import os
import numpy as np
import pandas as pd
import pickle
import scipy.io
from astropy.time import TimeFormat
import mubody.numeric as nm
from scipy.interpolate import interp1d


def store(data, file_name, dir_name):
    """
    Stores data in pickle object

    Parameters
    ----------
    data : -
        Data to be stored
    file_name : str
        File name
    dir_name : str
        Folder name
    """

    file_path = "Results/" + dir_name

    os.makedirs(file_path, exist_ok=True)

    file_handler = open(file_path + "/" + file_name, 'wb')

    pickle.dump(data, file_handler)

    file_handler.close()

    return 0


def recover(file_name, dir_name):
    """
    Recovers data from pickle object

    Parameters
    ----------
    file_name : str
        File name
    dir_name : str
        Folder name

    Returns
    -------
    data : -
        Data retrieved
    """

    file_path = "Results/" + dir_name
    file_handler = open(file_path + "/" + file_name, 'rb')

    data = pickle.load(file_handler)

    file_handler.close()

    return data


def extract_points(ref_orbit, N_segment):
    tf = ref_orbit.mt()
    time_segment_point = np.linspace(0, tf, N_segment + 1)

    # create df with the time of each point
    point_time_ar = ref_orbit.s(time_segment_point)
    point_df = pd.DataFrame(columns=ref_orbit.trajectory.df.columns, data=point_time_ar.T, index=time_segment_point)

    return point_df


def save_mat(file_name, data, data_name):
    """
    Saves data in a .mat file

    Parameters
    ----------
    file_name : str
        Data to be stored
    data : -
        Variable to be saved
    data_name : str
        Name of the variable
    """

    file_path = "Results"

    os.makedirs(file_path, exist_ok=True)

    scipy.io.savemat(file_path + "/" + file_name, {data_name: data})

    print("Data successfully saved")

    return 0


def load_mat(file_name):
    """
    Loada data from .mat file

    Parameters
    ----------
    file_name : str
        Name of the .mat file

    Returns
    -------
    data_loaded : -
        Data retrieved
    """

    file_path = "Results"

    data_loaded = scipy.io.loadmat(file_path + "/" + file_name)

    print("Data successfully loaded")

    return data_loaded


class TimeMJDG(TimeFormat):
    """
    Modified Julian Date GMAT time format.
    """
    name = 'mjdg'  # Unique format name

    def set_jds(self, val1, val2):
        self._check_scale(self._scale)  # Validate scale.
        jd1, jd2 = val1, val2
        self.jd1, self.jd2 = jd1, jd2

    @property
    def value(self):
        return self.jd1 + self.jd2 - 2430000.0


class frame:
    """
    This is the basic frame class from which all other frame classes are derived

    The position and the center of the frame regarding the Sun (in FK5) can be retrieved

    """
    ftype = None

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

    ftype = 'FK5'

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

    ftype = 'Synodic'

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

        x_syn_norm = r/nm.norm(r.T)
        y_syn_norm = v/nm.norm(v.T)

        z_syn = np.cross(x_syn_norm, y_syn_norm)
        z_syn_norm = z_syn/nm.norm(z_syn.T)

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

        x_syn_norm = r/nm.norm(r.T)
        # y_syn_norm = v/nm.norm(v.T)

        z_syn = np.cross(r, v)
        z_syn_norm = z_syn/nm.norm(z_syn.T)

        xp_syn_norm = v/nm.norm(r.T) - np.einsum('i,ij->ij',  np.einsum('ij,ij->i', x_syn_norm, v), x_syn_norm/nm.norm(r.T))  # noqa

        zp_syn_norm = np.cross(r, a)/nm.norm(z_syn.T) - np.einsum('i,ij->ij', np.einsum('ij,ij->i', np.cross(r, a), z_syn_norm), z_syn_norm/nm.norm(z_syn.T))  # noqa

        yp_syn_norm = np.cross(zp_syn_norm, x_syn_norm) + np.cross(z_syn_norm, xp_syn_norm)

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

    ftype = 'SynodicIdeal'

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
        if (self.origin.cetype == 'libration_point'):
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

    gamma = np.arccos((a**2 + b**2 - c**2)/(2 * a * b))

    return gamma


def trajectory_comparison(reference_trajectory, compared_trajectory, N=1000):
    """
    Compares two trajectories with RMSE

    Parameters
    ----------
    reference_trajectory : pandas DataFrame
        Trajectory A
    compared_trajectory : pandas DataFrame
        Trajectory B
    N : int
        Number of points used to compare

    Returns
    -------
    r_drift : 1D-array
        Distance between trajectories over time
    drift : ndarray (3,n)
        Difference between trajectories
    """

    time_A = reference_trajectory.index.values
    time_B = compared_trajectory.index.values

    r_A = reference_trajectory[['x', 'y', 'z']].values.T
    r_B = compared_trajectory[['x', 'y', 'z']].values.T

    v_A = reference_trajectory[['vx', 'vy', 'vz']].values.T
    v_B = compared_trajectory[['vx', 'vy', 'vz']].values.T

    t0 = max(time_A[0], time_B[0])
    tf = min(time_A[-1], time_B[-1])

    time = np.linspace(t0, tf, N)

    f_r_A = interp1d(time_A, r_A, kind='cubic')
    f_r_B = interp1d(time_B, r_B, kind='cubic')

    reference_interpolated_r = f_r_A(time)
    compared_interpolated_r = f_r_B(time)

    drift_r = reference_interpolated_r - compared_interpolated_r

    drift_r_norm = np.linalg.norm(drift_r, axis=0)

    f_v_A = interp1d(time_A, v_A, kind='cubic')
    f_v_B = interp1d(time_B, v_B, kind='cubic')

    reference_interpolated_v = f_v_A(time)
    compared_interpolated_v = f_v_B(time)

    drift_v = reference_interpolated_v - compared_interpolated_v

    drift_v_norm = np.linalg.norm(drift_v, axis=0)

    return time, drift_r, drift_r_norm, drift_v, drift_v_norm
