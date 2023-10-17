import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.interpolate import interp1d


pd.set_option("display.precision", 16)


class Satellite:

    def __init__(self, frame, **kwargs):
        # indicates wich mission has been simulated
        self.status = None
        self.name = "Default_sat"
        self.orbit = Orbit(frame)
        # Julian date 01/01/2000
        self.date = 51544

    def add_orbit(self, time, position, velocity, dim_status, frame):
        self.orbit.add_trajectory(time, position, velocity, dim_status, frame)

    def r(self, t):
        """
        Returns position of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        r_interp : ndarray (nx3)
            Array of positions for given times

        """

        r_interp = self.orbit.r(t)

        return r_interp

    def v(self, t):
        """
        Returns velocity of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        v_interp : ndarray (nx3)
            Array of velocities for given times
        """

        v_interp = self.orbit.v(t)

        return v_interp

    def s(self, t):
        """
        Returns state vector of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        s_interp : ndarray (nx6)
            Array of state vectors
        """

        s_interp = np.concatenate((self.r(t), self.v(t)))

        return s_interp


class Orbit:
    def __init__(self, frame):
        self.model = None
        self.trajectory = trajectory()
        self.frame = frame

    @property
    def tra_df(self):

        return self.trajectory.df

    def add_trajectory(self, time, position, velocity, dim_status, frame):
        self.trajectory.add(time, position, velocity, dim_status)
        self.frame = frame
        return 0

    def mt(self):
        """
        Returns mission time

        Returns
        -------
        mission_time : float
            Total mission time (seconds)
        """

        mission_time = self.trajectory.mt()

        return mission_time

    def r(self, t):
        """
        Returns position of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        r_interp : ndarray (nx3)
            Array of positions for given times
        """

        position = self.trajectory.r(t)

        return position

    def v(self, t):
        """
        Returns velocity of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        v_interp : ndarray (nx3)
            Array of velocities for given times
        """

        velocity = self.trajectory.v(t)

        return velocity

    def s(self, t):
        """
        Returns state vector of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        s_interp : ndarray (nx6)
            Array of state vectors
        """

        state = self.trajectory.s(t)

        return state

    def IC(self):
        IC = self.trajectory.IC()
        frame = self.frame

        return IC, frame


