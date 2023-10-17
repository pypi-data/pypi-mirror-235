import numpy as np
import pandas as pd
from scipy import interpolate


class BaseState:
    def __init__(self, system, libration_point, orbit_type, orbit_parameters):
        self.system = system
        self.Ln = libration_point
        self.orbit_type = orbit_type
        self.orbit_parameters = orbit_parameters


class LissajousState(BaseState):
    pass


class HaloState(BaseState):
    pass


class Orbit:
    def __init__(self, primaries, frame):
        self._primaries = primaries
        self._trajectory = trajectory()
        self._frame = frame

    @property
    def trajectory(self):

        return self._trajectory.states

    @property
    def frame(self):

        return self._frame

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
        self.df = pd.DataFrame(columns=["x", "y", "z", "vx", "vy", "vz"])
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

        self.tck = {"x": x, "y": y, "z": z, "vx": vx, "vy": vy, "vz": vz}

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

        x = interpolate.splev(t, self.tck["x"], der=0)
        y = interpolate.splev(t, self.tck["y"], der=0)
        z = interpolate.splev(t, self.tck["z"], der=0)

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

        vx = interpolate.splev(t, self.tck["vx"], der=0)
        vy = interpolate.splev(t, self.tck["vy"], der=0)
        vz = interpolate.splev(t, self.tck["vz"], der=0)

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