class trajectory:
    def __init__(self):
        self.df = pd.DataFrame(columns=['x', 'y', 'z', 'vx', 'vy', 'vz'])
        self.status = False
        self.dim_status = None

    def add(self, time, position, velocity, dimensions_flag):
        """
        Incorporates trajectory to orbit class

        Parameters
        ----------
        time : 1-D array (n)
            time
        position : ndarray (3,n)
            position vectors
        velocity : ndarray (3,n)
            velocity vectors
        dim_status : boolean
            if True, trajectory is dimensional
        """

        states = np.concatenate([position.T, velocity.T], axis=1)
        temp_df = pd.DataFrame(columns=self.df.columns, data=states, index=time)

        self.df = temp_df

        self.dim_status = dimensions_flag
        self.status = True

        self.generate_tck()

        return 0

    def adim(self, model):
        """
        Adimensionalize orbit

        Parameters
        ----------
        model : rnbp class
            Physical model
        """

        if self.dim_status:
            self.df.iloc[:, 0:3] /= model.rs
            self.df.iloc[:, 3:6] /= model.vs
            self.df.set_index([pd.Index(self.df.index.values / model.ts)], inplace=True)
            self.generate_tck()
            self.dim_status = False

        else:
            pass

        return 0

    def dim(self, model):
        """
        Dimensionalize orbit

        Parameters
        ----------
        model : rnbp class
            Physical model
        """

        if self.dim_status:
            pass
        else:
            self.df.iloc[:, 0:3] *= model.rs
            self.df.iloc[:, 3:6] *= model.vs
            self.df.set_index([pd.Index(self.df.index.values * model.ts)], inplace=True)
            self.generate_tck()
            self.dim_status = True

        return 0

    def generate_tck(self):
        position = self.df.iloc[:, 0:3].values.T
        velocity = self.df.iloc[:, 3:6].values.T
        time = self.df.index.values

        x = interpolate.splrep(time, position[0, :], s=0)
        y = interpolate.splrep(time, position[1, :], s=0)
        z = interpolate.splrep(time, position[2, :], s=0)

        vx = interpolate.splrep(time, velocity[0, :], s=0)
        vy = interpolate.splrep(time, velocity[1, :], s=0)
        vz = interpolate.splrep(time, velocity[2, :], s=0)

        self.tck = {'x': x, 'y': y, 'z': z, 'vx': vx, 'vy': vy, 'vz': vz}

        return 0

    def IC(self):
        """
        Returns initial conditions from trajectory

        Returns
        -------
        s : ndarray (6,1)
            Initial conditions
        """

        s = self.df.iloc[0].values.reshape(-1, 1)
        # if self.dim_status:
        #     s = self.df.iloc[0].values
        # else:
        #     self.dim(rnbp.CRTBP())
        #     self.dim_status = True
        #     s = self.df.iloc[0].values

        return s

    def r_lineal(self, t):
        """
        Returns position of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        r_interp : ndarray (nx3)
            Array of positions for given times
        """

        time = self.df.index.values

        x = np.interp(t, time, self.df.x.values)
        y = np.interp(t, time, self.df.y.values)
        z = np.interp(t, time, self.df.z.values)

        r_interp = np.array([x, y, z])

        return r_interp

    def v(self, t):
        """
        Returns velocity of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        v_interp : ndarray (nx3)
            Array of velocities for given times
        """

        v_interp = self.v_sp(t)

        return v_interp

    def r(self, t):
        """
        Returns position of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        r_interp : ndarray (nx3)
            Array of positions for given times
        """

        r_interp = self.r_sp(t)

        return r_interp

    def v_lineal(self, t):
        """
        Returns velocity of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        v_interp : ndarray (nx3)
            Array of velocities for given times
        """

        time = self.df.index.values

        vx = np.interp(t, time, self.df.vx.values)
        vy = np.interp(t, time, self.df.vy.values)
        vz = np.interp(t, time, self.df.vz.values)

        v_interp = np.array([vx, vy, vz])

        return v_interp

    def s(self, t):
        """
        Returns state vector of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        s_interp : ndarray (nx6)
            Array of state vectors
        """

        s_interp = np.concatenate((self.r(t), self.v(t)))

        return s_interp

    def r_sp(self, t):
        """
        Returns position of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        r_interp : ndarray (nx3)
            Array of positions for given times
        """

        x = interpolate.splev(t, self.tck['x'], der=0)
        y = interpolate.splev(t, self.tck['y'], der=0)
        z = interpolate.splev(t, self.tck['z'], der=0)

        r_interp = np.array([x, y, z])

        return r_interp

    def v_sp(self, t):
        """
        Returns velocity of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        v_interp : ndarray (nx3)
            Array of velocities for given times
        """

        vx = interpolate.splev(t, self.tck['vx'], der=0)
        vy = interpolate.splev(t, self.tck['vy'], der=0)
        vz = interpolate.splev(t, self.tck['vz'], der=0)

        v_interp = np.array([vx, vy, vz])

        return v_interp

    def s_sp(self, t):
        """
        Returns state vector of satellite for given time

        Parameters
        ----------
        t : float, 1-D array (n) or list (n)
            Times of interest

        Returns
        -------
        s_interp : ndarray (nx6)
            Array of state vectors
        """

        s_interp = np.concatenate((self.r_sp(t), self.v_sp(t)))

        return s_interp

    def mt(self):
        """
        Returns mission time

        Returns
        -------
        mission_time : float
            Total mission time (seconds)
        """

        mission_time = self.df.index.values[-1]

        return mission_time


def extract_points(ref_orbit, N_segment):
    tf = ref_orbit.mt()
    time_segment_point = np.linspace(0, tf, N_segment + 1)

    # create df with the time of each point
    point_time_ar = ref_orbit.s(time_segment_point)
    point_df = pd.DataFrame(
        columns=ref_orbit.trajectory.df.columns,
        data=point_time_ar.T,
        index=time_segment_point,
    )

    return point_df


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

    r_A = reference_trajectory[["x", "y", "z"]].values.T
    r_B = compared_trajectory[["x", "y", "z"]].values.T

    v_A = reference_trajectory[["vx", "vy", "vz"]].values.T
    v_B = compared_trajectory[["vx", "vy", "vz"]].values.T

    t0 = max(time_A[0], time_B[0])
    tf = min(time_A[-1], time_B[-1])

    time = np.linspace(t0, tf, N)

    f_r_A = interp1d(time_A, r_A, kind="cubic")
    f_r_B = interp1d(time_B, r_B, kind="cubic")

    reference_interpolated_r = f_r_A(time)
    compared_interpolated_r = f_r_B(time)

    drift_r = reference_interpolated_r - compared_interpolated_r

    drift_r_norm = np.linalg.norm(drift_r, axis=0)

    f_v_A = interp1d(time_A, v_A, kind="cubic")
    f_v_B = interp1d(time_B, v_B, kind="cubic")

    reference_interpolated_v = f_v_A(time)
    compared_interpolated_v = f_v_B(time)

    drift_v = reference_interpolated_v - compared_interpolated_v

    drift_v_norm = np.linalg.norm(drift_v, axis=0)

    return time, drift_r, drift_r_norm, drift_v, drift_v_norm
