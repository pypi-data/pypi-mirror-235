import numpy as np
from numpy.linalg import eig
import mubody.numeric as nm
import mubody.core.physic as phy
import mubody.constants as cte
from mubody.coordinates.frames import J2000Eq, Synodic, SynodicIdeal
from mubody.core.perturbations import SRP
from mubody.utilities.rotations import Cz

import pkg_resources
from astropy.time import Time
import spiceypy as spice
from scipy import interpolate
from scipy.integrate import solve_ivp
from scipy.optimize import newton, least_squares
import requests
from pathlib import Path
from scipy.interpolate import splev, splrep
from math import sqrt
import matplotlib.pyplot as plt
import os

"""This library contains the different physical models of the 3-body movement"""


class CRTBP:
    """
    CRTBP model class

    Attributes
    ----------
    name : str
        Name of the class
    orbit: str
        Type of orbit (Halo/Lissajous)
    primaries : list (2)
        Celestial bodies acting as primaries
    xL : float
        Parameter xL of the CRTBP model
    gamma : float
        Parameter gamma of the CRTBP model
    mu : float
        Parameter mu of the CRTBP model
    L : float
        Parameter L of the CRTBP model
    w0 : float
        Paramter w0 of the CRTBP model
    bodies : list
        All celestial bodies considered in the model
    cf : str
        Coordinate frame
    """

    def __init__(self, primaries, crtbp_parameters, orbit, perturbations=False, bodies_list=[]):
        self.name = "CRTBP"
        self.orbit = orbit
        self.primaries = primaries
        self.bodies_list = bodies_list
        self.crtbp_parameters = crtbp_parameters
        self.xL = crtbp_parameters[0]
        self.gamma = crtbp_parameters[1]
        self.mu = crtbp_parameters[2]
        self.L = crtbp_parameters[3]
        self.w0 = crtbp_parameters[4]
        self.Ln = crtbp_parameters[5]
        self.bodies = None
        self.cf = "SunSynodic"
        self.srp = SRP()
        self.perturbations = perturbations

        self.setup_models()

        if self.bodies_list[0].id == "10":
            self.omega_theta = 0
        else:
            self.omega_theta = self.ts/self.bodies_list[0].Torb()
        self.a_barycenter = self.bodies_list[0].sma/self.L
        self.phi0 = np.pi/4

    def setup_models(self):
        self.models = {'Lissajous': Lissajous(self.primaries, self.crtbp_parameters),
                       'Halo': Halo(self.primaries, self.crtbp_parameters)
                       }

    def orbit_parameters(self, parameter_type, parameter, stable, ROLE, HOP):
        if self.orbit == 'Halo':
            self.orbit_parameters = self.models[self.orbit].get_HOP(HOP)
        elif self.orbit == 'Lissajous':
            self.orbit_parameters = self.models[self.orbit].get_GOLE(parameter_type, parameter, stable, ROLE)
        else:
            raise NotImplementedError

        return self.orbit_parameters

    def F(self, t, U):
        """
        Derivates of the state vector in the CRTBP model.

        The derivatives are obtained from the equations of motion of the CRTBP
        model.

        Parameters
        ----------
        t : float
            Time
        U : ndarray
            State vector

        Returns
        -------
        Up : ndarray (6, n)
            Derivative of state vector
        """

        Up_list = phy.F(self.mu, t, U)  # Call the function "F" from the physics module
        Up_array = np.array(Up_list)

        if self.perturbations:
            a_SRP = self.srp._acceleration(t, U, self.L, self.ts, self.sun_function, self.bodies_list)
            pass
        else:
            a_SRP = np.zeros(3)

        _, n = Up_array.shape
        Up = np.array(Up_list) + np.repeat(np.concatenate([np.zeros(3), a_SRP]).reshape(-1, 1), n).reshape(6, -1)

        return Up

    def a(self, t, state):
        """
        Returns acceleration vector (dimensionless) for given time according to
        the CRTBP model.

        In CRTBP, acceleration does not depend on time, but is considered here
        as an input so it has the same interface as in other models where it
        does.

        Parameters
        ----------
        t : float/1D-array (n)
            Time of interest, dimensionless
        s : ndarray (6,n)
            State vector, dimensionless

        Returns
        -------
        acceleration : ndarray (3,n)
            acceleration vector, dimensionless
        """

        Up = self.F(t, state)

        acceleration = Up[3:6].reshape(3, -1)

        return acceleration

    def A(self, t, integrate=False):
        """
        Matrix from the matrix differential equation of the model.

        xp = Ax

        For the CRTBP A matrix does not depends explicitly on time. However, as
        the satellite moves along the orbit, its position can be determined from
        time and the A matrix computed. Position is obtained from interpolation
        of the stored trajectory.

        Parameters
        ----------
        t : float
            Time

        Returns
        -------
        A_M : ndarray (6, 6)
            A matrix
        """

        mu = self.mu

        if not integrate:
            x, y, z = self.r_sp(t)
        else:
            x, y, z = self.position_xyz
            x, y, z = float(x), float(y), float(z)

        r1 = nm.norm_sc(x + mu, y, z)
        r2 = nm.norm_sc(x + mu - 1, y, z)

        Uxx = (1 - (1 - mu)/(r1**3) - mu/(r2**3)
               + 3 * ((1 - mu) * ((x + mu)**2)/(r1**5)
               + (mu/(r2**5)) * ((x - 1 + mu)**2)))

        Uyy = (1 - (1 - mu)/(r1**3) - mu/(r2**3)
               + 3 * (y**2) * ((1 - mu)/(r1**5)
               + (mu/(r2**5))))

        Uzz = (-(1 - mu)/(r1**3) - mu/(r2**3)
               + 3 * (z**2) * ((1 - mu)/(r1**5)
               + (mu/(r2**5))))

        Uxy = 3 * y * ((1 - mu) * (x + mu)/(r1**5)+(mu/(r2**5)) * (x - 1 + mu))
        Uyx = Uxy

        Uxz = 3 * z * ((1 - mu) * (x + mu)/(r1**5) + (mu/(r2**5)) * (x - 1 + mu))
        Uzx = Uxz

        Uyz = 3 * z * y * ((1 - mu)/(r1**5) + (mu/(r2**5)))
        Uzy = Uyz

        A_U = np.array([[Uxx, Uxy, Uxz], [Uyx, Uyy, Uyz], [Uzx, Uzy, Uzz]])
        A_0 = np.zeros((3, 3))
        A_I = np.eye(3)
        A_W = np.array([[0, 2, 0], [-2, 0, 0], [0, 0, 0]])

        A_1 = np.concatenate((A_0, A_I), axis=1)
        A_2 = np.concatenate((A_U, A_W), axis=1)
        A_M = np.concatenate((A_1, A_2), axis=0)

        return A_M

    def phi_dot_vec(self, t, phi_vec, integrate=False):
        """
        Vectorized state transition matrix derivative of the CRTBP model.

        The state transition matrix derivative is computed using the current
        state transition matrix and the A matrix (from the matrix differential
        equation of the model). The kronequer product is used to transform the
        matrix equation so the state transition matrix and its derivative have
        vector shape and thus they can be feeded directly to the differential
        equation solver.

        Parameters
        ----------
        t : float
            Time
        phi_vec : ndarray (36,1)
            Vectorized state transition matrix

        Returns
        -------
        phip_vec : ndarray (36,1)
            Vectorized state transition matrix
        """

        I_matrix = np.identity(6)

        A_ext = np.kron(I_matrix, self.A(t, integrate))

        phip_vec = np.matmul(A_ext, phi_vec)

        return phip_vec

    @property
    def rs(self):
        r_star = self.models[self.orbit].rs
        return r_star

    @property
    def ts(self):
        t_star = self.models[self.orbit].ts
        return t_star

    @property
    def vs(self):
        v_star = self.models[self.orbit].vs
        return v_star

    def add_trajectory(self, time, position):
        """
        Stores reference trajectory in the class instance and adds interpolation
        parameters.

        Parameters
        ----------
        time : ndarray (n)
            Time of trajectory points
        position : ndarray (3,n)
            Position of the satellite
        """

        x = interpolate.splrep(time, position[0, :], s=0)
        y = interpolate.splrep(time, position[1, :], s=0)
        z = interpolate.splrep(time, position[2, :], s=0)

        self.tck = {'x': x, 'y': y, 'z': z}
        self.time = time
        self.position = position

        return 0

    def r(self, t):
        """
        Interpolates position linearly for a given time from the stored
        trajectory.

        Parameters
        ----------
        t : float
            Time of interest

        Returns
        -------
        r_interp : ndarray (3,1)
            Interpolated position
        """

        try:
            x = np.interp(t, self.time, self.position[0, :])
            y = np.interp(t, self.time, self.position[1, :])
            z = np.interp(t, self.time, self.position[2, :])

        except AttributeError:
            print("No trajectory stored in model.")

        r_interp = np.array([x, y, z])

        return r_interp

    def r_sp(self, t):
        """
        Interpolates position using splines for a given time from the stored
        trajectory.

        Parameters
        ----------
        t : float
            Time of interest

        Returns
        -------
        r_interp : ndarray (3,1)
            Interpolated position
        """

        try:
            x = interpolate.splev(t, self.tck['x'], der=0)
            y = interpolate.splev(t, self.tck['y'], der=0)
            z = interpolate.splev(t, self.tck['z'], der=0)

        except AttributeError:
            print("No trajectory stored in model.")

        r_interp = np.array([x, y, z])

        return r_interp

    def get_IC(self, elements):

        IC = self.models[self.orbit].get_IC(elements)

        return IC

    def VarEq(self, t, x):
        """
        Generate the coupled system of state vector phi_dot_vec

        Parameters
        ----------
        time : ndarray(n)
            Time of trajectory points
        x : ndarray(42, 1) --> state vector(6,) and STM flatten (36, )
            State vector from 0:6, and STM matrix (6:6) flatten
        """

        self.position_xyz = x[0:3]
        Phi = x[6:]
        eq2solve = []

        eq2solve[0:6] = self.F(t, x[0:6])
        eq2solve[6:] = self.phi_dot_vec(t, Phi, integrate=True)

        return eq2solve

    def manifolds(self, y0, N=50, tf=3, t_span_manifold=3, epsilon=1e-6,
                  event=True, stable=True):

        """
        This function computes the manifolds of the CRTBP
        Parameters
        ----------
        y : ndarray(n)
            It admits two options.
            -) y=ndarray(6) state vetor. Position+velocity
            -) y=ndarray(2) Az and branch of a Halo orbit
        N : number of point through which we compute the manifold to the orbit. [DEFAULT] = 50
        tf : time of simulation of the Halo orbit. Only use if y = statevector. [DEFAULT] = 3
        t_span_manifold : time of simulation of the manifold. [DEFAULT] = 3
        epsilon : perturbation to compute the manifold s = s0 +- epsilon*eigvec. [DEFAULT] = 1E-6
        event : stop the manifold when arrives to the x coordinate of the body. [DEFAULT] = True
        stable : compute the stable manifold. [DEFAULT] = True
        """
        from mubody.mission import Mission
        t0 = 0
        lp = False  # libration point or periodic orbit
        phi_0 = np.eye(6).flatten()
        mu = self.mu
        if len(y0) == 2:
            Az, branch = y0
            T_dim = self.models['Halo'].get_Halo_data([Az, branch, 0])[0][0]
            tf = self.models['Halo'].get_Halo_data([Az, branch, 0], adim=True)[0][0]
            main_data = Mission(primary_1=self.primaries[0],
                                primary_2=self.primaries[1],
                                mission_time=T_dim*24*3600,
                                lagrangian_point=self.Ln,
                                orbit="Halo",
                                HOP=[Az, branch, 0])

            main_data.OTM(N_segments=5, bar=False)
            y0 = main_data.state[:, 0].flatten()
        y_0 = np.concatenate((y0, phi_0), axis=0)
        time, sol = nm.integrator(F=self.VarEq,
                                  t0=t0,
                                  tf=tf,
                                  y0=y_0,
                                  N=N,
                                  ts=1)

        # EVENTS TO STOP MANIFOLD. MAKE FOR L2
        def events1(t, y):
            return y[0] - (1-mu)
        events1.terminal = event
        # events.direction = 1
        manifold1, manifold2 = list(), list()
        times1, times2 = list(), list()

        # The case for a libration point
        if y0[1] == 0 and y0[2] == 0:
            time = [1]
            lp = True  # libration point

        for ts in range(len(time)):
            if lp:
                state = y0
                self.position_xyz = y0[0:3]
            else:
                state = sol[0:6, ts]
                self.position_xyz = sol[0:3, ts]

            eigValues, eigVector = eig(self.A(ts, True))
            if stable:
                index = np.argmin(eigValues)
                eigVec = np.real(eigVector[:, index])
            else:
                index = np.argmax(eigValues)
                eigVec = np.real(eigVector[:, index])

            trajectory1 = state + epsilon * eigVec / np.linalg.norm(eigVec)
            trajectory2 = state - epsilon * eigVec / np.linalg.norm(eigVec)

            solucion1 = solve_ivp(
                                        fun=self.F,
                                        y0=trajectory1,
                                        t_span=[0, -t_span_manifold],
                                        t_eval=np.linspace(0, -t_span_manifold, 5000),
                                        method='DOP853',
                                        events=[events1],
                                        rtol=1e-12,
                                        atol=1e-12)
            solucion2 = solve_ivp(
                                        fun=self.F,
                                        y0=trajectory2,
                                        t_span=[0, -t_span_manifold],
                                        t_eval=np.linspace(0, -t_span_manifold, 5000),
                                        method='DOP853',
                                        events=[events1],
                                        rtol=1e-12,
                                        atol=1e-12)
            manifold1.append(solucion1.y)
            manifold2.append(solucion2.y)
            times1.append(solucion1.t)
            times2.append(solucion2.t)

        return manifold1, manifold2, times1, times2

    def propagate(self, x0, tf, N, ti=0, event=False):
        def event(t, y):
            return y[1]
        event.terminal = event
        solucion = solve_ivp(
            fun=self.F,
            y0=x0,
            t_span=[ti, tf],
            t_eval=np.linspace(ti, tf, N),
            method='DOP853',
            events=event,
            rtol=1e-12,
            atol=1e-12)

        return solucion.y, solucion.t

    def sun_function(self, t):
        """Sun position w.r.t. the barycenter of a CR3BP system

        Parameters
        ----------
        t : float
            Current time [-].
        omega_theta : float
            Angular velocity of the primaries barycenter around the Sun [-].
        a_barycenter : float
            Semi-major axis of the primaries barycenter around the Sun [-].
        inc : float
            Inclination of the primaries orbital plane regarding the ecliptic [deg].
        phi0 : float
            Initial angle between Sun-barycenter and P1P2 axes.

        Returns
        -------
        r_sun : np.ndarray
            Position of the Sun w.r.t. the barycenter, expressed in the Synodic frame [-]
        """

        phi = self.phi0 + 1. * t
        theta = self.omega_theta * t

        r0_sun = -np.array([self.a_barycenter, 0, 0])

        r_sun = np.matmul(Cz(theta).T @ Cz(phi), r0_sun)

        return r_sun


class Halo:
    def __init__(self, primaries, crtbp_parameters):
        self.name = "Halo"
        self.primaries = primaries
        self.xL = crtbp_parameters[1]  # We call it xL, but is the gamma parameter
        self.mu = crtbp_parameters[2]
        self.L = crtbp_parameters[3]
        self.w0 = crtbp_parameters[4]
        self.Ln = crtbp_parameters[5]
        self.setup_model()

    def setup_model(self):
        self.generate_system_parameters()
        self.generate_adimensionalization()
        return 0

    def generate_adimensionalization(self):
        """
        Computes the adimensionalization parameters.

        The adimensionalization parameters for distance, time, velocity and
        acceleration are computed
        """

        self.ts = 1/self.w0
        self.rs = self.L
        self.vs = self.rs/self.ts

    def generate_system_parameters(self):
        """
        Generates some parameters needed for the operations which only
        depend on the system, not the HOP
        """
        mu = self.mu
        point_number = self.Ln
        xL = self.xL

        # Generate the parameters according to Richardson 1980
        if point_number == 1:
            barycenter_distance = 1 - mu - xL

            c2 = 1/xL**3 * (mu + (1 - mu) * xL**3/(1 - xL)**3)
            c3 = 1/xL**3 * (mu - (1 - mu) * xL**4/(1 - xL)**4)
            c4 = 1/xL**3 * (mu + (1 - mu) * xL**5/(1 - xL)**5)

        elif point_number == 2:
            barycenter_distance = 1 - mu + xL

            c2 = 1/xL**3 * (mu + (1 - mu) * xL**3/(1 + xL)**3)
            c3 = 1/xL**3 * (-mu - (1 - mu) * xL**4/(1 + xL)**4)
            c4 = 1/xL**3 * (mu + (1 - mu) * xL**5/(1 + xL)**5)

        elif point_number == 3:
            barycenter_distance = -mu - xL

            c2 = 1/xL**3 * (1 - mu + mu * xL**3/(1 + xL)**3)
            c3 = 1/xL**3 * (1 - mu + mu * xL**4/(1 + xL)**4)
            c4 = 1/xL**3 * (1 - mu + mu * xL**5/(1 + xL)**5)

        else:
            raise NotImplementedError

        lamda = ((2 - c2 + np.sqrt(9 * c2**2 - 8 * c2))**(1/2))/np.sqrt(2)
        k = (lamda**2 + 1 + 2 * c2)/(2*lamda)
        delta = lamda**2 - c2

        d1 = 3 * lamda**2/k * (k * (6 * lamda**2 - 1) - 2 * lamda)
        d2 = 8 * lamda**2/k * (k * (11 * lamda**2 - 1) - 2 * lamda)

        a21 = (3 * c3 * (k**2 - 2))/(4 * (1 + 2 * c2))
        a22 = 3 * c3/(4 * (1 + 2 * c2))
        a23 = -3 * c3 * lamda * (3 * k**3 * lamda - 6 * k * (k - lamda) + 4)/(4 * k * d1)
        a24 = -3 * c3 * lamda * (2 + 3 * k * lamda)/(4 * k * d1)

        b21 = -3 * c3 * lamda * (3 * k * lamda - 4)/(2 * d1)
        b22 = 3 * c3*lamda/d1

        d21 = -c3/(2 * lamda**2)

        a31 = (-9 * lamda * (4 * c3 * (k * a23 - b21) + k * c4 * (4 + k**2))/(4 * d2)
               + (9 * lamda**2 + 1 - c2)/(2 * d2) * (3 * c3 * (2 * a23 - k * b21) + c4 * (2 + 3 * k**2)))

        a32 = (-1/d2 * (9 * lamda/4 * (4 * c3 * (k * a24 - b22) + k * c4) + 3/2 * (9 * lamda**2 + 1 - c2)
               * (c3 * (k * b22 + d21 - 2 * a24) - c4)))

        b31 = (3/(8 * d2) * (8 * lamda * (3 * c3 * (k * b21 - 2 * a23) - c4 * (2 + 3 * k**2))
               + (9 * lamda**2 + 1 + 2 * c2) * (4 * c3 * (k * a23 - b21) + k * c4 * (4 + k**2))))

        b32 = (1/d2 * (9 * lamda * (c3 * (k * b22 + d21 - 2 * a24) - c4)
               + 3/8 * (9*lamda**2 + 1 + 2 * c2) * (4 * c3 * (k * a24 - b22) + k * c4)))

        d31 = 3 * (4*c3*a24 + c4)/(64*lamda**2)

        d32 = 3 * (4 * c3 * (a23 - d21) + c4 * (4 + k**2))/(64 * lamda**2)

        a1 = -3/2 * c3 * (2 * a21 + a23 + 5 * d21) - 3/8 * c4 * (12 - k**2)
        a2 = 3/2 * c3 * (a24 - 2 * a22) + 9/8 * c4

        s1 = (1/(2 * lamda * (lamda * (1 + k**2) - 2 * k)) * (3/2 * c3 * (2 * a21 * (k**2 - 2)
              - a23 * (k**2 + 2) - 2 * k * b21) - 3/8 * c4 * (3 * k**4 - 8 * k**2 + 8)))

        s2 = (1/(2 * lamda * (lamda * (1 + k**2) - 2 * k)) * (3/2 * c3 * (2 * a22 * (k**2 - 2)
              + a24 * (k**2 + 2) + 2 * k * b22 + 5 * d21) + 3/8 * c4 * (12 - k**2)))

        l1 = a1 + 2 * lamda**2 * s1
        l2 = a2 + 2 * lamda**2 * s2

        self.system_parameters = [xL, lamda, k, delta, c2, c3, c4, s1, s2, l1, l2, a1, a2, d1,
                                  d2, a21, a22, a23, a24, a31, a32, b21, b22, b31, b32, d21, d31, d32]

        # xL-->0; lamda-->1; k-->2; delta-->3; c2-->4; c3-->5; c4-->6; s1-->7; s2-->8; l1-->9; l2-->10
        # a1-->11; a2-->12; d1-->13; d2-->14; a21-->15; a22-->16; a23-->17; a24-->18; a31-->19
        # a32-->20; b21-->21; b22-->22; b31-->23; b32-->24; d21-->25; d31-->26; d32-->27

        self.lamda = lamda
        self.barycenter_distance = barycenter_distance

        return 0

    def generate_HOP_parameters(self, HOP):
        """
        HOP: Az (km), branch (1 or 2), phi

        This function computes all the necessary parameters which depends
        on the HOP parameters
        """
        Az = HOP[0]/self.xL/self.L * 1000  # Needs to be adimensionalised
        branch = HOP[1]
        phi = HOP[2]
        if branch == "northern":
            self.delt = 1
        elif branch == "southern":
            self.delt = -1
        else:
            raise NotImplementedError

        # xL,lamda,k,delta,c2,c3,c4,s1,s2,l1,l2,a1,a2,d1,\
        # d2,a21,a22,a23,a24,a31,a32,b21,b22,b31,b32,d21,d31,d32  = self.HALO_parameters

        lamda = self.system_parameters[1]
        delta = self.system_parameters[3]
        s1 = self.system_parameters[7]
        s2 = self.system_parameters[8]
        l1 = self.system_parameters[9]
        l2 = self.system_parameters[10]

        Ax = np.sqrt((-delta - l2 * Az**2)/l1)
        omega = 1 + s1 * Ax**2 + s2 * Az**2

        self.omega = omega
        self.Ax = Ax
        self.Az = Az
        self.phi = phi

        self.T = 2 * np.pi/(lamda * omega)

        return 0

    def r_linear_dimensionless(self, HOP, time):
        self.generate_HOP_parameters(HOP)  # We call all the paremeters needed
        Ax = self.Ax
        Az = self.Az
        [xL, lamda, k, delta, c2, c3, c4, s1, s2, l1, l2, a1, a2, d1,
         d2, a21, a22, a23, a24, a31, a32, b21, b22, b31, b32, d21, d31, d32] = self.system_parameters

        t = np.array([time]).flatten()
        t = self.omega*t
        t = self.lamda*t + self.phi

        x = a21*Ax**2 + a22*Az**2 - Ax*np.cos(t) + (a23*Ax**2 - a24*Az**2)*np.cos(2*t) \
            + (a31*Ax**3 - a32*Ax*Az**2)*np.cos(3*t)

        y = k*Ax*np.sin(t) + (b21*Ax**2 - b22*Az**2)*np.sin(2*t) \
            + (b31*Ax**3 - b32*Ax*Az**2)*np.sin(3*t)

        z = self.delt * Az*np.cos(t) + self.delt*d21*Ax*Az*(np.cos(2*t) - 3) \
            + self.delt*(d32*Az*Ax**2 - d31*Az**3)*np.cos(3*t)

        # We adimensionalize with ^x=x/L;
        # REMEMBER: this formulation adimensionalization ^x=x/r1 --> R1=xL*L
        r = np.array([x, y, z]) * self.xL
        r[0] += self.barycenter_distance   # We express in the synodic frame (centered in the barycenter)

        return r

    def v_linear_dimensionless(self, HOP, time):
        self.generate_HOP_parameters(HOP)  # We call all the paremeters needed
        Ax = self.Ax
        Az = self.Az
        [xL, lamda, k, delta, c2, c3, c4, s1, s2, l1, l2, a1, a2, d1,
         d2, a21, a22, a23, a24, a31, a32, b21, b22, b31, b32, d21, d31, d32] = self.system_parameters

        t = np.array([time]).flatten()

        t = self.omega*t
        t = self.lamda*t + self.phi

        vx = self.lamda*Ax*np.sin(t) - 2*self.lamda*(a23*Ax**2 - a24*Az**2)*np.sin(2*t) \
            - 3*self.lamda*(a31*Ax**3 - a32*Ax*Az**2)*np.sin(3*t)

        vy = self.lamda*k*Ax*np.cos(t) + 2*self.lamda*(b21*Ax**2 - b22*Az**2)*np.cos(2*t) \
            + 3*self.lamda*(b31*Ax**3 - b32*Ax*Az**2)*np.cos(3*t)

        vz = -self.lamda*self.delt*Az*np.sin(t) - 2*self.lamda*self.delt*d21*Ax*Az*np.sin(2*t) \
            - 3*self.lamda*self.delt*(d32*Az*Ax**2 - d31*Az**3)*np.sin(3*t)

        # We adimensionalize with ^v=v/(L*n);
        # REMEMBER: this formulation adimensionalization ^x=x/r1 --> R1=xL*L
        v = np.array([vx, vy, vz])

        return v * self.xL * self.omega

    def r_linear(self, HOP, t):
        t = t/self.ts     # tau = t/ts
        r = self.r_linear_dimensionless(HOP, t) * self.rs
        return r

    def v_linear(self, HOP, t):
        t = t/self.ts     # tau = t/ts
        v = self.v_linear_dimensionless(HOP, t) * self.vs
        return v

    def get_HOP(self, HOP):  # HOP: Halo Orbital Parameters
        Az = float(HOP[0])
        class_ = HOP[1]   # 1: Northern Halo; 2: Southern Halo
        phase = float(HOP[2])
        HOP = [Az, class_, phase]
        return HOP

    def IC_to_class(self, IC):
        y = IC[1]
        vz = IC[5]
        if np.sign(y) != np.sign(vz):
            class_ = 1  # Class 1: Northern HALO

        if np.sign(y) == np.sign(vz):
            class_ = 2

        return class_

    def r_equations(self, x, r0, class_):
        Az, phi, t = x
        x0 = r0[0]
        y0 = r0[1]
        z0 = r0[2]

        [xL, lamda, k, delta, c2, c3, c4, s1, s2, l1, l2, a1, a2, d1,
         d2, a21, a22, a23, a24, a31, a32, b21, b22, b31, b32, d21, d31, d32] = self.system_parameters

        Ax = np.sqrt((-delta - l2 * Az**2)/l1)
        omega = 1 + s1 * Ax**2 + s2 * Az**2
        tau = omega * t
        tau = lamda * t + phi

        alpha0 = a21 * Ax**2 + a22 * Az**2
        alpha1 = -Ax
        alpha2 = a23 * Ax**2 - a24 * Az**2
        alpha3 = a31 * Ax**3 - a32 * Ax * Az**2

        beta0 = 0
        beta1 = k * Ax
        beta2 = b21 * Ax**2 - b22 * Az**2
        beta3 = b31 * Ax**3 - b32 * Ax * Az**2

        gamma0 = 0
        gamma1 = Az
        gamma2 = d21 * Ax * Az
        gamma3 = d32 * Az * Ax**2 - d31 * Az**3

        eq_x = (alpha0 + alpha1 * np.cos(tau)
                + alpha2 * np.cos(2 * tau)
                + alpha3 * np.cos(3 * tau)
                - (x0 - self.barycenter_distance)/self.xL)

        eq_y = (beta0 + beta1 * np.sin(tau)
                + beta2 * np.sin(2 * tau)
                + beta3 * np.sin(3 * tau)
                - y0/self.xL)

        if class_ == 1:
            eq_z = (gamma0 + gamma1 * np.cos(tau)
                    + gamma2 * (np.cos(2 * tau) - 3)
                    + gamma3 * np.cos(3 * tau)
                    - z0/self.xL)

        if class_ == 2:
            eq_z = (-gamma0 - gamma1*np.cos(tau)
                    - gamma2 * (np.cos(2 * tau) - 3)
                    - gamma3 * np.cos(3 * tau)
                    - z0/self.xL)

        return np.array([eq_x, eq_y, eq_z])

    def v_equations(self, x, v0, class_, tol=1e-4):
        Az, phi, t = x

        [xL, lamda, k, delta, c2, c3, c4, s1, s2, l1, l2, a1, a2, d1,
         d2, a21, a22, a23, a24, a31, a32, b21, b22, b31, b32, d21, d31, d32] = self.system_parameters

        Ax = np.sqrt((-delta - l2 * Az**2)/l1)
        omega = 1 + s1 * Ax**2 + s2 * Az**2
        tau = omega * t
        tau = lamda * t + phi

        v0 = v0/xL/lamda/omega
        vx0 = v0[0]
        vy0 = v0[1]
        vz0 = v0[2]

        alpha0 = 0
        alpha1 = Ax
        alpha2 = - 2 * (a23 * Ax**2 - a24 * Az**2)
        alpha3 = - 3 * (a31 * Ax**3 - a32 * Ax * Az**2)

        beta0 = 0
        beta1 = k * Ax
        beta2 = 2 * (b21 * Ax**2 - b22 * Az**2)
        beta3 = 3 * (b31 * Ax**3 - b32 * Ax * Az**2)

        gamma0 = 0
        gamma1 = -Az
        gamma2 = -2 * d21 * Ax * Az
        gamma3 = -3 * (d32 * Az * Ax**2 - d31 * Az**3)

        eq_vx = alpha0 + alpha1 * np.sin(tau) + alpha2 * np.sin(2 * tau) + alpha3 * np.sin(3 * tau) - vx0
        eq_vy = beta0 + beta1 * np.cos(tau) + beta2 * np.cos(2 * tau) + beta3 * np.cos(3 * tau) - vy0

        if class_ == 1:
            eq_vz = gamma0 + gamma1*np.sin(tau) + gamma2*np.sin(2*tau) + gamma3*np.sin(3*tau) - vz0
        if class_ == 2:
            eq_vz = -gamma0 - gamma1*np.sin(tau) - gamma2*np.sin(2*tau) - gamma3*np.sin(3*tau) - vz0

        state = False

        if eq_vx < tol:
            state = True
        else:
            print("HALO orbit not possible: vx fails -->", eq_vx)

        if eq_vy < tol:
            state = True
        else:
            print("HALO orbit not possible: vy fails -->", eq_vy)

        if eq_vz < tol:
            state = True
        else:
            print("HALO orbit not possible: vz fails -->",  eq_vz)

        return state

    def IC_to_Halo(self, IC, val0=[5000, 0, 0]):
        """
        This function solve the system of equations for the position
        and then check that also complies with the velocity
        """
        r0 = IC[0:3]
        v0 = IC[3:6]

        class_ = self.IC_to_class(IC)  # We determine the class I or II

        Az0 = val0[0]/self.xL/self.L * 1000
        phi0 = val0[1]
        t0 = val0[2]
        val0 = np.array([Az0, phi0, t0])

        sol = least_squares(fun=self.r_equations,
                            x0=val0,
                            bounds=((0, 0, 0), (np.inf, 2*np.pi, np.inf)),
                            xtol=1e-12,
                            args=(r0, class_))

        Az = sol.x[0] * self.xL * self.L/1000
        phi = sol.x[1]

        self.v_equations(sol.x, v0, class_)
        return [Az, class_, phi]

    def get_Halo_data(self, HOP, coords=False, verbose=False, adim=False):
        data = []
        self.generate_HOP_parameters(HOP)
        if not adim:
            T = self.T * self.ts/3600/24.0  # days
            Az = self.Az * self.xL * self.L/1000   # km
            Ax = self.Ax * self.xL * self.L/1000   # km
        else:
            T = self.T
            Az = self.Az
            Ax = self.Ax

        if coords:
            Ln_coords = self.barycenter_distance
            P1_coords = -self.mu
            P2_coords = 1-self.mu
            data.extend([T, Az, Ax, Ln_coords, P1_coords, P2_coords])
        else:
            data.append([T, Az, Ax])

        if verbose:
            print("Az (km) :", Az)
            print("Ax (km) :", Ax)
            print("T (days) :", T)

        return data

    def get_IC(self, HOP):
        """
        Generates IC (state vecotr) from ROLE. All dimensional.

        Parameters
        ----------
        HOP : list (4)
            Halo Osculating Elements (Ax, Az, phi_xy, phi_z)
            (m, degrees)

        Returns
        -------
        IC : ndarray (6,1)
            Initial conditions, dimensional (m, m/s)
        """

        r = self.r_linear(HOP, 0)
        v = self.v_linear(HOP, 0)
        IC = np.concatenate((r, v), axis=0)

        return IC


class Lissajous:
    """
    Lissajous model class

    Attributes
    ----------
    name : str
        Name of the model
    primaries : list (2)
        Celestial bodies acting as primaries
    xL : float
        Parameter xL of the CRTBP model
    mu : float
        Parameter mu of the CRTBP model
    L : float
        Parameter L of the CRTBP model
    w0 : float
        Paramter w0 of the CRTBP model
    bodies : list
        All celestial bodies considered in the model
    cf : str
        Coordinate frame
    """

    def __init__(self, primaries, crtbp_parameters):
        """
        Constructor

        Parameters
        ----------
        primaries : list (2)
            Celestial bodies acting as primaries
        crtbp_parameters : list (4)
            Parameters of CRTBP model
        """

        self.name = "Lissajous"
        self.primaries = primaries
        self.xL = crtbp_parameters[0]
        self.mu = crtbp_parameters[2]
        self.L = crtbp_parameters[3]
        self.w0 = crtbp_parameters[4]
        self.Ln = crtbp_parameters[5]
        self.setup_model()
        self.bodies = None
        self.cf = "SunSynodic"

    def setup_model(self):
        """
        Generates model parameters associated to the primaries selected.

        This method generates the parameters of the linearized model and the
        adimensionalization factors.
        """

        self.generate_lineal_parameters()
        self.generate_adimensionalization()

        return 0

    def generate_lineal_parameters(self):
        """
        Compute the parameters of the linearized model.

        M matrix relates linearly parameters A1, A2, A3 and A4 from GOLE with
        the IC (x0, y0, xp0 and yp0).
        """

        xL = self.xL
        mu = self.mu

        K = mu/abs(xL - 1 + mu)**3 + (1 - mu)/abs(xL + mu)**3

        omega_xy = ((-K + 2 + np.sqrt(9 * K**2 - 8 * K))**(1/2))/np.sqrt(2)
        lamda_xy = ((K - 2 + np.sqrt(9 * K**2 - 8 * K))**(1/2))/np.sqrt(2)
        c1 = (lamda_xy**2 - 1 - 2 * K)/(2 * lamda_xy)
        c2 = (omega_xy**2 + 1 + 2 * K)/(2 * omega_xy)
        omega_z = np.sqrt(K)

        d1 = c1 * lamda_xy + c2 * omega_xy
        d2 = c1 * omega_xy - c2 * lamda_xy

        M = np.array([[c2 * omega_xy/(2 * d1),  omega_xy/(2 * d2), -c2/(2 * d2),  1/(2 * d1)],
                      [c2 * omega_xy/(2 * d1), -omega_xy/(2 * d2),  c2/(2 * d2),  1/(2 * d1)],
                      [c1 * lamda_xy/d1,                        0,            0,       -1/d1],
                      [0,                            -lamda_xy/d2,        c1/d2,           0]])

        self.K = K

        self.omega_xy = omega_xy
        self.omega_z = omega_z

        self.lamda_xy = lamda_xy

        self.c1 = c1
        self.c2 = c2

        self.d1 = d1
        self.d2 = d2

        self.M = M

        return 0

    def generate_adimensionalization(self):
        """
        Computes the adimensionalization parameters.

        The adimensionalization parameters for distance, time, velocity and
        acceleration are computed

        time t=nt*; t*->> dimensionless time; n->> angular velocity
        """

        self.ts = 1/self.w0
        self.rs = self.L
        self.vs = self.rs/self.ts
        self.acs = self.rs/self.ts**2

        return 0

    def r_linear_dimensionless(self, GOLE, t):
        """
        Returns position vector (dimensionless) for given time using
        the general linear solution of CRTBP model.

        Coordinate system -> P1-IdealSynodic

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensionless

        Returns
        -------
        r : ndarray (3,n)
            Position vector, dimensionless
        """

        t = np.array([t]).flatten()

        A = GOLE[0:4]
        Az = GOLE[4]
        phi_z = GOLE[5]

        x = (A[0] * np.exp(self.lamda_xy * t)
             + A[1] * np.exp(-self.lamda_xy * t)
             + A[2] * np.cos(self.omega_xy * t)
             + A[3] * np.sin(self.omega_xy * t)
             + self.xL + self.mu)

        y = (A[0] * self.c1 * np.exp(self.lamda_xy * t)
             - A[1] * self.c1 * np.exp(-self.lamda_xy * t)
             + A[3] * self.c2 * np.cos(self.omega_xy * t)
             - A[2] * self.c2 * np.sin(self.omega_xy * t))

        z = Az * np.cos(self.omega_z * t + phi_z)

        r = np.array([x, y, z])

        return r

    def v_linear_dimensionless(self, GOLE, t):
        """
        Returns velocity vector (dimensionless) for given time using
        the general linear solution of CRTBP model.

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensionless

        Returns
        -------
        v : ndarray (3,n)
            Velocity vector, dimensionless
        """

        t = np.array([t]).flatten()

        A = GOLE[0:4]
        Az = GOLE[4]
        phi_z = GOLE[5]

        vx = (A[0] * self.lamda_xy * np.exp(self.lamda_xy * t)
              - A[1] * self.lamda_xy * np.exp(-self.lamda_xy * t)
              - A[2] * self.omega_xy * np.sin(self.omega_xy * t)
              + A[3] * self.omega_xy * np.cos(self.omega_xy * t))

        vy = (A[0] * self.c1 * self.lamda_xy * np.exp(self.lamda_xy * t)
              + A[1] * self.c1 * self.lamda_xy * np.exp(-self.lamda_xy * t)
              - A[3] * self.c2 * self.omega_xy * np.sin(self.omega_xy * t)
              - A[2] * self.c2 * self.omega_xy * np.cos(self.omega_xy * t))

        vz = - Az * self.omega_z * np.sin(self.omega_z * t + phi_z)

        v = np.array([vx, vy, vz])

        return v

    def s_linear_dimensionless(self, GOLE, t):
        """
        Returns state vector (dimensionless) for given time using
        the general linear solution of CRTBP model.

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensionless

        Returns
        -------
        s : ndarray (6,n)
            State vector, dimensionless
        """

        s = np.concatenate(self.r_linear_dimensionless(GOLE, t), self.v_linear_dimensionless(GOLE, t), axis=0)

        return s

    def r_linear(self, GOLE, t):
        """
        Returns position vector (dimensionless) for given time using
        the general linear solution of CRTBP model.

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensionless

        Returns
        -------
        r : ndarray (3,n)
            Position vector, dimensionless
        """

        t = t/self.ts

        r = self.r_linear_dimensionless(GOLE, t) * self.rs

        return r

    def v_linear(self, GOLE, t):
        """
        Returns velocity vector (dimensionless) for given time using
        the general linear solution of CRTBP model.

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensionless

        Returns
        -------
        v : ndarray (3,n)
            Velocity vector, dimensionless
        """

        t = t/self.ts

        v = self.v_linear_dimensionless(GOLE, t) * self.vs

        return v

    def s_linear(self, GOLE, t):
        """
        Returns state vector (dimensional) for given time using
        the general linear solution of CRTBP model.

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        t : float/1D-array (n)
            Time of interest, dimensional (s)

        Returns
        -------
        s : ndarray (6,n)
            State vector, dimensional (m, m/s)
        """

        s = np.concatenate(self.r_linear(GOLE, t), self.v_linear(GOLE, t), axis=0)

        return s

    def ROLE_to_GOLE(self, ROLE):
        """
        Transforms Reduced Osculating Lissajous Elements (ROLE) to General
        Osculating Lissajous Elements (GOLE).

        ROLE parameters defined a lissajous orbit from the stable solution of
        the linearised CRTBP model. ROLE parameters can be expanded to GOLE by
        assuming A1 and A2 are equal to 0. Both ROLE and GOLE are dimensionless.

        Parameters
        ----------
        ROLE : list (6)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensionless (CRTBP units, radians)

        Returns
        -------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless (CRTBP units, radians)
        """

        Ax, Az, phi_xy, phi_z = ROLE

        GOLE = [0, 0, Ax * np.cos(phi_xy), -Ax * np.sin(phi_xy), Az, phi_z]

        return GOLE

    def IC_to_GOLE(self, IC):
        """
        Transforms initial conditions (state vector) to General Osculating
        Lissajous Elements (GOLE).

        IC must be in SunSynodic frame and in dimensionless units. GOLE are
        dimensionless.

        Parameters
        ----------
        IC : ndarray (6,1)
            State vector corresponding to the initial conditions, dimensionless

        Returns
        -------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless
        """

        x, y, z = IC[0:3]
        vx, vy, vz = IC[3:6]

        x -= self.xL + self.mu

        IC_red = np.array([x, y, vx, vy])

        A = np.matmul(self.M, IC_red)

        phi_z = np.arctan2(-vz/self.omega_z, z)

        Az = (z/np.cos(phi_z))

        GOLE = np.concatenate((A, np.array([Az, phi_z])))

        return GOLE

    def IC_to_ROLE(self, IC):
        """
        Transforms initial conditions (state vector) to Reduced Osculating
        Lissajous Elements (ROLE).

        IC must be in SunSynodic frame and in dimensionless units. ROLE are
        dimensionless. Stable solution from the linearised CRTBP model is used.

        Parameters
        ----------
        IC : ndarray (6,1)
            State vector corresponding to the initial conditions, dimensionless
            (CRTBP units)

        Returns
        -------
        ROLE : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensionless (CRTBP units)
        """

        x, y, z = IC[0:3]
        vx, vy, vz = IC[3:6]

        x -= self.xL + self.mu

        r = np.array([x, y])

        M = self.M

        B = M[0:2, 0:2]
        C = M[0:2, 2:4]

        v = - np.linalg.inv(C) @ B @ r

        vx = v[0]
        vy = v[1]

        IC_red = np.array([x, y, vx, vy])

        A = np.matmul(M, IC_red)

        phi_xy = np.arctan2(-y/self.c2, x)
        phi_z = np.arctan2(-vz/self.omega_z, z)

        Ax = np.sqrt(A[2]**2 + A[3]**2)
        Az = (z/np.cos(phi_z))

        ROLE = np.array([Ax, Az, phi_xy, phi_z])

        return ROLE

    def ROLE_to_IC(self, ROLE):
        """
        Transforms Reduced Osculating Lissajous Elements (ROLE) to initial
        conditions (state vector).

        ROLE must be dimensionless and the IC will be in SunSynodic frame and in
        dimensionless units.

        Parameters
        ----------
        ROLE : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensionless

        Returns
        -------
        IC : ndarray (6,1)
            State vector corresponding to the initial conditions, dimensionless
            (CRTBP units)
        """

        Ax, Az, phi_xy, phi_z = ROLE

        # Amplitudes A1 and A2 are nulled, A3 and A4 are retrieved from ROLE
        A = np.array([0, 0, Ax * np.cos(phi_xy), - Ax * np.sin(phi_xy)])

        # x, y, vx and vy are determined from A1, A2, A3 and A4
        IC_red = np.linalg.inv(self.M) @ A

        x = IC_red[0] + self.xL + self.mu
        y = IC_red[1]
        z = Az * np.cos(phi_z)

        vx = IC_red[2]
        vy = IC_red[3]
        vz = - Az * self.omega_z * np.sin(phi_z)

        IC = np.array([x, y, z, vx, vy, vz]).reshape(-1, 1)

        return IC

    def GOLE_to_OLE(self, GOLE):
        """
        Transforms General Osculating Lissajous Elements (GOLE) to Osculating
        Lissajous Elements (OLE).

        OLE is an alternative version of GOLE, with Ax and phi_xy substituting
        A3 and A4 elements. Both OLE and GOLE are dimensionless although this
        function will work with dimensional units.

        #a*cos(x)+b*sin(x) = A*cos(x-D)
        #A = sqrt(a**2+b**2)
        #D = arctan(b/a) = atan2(b, a)
        #OLE = [A1 A2 Ax Az phi_xy phi_z]

        Parameters
        ----------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless (CRTBP untis)

        Returns
        -------
        OLE : list (6)
            Osculating lissajous elements (A1, A2, Ax, Az, phi_xy, phi_z),
            dimensionless
        """

        A1, A2, A3, A4, Az, phi_z = GOLE

        phi_xy = - np.arctan2(A4, A3)

        Ax = np.sqrt(A3**2 + A4**2)

        OLE = np.array([A1, A2, Ax, Az, phi_xy, phi_z])

        return OLE

    def remove_IC_dimensions(self, IC):
        """
        Transforms inital conditions (state vector) from dimensional units
        (m, m/s) to dimensionless units.

        Parameters
        ----------
        IC : ndarray (6,1)
            State vector corresponding to the initial conditions, (m, m/s)

        Returns
        -------
        IC_dimensionless : ndarray (6,1)
            State vector corresponding to the initial conditions, dimensionless
            (CRTBP units)
        """

        r = IC[0:3]/self.rs
        v = IC[3:6]/self.vs
        IC_dimensionless = np.concatenate((r, v), axis=0)

        return IC_dimensionless

    def add_IC_dimensions(self, IC_dimensionless):
        """
        Transforms inital conditions (state vector) from dimensionless units to
        dimensional units (m, m/s).

        Parameters
        ----------
        IC_dimensionless : ndarray (6,1)
            State vector corresponding to the initial conditions, dimensionless
            (CRTBP units)

        Returns
        -------
        IC : ndarray (6,1)
            State vector corresponding to the initial conditions, (m, m/s)
        """

        r = IC_dimensionless[0:3] * self.rs
        v = IC_dimensionless[3:6] * self.vs
        IC = np.concatenate((r, v), axis=0)

        return IC

    def remove_ROLE_dimensions(self, ROLE):
        """
        Transforms Reduced Osculating Lissajous Elements (ROLE) from dimensional
        units (m) to dimensionless units. It also changes ROLE parameters from
        degrees to radians.

        Parameters
        ----------
        ROLE : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensional (m, degrees)

        Returns
        -------
        ROLE_dimensionless : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensionless (CRTBP units, radians)
        """

        Ax, Az = ROLE[0:2]/self.rs
        phi_xy, phi_z = np.pi * ROLE[2:4]/180

        ROLE_dimensionless = np.array([Ax, Az, phi_xy, phi_z])

        return ROLE_dimensionless

    def add_ROLE_dimensions(self, ROLE_dimensionless):
        """
        Transforms Reduced Osculating Lissajous Elements (ROLE) from
        dimensionaless units (m) to dimensional units. It also changes ROLE
        parameters from radians to degrees.

        Parameters
        ----------
        ROLE_dimensionless : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensionless (CRTBP units, radians)

        Returns
        -------
        ROLE : list (4)
            Reduced osculating lissajous elements (Ax, Az, phi_xy, phi_z),
            dimensional (m, degrees)
        """

        Ax, Az = ROLE_dimensionless[0:2] * self.rs
        phi_xy, phi_z = 180 * ROLE_dimensionless[2:4]/np.pi

        ROLE = np.array([Ax, Az, phi_xy, phi_z])

        return ROLE

    def get_GOLE(self, parameter_type, parameter, stable, default_ROLE):
        """
        Generates GOLE parameters. Input is dimensional and output
        dimensionless.

        This method generates GOLE parameters according to the type of input
        and the stability option. First parameters are nondimensionalized and
        then converted to GOLE.

        Parameters
        ----------
        parameter_type : string
            Initial parameter set type (IC/ROLE)
        parameter : 1-D array
            Initial parameter set (IC/ROLE, m, m/s, degrees)
        stable : bool
            Boolean to choose between general and stable solution
        default_ROLE : list (4)
            Default Reduced osculating lissajous elements (Ax, Az, phi_xy,
            phi_z) (m, degrees)

        Returns
        -------
        GOLE : list (6)
            General osculating lissajous elements (A1, A2, A3, A4, Az, phi_z),
            dimensionless (CRTPB units, radians)
        """

        if parameter_type == "IC":
            IC_dimensionless = self.remove_IC_dimensions(parameter)

            if stable:
                ROLE_dimensionless = self.IC_to_ROLE(IC_dimensionless)
                GOLE = self.ROLE_to_GOLE(ROLE_dimensionless)

            else:
                GOLE = self.IC_to_GOLE(IC_dimensionless)

        elif parameter_type == "ROLE":
            ROLE_dimensionless = self.remove_ROLE_dimensions(parameter)
            GOLE = self.ROLE_to_GOLE(ROLE_dimensionless)

        elif parameter_type is None:
            default_ROLE_dimensionless = self.remove_ROLE_dimensions(default_ROLE)
            GOLE = self.ROLE_to_GOLE(default_ROLE_dimensionless)

        return GOLE

    def get_IC(self, ROLE):
        """
        Generates IC (state vecotr) from ROLE. All dimensional.

        Parameters
        ----------
        ROLE : list (4)
            Reduced Osculating Lissajous Elements (Ax, Az, phi_xy, phi_z)
            (m, degrees)

        Returns
        -------
        IC : ndarray (6,1)
            Initial conditions, dimensional (m, m/s)
        """

        ROLE_dimensionless = self.remove_ROLE_dimensions(ROLE)
        IC_dimensionless = self.ROLE_to_IC(ROLE_dimensionless)
        IC = self.add_IC_dimensions(IC_dimensionless)

        return IC


class FETBP:
    def __init__(self, primaries, date, gravity_bodies_dict):
        self.name = "FETBP"
        self.primaries = primaries
        self.date = date
        self.gravity_bodies_dict = gravity_bodies_dict
        self.generate_adimensionalization()

    def generate_adimensionalization(self):
        """Create adimensionalization parameters"""

        self.ts = 1
        self.rs = 1
        self.vs = 1

    def F(self, t, U):
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

        if np.isscalar(t) is not True:
            raise NameError("Scalar error")

        v_sat = U[3:6, :]

        a_sat = self.a(t, U)

        Up = np.concatenate((v_sat, a_sat), axis=0)

        return Up

    def A(self, t):
        '''
        Formación de la matriz de transformación (A).

        r_sat_p, r_sat_per: radio vectorer del satélite
                            respecto a los cuerpos primario y perturbador
        G: Constante de gravitación universal
        M_p, M_per: masas de los cuerpos primario y perturbador
        '''

        r_sat = self.r(t).reshape(-1, 1)

        M = np.zeros((6, 6))

        for body in self.gravity_bodies_dict.values():

            r_body = body.r([t])
            r_body_sat = r_sat - r_body

            M += phy.gravity_jacobian(body.mass, r_body_sat)

        M[0, 3] = 1
        M[1, 4] = 1
        M[2, 5] = 1

        return M

    def phi_dot_vec(self, t, phi_vec):
        """AXB=C
            A = A
            X = phi
            B = I
            C = phi_d
            vec(c) = (B.T kron A) @ vec(X)
            """
        I_matrix = np.identity(6)

        B = self.A(t)

        A_ext = np.kron(I_matrix, B)

        phip_vec = np.matmul(A_ext, phi_vec)

        return phip_vec

    def a(self, t, U):
        """Returns acceleration in FETBP model"""

        r_sat = U[0:3, :]
        a_sat = np.zeros_like(r_sat)

        for body_name, body in self.gravity_bodies_dict.items():

            r_body = body.r(np.array([t]).flatten())
            r_body_sat = r_sat - r_body

            a_direct = phy.gravity_law(body.mass, r_body_sat)

            if body_name == 'Sun':
                a_indirect = np.zeros_like(a_direct)
            else:
                a_indirect = phy.gravity_law(body.mass, r_body)

            a_sat += a_direct + a_indirect

        return a_sat

    def add_trajectory(self, time, position):

        x = interpolate.splrep(time, position[0, :], s=0)
        y = interpolate.splrep(time, position[1, :], s=0)
        z = interpolate.splrep(time, position[2, :], s=0)

        self.tck = {'x': x, 'y': y, 'z': z}
        self.time = time
        self.position = position

        return 0

    def r(self, t):

        x = np.interp(t, self.time, self.position[0, :])
        y = np.interp(t, self.time, self.position[1, :])
        z = np.interp(t, self.time, self.position[2, :])

        r_interp = np.array([x, y, z])

        return r_interp

    def r_sp(self, t):
        x = interpolate.splev(t, self.tck['x'], der=0)
        y = interpolate.splev(t, self.tck['y'], der=0)
        z = interpolate.splev(t, self.tck['z'], der=0)

        r_interp = np.array([x, y, z])

        return r_interp


class dynamical_system:

    def __init__(self, date, primary_1, primary_2, lagrange_point, orbit, perturbations, mission_time, SRP_flag):
        self.date = Time(date, format='iso', scale='utc')
        self.bodies = [primary_1] + [primary_2] + perturbations
        self.orbit = orbit
        self.eph_class = Ephemeris(self.date, cte.SolarSystemBodies_list, mission_time, 3600)
        self.SRP_flag = SRP_flag
        self.setup_solar_system(lagrange_point)
        self.setup_primaries_system(primary_1, primary_2, lagrange_point)
        self.setup_models()

    def setup_models(self):
        self.models = {'CRTBP': CRTBP(self.primaries,
                                      self.crtbp_parameters,
                                      self.orbit,
                                      self.SRP_flag,
                                      [self.p1, self.p2]),
                       'FETBP': FETBP(self.primaries, self.date,  self.gravity_bodies),
                       }

    def setup_solar_system(self, lagrange_point):
        """
        Setups the dynamic system class

        Parameters
        ----------
        bodies_list : list
            List of celestial bodies to populate the class
        """

        barycenter_list = []

        gravity_bodies_list = []
        self.gravity_bodies = {}

        for idx, body in enumerate(self.bodies):
            if '-' in body:
                barycenter_list.append(body.split('-'))
                self.bodies[idx] += "-barycenter"
                gravity_bodies_list = gravity_bodies_list + body.split('-')
            else:
                gravity_bodies_list.append(body)

        self.barycenter_list = barycenter_list
        self.ss = solar_system(self.eph_class)

        for body in gravity_bodies_list:
            self.gravity_bodies[body] = self.ss.bodies_dict[body]

        self.ss.add_virtual_points(barycenter_list=barycenter_list)

        libration_point_list = [self.bodies[0:2] + [lagrange_point]]

        self.ss.add_virtual_points(libration_point_list=libration_point_list)

        return 0

    def setup_primaries_system(self, primary_1, primary_2, lagrange_point):
        """TBD"""
        if '-' in primary_1:
            primary_1 += "-barycenter"
        if '-' in primary_2:
            primary_2 += "-barycenter"

        lp_name = primary_1 + "/" + primary_2 + "/" + "L" + str(lagrange_point)

        self.p1 = self.ss.bodies_dict[primary_1]
        self.p2 = self.ss.bodies_dict[primary_2]
        self.Ln = lagrange_point
        self.w0 = np.sqrt(cte.G * self.p1.mass/self.p2.sma**3)
        self.L = self.p2.sma
        self.m_p1 = self.p1.mass
        self.m_p2 = self.p2.mass
        self.mu = self.p2.mass/(self.p2.mass + self.p1.mass)
        self.a = self.p2.sma
        self.primaries = (primary_1, primary_2)
        self.Lp = self.ss.libration_points[lp_name]
        self.xL, self.yL = self.Lp.location_CoM()
        self.gamma, self.gammay = self.Lp.location_primary()
        self.crtbp_parameters = [self.xL, self.gamma, self.mu, self.a, self.w0, self.Ln]

        return 0

    def setup_coordinate_frames(self):
        self.coordinate_frames = {'Sun-J2000Eq': J2000Eq(self.ss.bodies_dict['Sun']),
                                  'P1-Synodic': Synodic(self.p1, self.p1, self.p2, self),
                                  'Ln-Synodic': Synodic(self.Lp, self.p1, self.p2, self),
                                  'Ln-IdealSynodic': SynodicIdeal(self.Lp, self.p1, self.p2, self),
                                  'P1-IdealSynodic': SynodicIdeal(self.p1, self.p1, self.p2, self)
                                  }

        return 0

    def libration_point_location(self, point_number):
        """
        Returns adimensional position of colinear libration points

        Parameters
        ----------
        point_number : integer
            Id of lagrange point

        Returns
        -------
        xL : float
            Position of libration point in synodic frame

        """

        mu = self.mu

        p5 = 1

        if point_number == 1:
            p4 = 4 * mu - 2
            p3 = (1 - mu)**2 - 4 * mu * (1 - mu) + mu**2
            p2 = 2 * mu * (1 - mu) * (1 - 2 * mu) - 1 + 2 * mu
            p1 = mu**2 * (1 - mu)**2 + 2 * (mu**2 + (1 - mu)**2)
            p0 = -(1 - mu)**3 + mu**3

        elif point_number == 2:
            p4 = 2 * (2*mu - 1)
            p3 = (1 - mu)**2 - 4 * mu * (1 - mu) + mu**2
            p2 = 2 * mu * (1 - mu) * (1 - 2 * mu) - 1
            p1 = mu**2 * (1 - mu)**2 + 2 * (-mu**2 + (1 - mu)**2)
            p0 = -(1 - mu)**3 - mu**3

        elif point_number == 3:
            p4 = 4 * mu - 2
            p3 = 6 * mu**2 - 6 * mu + 1
            p2 = 4 * mu**3 - 6 * mu**2 + 2 * mu + 1
            p1 = mu**4 - 2 * mu**3 + mu**2 + 4 * mu - 2
            p0 = 3 * mu**2 - 3 * mu + 1

        else:
            raise NotImplementedError

        p = np.array([p5, p4, p3, p2, p1, p0])
        x = np.roots(p)

        xL = x[np.abs(x.imag) < 1e-6].real[0]

        return xL

    def libration_point_location_Halo(self, point_number):
        """
        Returns adimensional position of colinear libration points to the nearest primary

        Reference:
        V. G. Szebehely, Theory of orbits, the restricted problem of three bodies. Chapter 4

        Parameters
        ----------
        point_number : integer
            Id of lagrange point

        Returns
        -------
        gamma : float
            Distance of the libration point to the nearest mass (adimensional)
        """
        mu = self.mu

        p5 = 1

        if point_number == 1:
            p4 = - (3 - mu)
            p3 = 3 - 2*mu
            p2 = - mu
            p1 = 2*mu
            p0 = -mu

            x0 = (mu/(3*(1-mu)))**(1./3)

        elif point_number == 2:
            p4 = 3 - mu
            p3 = 3 - 2*mu
            p2 = -mu
            p1 = -2*mu
            p0 = -mu

            x0 = (mu/(3*(1-mu)))**(1./3)

        elif point_number == 3:
            p4 = 2 + mu
            p3 = 1 + 2*mu
            p2 = - (1 - mu)
            p1 = - 2*(1 - mu)
            p0 = - (1 - mu)

            x0 = 1-7/12.0*mu

        else:
            raise NotImplementedError

        def f(x, p0, p1, p2, p3, p4, p5):
            return x**5 + p4*x**4 + p3*x**3 + p2*x**2 + p1*x + p0

        gamma = newton(f, x0=x0,  args=(p0, p1, p2, p3, p4, p5,), maxiter=10000)

        return gamma


class solar_system():
    """
    This class gathers all the bodies of the solar system and the virtual
    points defined by the user.

    Here the instances of the celestial body class for each body of the solar
    system are created.

    Attributes
    ----------
    star : celestial body class
        Name of the mission.
    planets : dict
        Dictionary of planets celestial body instances
    moons : dict
        Dictionary of moons celestial body instances
    bodies_dict : dict
        Dictionary with all the solar system bodies
    Sun/Planet/Moon : celestial body class
        Celestial body instances of the Sun and the solar system planets and
        moons can be accessed directed as attributes.
    barycenters : dict
        Dictionary of the barycenter instances
    libration_point : dict
        Dictionary of the libration point instances
    """

    def __init__(self, ephemeris):
        """
        Constructor

        Parameters
        ----------
        ephemeris : Ephemeris class
            Reference to ephemeris instance from DS
        barycenter_list : list
            List of barycenters to be created (Body1-Body2-...-Bodyn-barycenter)
        libration_point_list : list
            List of libration points to be created (...)
        """

        self.setup_solar_system(ephemeris)

    def setup_solar_system(self, ephemeris):
        """
        Creates the celestial body instances of all the Solar System bodies.

        Parameters
        ----------
        ephemeris : Ephemeris class
            Reference to ephemeris instance from DS
        """

        # add the sun
        self.star = celestial_body(cte.sun_dict, ephemeris)

        planets_dict = {}
        all_moons_dict = {}

        for planet_name, planet in cte.SolarSystemPlanets_dict.items():

            # add moons to each planet
            if planet['moons'] is None:
                moons_dict = None

            else:
                moons_dict = {}

                for moon in planet['moons']:
                    moon_instance = celestial_body(cte.SolarSystemMoons_dict[moon], ephemeris)

                    # dict of moons for the planets
                    moons_dict[moon] = moon_instance
                    all_moons_dict[moon] = moon_instance

                    # add moons individually to ss top level
                    setattr(self, moon_instance.name, moon_instance)

            planet_instance = celestial_body(planet, ephemeris)

            # dict of planets for the star
            planets_dict[planet_name] = planet_instance

            # add moons to each planet as a dict
            setattr(planet_instance, 'moons', moons_dict)

            # add planets to ss top level
            setattr(self, planet_name, planet_instance)

        # add planets to the ss as a dict
        setattr(self, 'planets', planets_dict)

        # add all moons to the ss as dict
        setattr(self, 'moons', all_moons_dict)

        # add all bodies
        self.bodies_dict = {"Sun": self.star}
        self.bodies_dict.update(self.planets)
        self.bodies_dict.update(self.moons)

        return 0

    def add_virtual_points(self, barycenter_list=None, libration_point_list=None):
        """
        Creates the barycenters and libration points defined by the user.

        Parameters
        ----------
        barycenter_list : list
            List of barycenters to be created (Body1-Body2-...-Bodyn-barycenter)
        libration_point_list : list
            List of libration points to be created (...)
        """

        if barycenter_list is None:
            pass

        else:
            barycenter_bodies = []
            barycenter_dict = {}

            for bodies_list in barycenter_list:
                barycenter_bodies = [self.bodies_dict[body] for body in bodies_list]

                barycenter_instance = barycenter(barycenter_bodies)

                setattr(self, barycenter_instance.name.replace("-", "_"), barycenter_instance)

                barycenter_dict.update({barycenter_instance.name: barycenter_instance})

            # add a dict as ss attribute
            setattr(self, "barycenters", barycenter_dict)
            self.bodies_dict.update(self.barycenters)

        if libration_point_list is None:
            pass
        else:
            libration_points_dict = {}
            for libration_data in libration_point_list:

                libration_data = [self.bodies_dict[body] for body in libration_data[:2]] + [libration_data[2]]

                libration_point_instance = libration_point(*libration_data)

                setattr(self,
                        libration_point_instance.name.replace("-", "_").replace("/", "__"),
                        libration_point_instance)

                libration_points_dict.update({libration_point_instance.name: libration_point_instance})

            # add a dict as ss attribute
            setattr(self, "libration_points", libration_points_dict)
            self.bodies_dict.update(self.libration_points)

        return 0


class celestial_body():
    cetype = 'body'

    def __init__(self, body_dict, ephemeris):
        for k, v in body_dict.items():
            setattr(self, k, v)

        self.eph = ephemeris

    def r(self, t):
        """
        Returns position of the celestial body in J2000Eq frame centered at Sun
        """

        r = self.eph.r(self.name, t)

        return r

    def v(self, t):
        """
        Returns velocity of the celestial body in J2000Eq frame centered at Sun
        """

        v = self.eph.v(self.name, t)

        return v

    def Torb(self):
        T = 2 * np.pi * np.sqrt(self.sma**3/(cte.G * self.mass))
        return T


class barycenter():
    cetype = 'barycenter'

    def __init__(self, celestial_bodies):
        """
        Constructor

        Parameters
        ----------
        celestial_bodies : list
            list of celestial bodies instances
        """

        self.bodies_list = []
        self.bodies_dict = {}
        self.type = "barycenter"
        self.mass = 0
        self.sma = 0

        self.set_barycenter(celestial_bodies)
        self.set_name()

    def set_barycenter(self, celestial_bodies):
        """
        Add the celestial bodies instances as attributes of the barycenter class
        and computes its total mass.

        Parameters
        ----------
        celestial_bodies : list
            list of celestial bodies instances
        """

        for body in celestial_bodies:
            self.bodies_list.append(body.name)
            self.bodies_dict[body.name] = body
            self.mass += body.mass
            self.sma += body.sma * body.mass

        self.sma /= self.mass

        return 0

    def set_name(self):
        """
        Sets the default name of the barycenter based on the list of bodies
        which defines it.
        """

        self.name = '-'.join(self.bodies_list) + "-barycenter"

        return 0

    def r(self, t):
        """
        Returns position of the barycenter regarding the Sun in Sun-J2000Eq frame

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Barycenter position
        """

        r = np.zeros((3, len(t)))

        for body in self.bodies_dict.values():

            r += body.r(np.array([t]).flatten()) * body.mass

        r /= self.mass

        return r

    def v(self, t):
        """
        Returns velocity of the barycenter regarding the Sun in Sun-J2000Eq frame

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Barycenter velocity
        """

        v = np.zeros((3, len(t)))

        for body in self.bodies_dict.values():

            v += body.v(np.array([t]).flatten()) * body.mass

        v /= self.mass

        return v


class libration_point():
    cetype = "libration_point"

    def __init__(self, primary_1, primary_2, point_number):
        """
        Constructor

        Parameters
        ----------
        primary_1 : celestial_body class
            Celestial_body instance of primary with higher mass
        primary_2 : celestial_body class
            Celestial_body instance of primary with lower mass
        point_number : str
            Lagrange point
        """

        self.p1 = primary_1
        self.p2 = primary_2

        self.mu = self.p2.mass/(self.p2.mass + self.p1.mass)

        self.Ln = point_number

        self.check_primaries_order()
        self.get_xL()
        self.set_name()
        self.check_stability()

    def check_primaries_order(self):
        """
        Checks that m_p1 > m_p2
        """

        if self.p2.mass > self.p1.mass:
            raise Exception("Wrong primaries order. P1 must be the primary with the largest mass")
        else:
            pass

        return 0

    def check_stability(self):
        pass

    def set_name(self):
        """
        Sets the default name of the libration point based on the list of bodies
        which defines it.
        """

        self.name = self.p1.name + "/" + self.p2.name + "/L" + str(self.Ln)

        return 0

    def location_primary(self):
        """
        Returns adimensional position of colinear libration points to the nearest primary.

        References:
        - V. G. Szebehely, Theory of orbits, the restricted problem of three bodies. Chapter 4.
        - GMATMathSpec

        Returns
        -------
        gammax : float
            x-distance of the libration point to the nearest primary (adimensional)
        gammay : float
            y-distance of the libration point to the nearest primary (adimensional)
        """

        mu = self.mu
        point_number = self.Ln

        def f(x, p0, p1, p2, p3, p4, p5):
            return p5 * x**5 + p4 * x**4 + p3 * x**3 + p2 * x**2 + p1 * x + p0

        if point_number == 1 or point_number == 2 or point_number == 3:

            p5 = 1

            if point_number == 1:
                p4 = - (3 - mu)
                p3 = 3 - 2 * mu
                p2 = - mu
                p1 = 2 * mu
                p0 = - mu

                x0 = (mu / (3 * (1 - mu)))**(1. / 3)  # initial guess for the iterative procedure

            elif point_number == 2:
                p4 = 3 - mu
                p3 = 3 - 2 * mu
                p2 = - mu
                p1 = - 2 * mu
                p0 = - mu

                x0 = (mu / (3 * (1 - mu)))**(1. / 3)  # initial guess for the iterative procedure

            else:
                p4 = 2 + mu
                p3 = 1 + 2 * mu
                p2 = - (1 - mu)
                p1 = - 2 * (1 - mu)
                p0 = - (1 - mu)

                x0 = 1 - 7 / 12.0 * mu                # initial guess for the iterative procedure (why not 1?)

            gammax = newton(f, x0=x0, args=(p0, p1, p2, p3, p4, p5,), maxiter=10000)
            gammay = 0

        elif point_number == 4 or point_number == 5:
            gammax = 1 / 2
            gammay = sqrt(3) / 2

        else:
            print("Invalid point number")
            gammax = 0
            gammay = 0

        return gammax, gammay

    def location_CoM(self):
        """
        Returns adimensional position of colinear libration points to the center of mass of the primaries system.

        References:
        - V. G. Szebehely, Theory of orbits, the restricted problem of three bodies. Chapter 4.
        - GMATMathSpec

        Returns
        -------
        x : float
            x-position of the libration point in synodic frame (adimensional)
        y : float
            y-position of the libration point in synodic frame (adimensional)
        """

        mu = self.mu
        point_number = self.Ln

        gammax, gammay = self.location_primary()

        if point_number == 1:
            x = 1 - mu - gammax
            y = gammay  # 0

        elif point_number == 2:
            x = 1 - mu + gammax
            y = gammay  # 0

        elif point_number == 3:
            x = - (mu + gammax)
            y = gammay  # 0

        elif point_number == 4:
            x = gammax - mu
            y = gammay

        elif point_number == 5:
            x = gammax - mu
            y = - gammay

        return x, y

    def plot_libration_points(self, positions):

        """
        Returns plot including the primaries, their orbits and the five libration points' locations.

        References:
        - V. G. Szebehely, Theory of orbits, the restricted problem of three bodies. Chapter 4.
        - GMATMathSpec

        Parameters
        ----------
        positions : list
            Includes the x and y positions of all libration points in a synodic frame.
        """

        mu = self.mu

        # Obtaining libration points' coordinates with respect to center of mass
        x1, y1 = positions[0], positions[1]
        x2, y2 = positions[2], positions[3]
        x3, y3 = positions[4], positions[5]
        x4, y4 = positions[6], positions[7]
        x5, y5 = positions[8], positions[9]

        # Plotting primaries and their orbits
        primary1 = plt.Circle((- mu, 0), 0.1, color='black')
        primary2 = plt.Circle((1 - mu, 0), 0.05, color='black')
        orbit_2 = plt.Circle((- mu, 0), 1, color='blue', fill=False)
        _, ax = plt.subplots()
        ax.add_patch(primary1)
        ax.add_patch(primary2)
        ax.add_patch(orbit_2)

        # Plotting libration points
        ax.plot(x1, y1, 'x', color='black', lw=1)
        plt.annotate("L1", (x1 + 0.05, y1 + 0.05), textcoords="offset points", xytext=(0, 0))
        ax.plot(x2, y2, 'x', color='black', lw=1)
        plt.annotate("L2", (x2 + 0.05, y2 + 0.05), textcoords="offset points", xytext=(0, 0))
        ax.plot(x3, y3, 'x', color='black', lw=1)
        plt.annotate("L3", (x3 + 0.05, y3 + 0.05), textcoords="offset points", xytext=(0, 0))
        ax.plot(x4, y4, 'x', color='black', lw=1)
        plt.annotate("L4", (x4 + 0.05, y4 + 0.05), textcoords="offset points", xytext=(0, 0))
        ax.plot(x5, y5, 'x', color='black', lw=1)
        plt.annotate("L5", (x5 + 0.05, y5 + 0.05), textcoords="offset points", xytext=(0, 0))

        # Plot general properties
        plt.axis([-2, 2, -2, 2])
        ax.set_aspect(1)
        plt.show(block=False)

        return 0

    def get_xL(self):

        self.xL, self.yL = self.location_CoM()

        return 0

    def r(self, t):
        """
        Returns position of the libration point regarding the Sun in
        Sun-J2000Eq frame

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position
        """

        r_synodic = (np.linalg.norm(self.p2.r(t) - self.p1.r(t), axis=0)
                     * (self.xL + self.mu)
                     * np.array([1, 0, 0]).reshape(-1, 1))

        r = np.einsum('ijk,jk->ik', self.R(t), r_synodic) + self.p1.r(t)

        return r

    def v(self, t):
        """
        Returns velocity of the libration point regarding the Sun in
        Sun-J2000Eq frame

        Parameters
        ----------
        t : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Velocity
        """

        r_synodic = (np.linalg.norm(self.p2.r(t) - self.p1.r(t), axis=0)
                     * (self.xL + self.mu)
                     * np.array([1, 0, 0]).reshape(-1, 1))

        v_synodic = (np.einsum('ij,ij->i', (self.p2.v(t) - self.p1.v(t)).T, (self.p2.r(t) - self.p1.r(t)).T)
                     / np.linalg.norm(r_synodic, axis=0)
                     * (self.xL + self.mu) * np.array([1, 0, 0]).reshape(-1, 1))

        v = np.einsum('ijk,jk->ik', self.Rp(t), r_synodic) + np.einsum('ijk,jk->ik', self.R(t), v_synodic)

        return v

    def R(self, t):
        """
        Computes rotation matrix from this frame to FK5

        Rotation matrix R12 is built with the basis vectors of S2 in columns [i j k] expressed
        in S1.  u1 = R12 @ u2

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
        Computes the derivate of the rotation matrix from this frame to FK5, wich results in null matrix

        Rotation matrix Rp12 is built with the basis vectors derivate of S2 in columns [ip jp kp] expressed
        in S1.  u1 = R12 @ u2

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

        xp_syn_norm = (v/nm.norm(r.T)
                       - np.einsum('i,ij->ij',  np.einsum('ij,ij->i', x_syn_norm, v), x_syn_norm/nm.norm(r.T)))

        zp_syn_norm = (np.cross(r, a)/nm.norm(z_syn.T)
                       - np.einsum('i,ij->ij', np.einsum('ij,ij->i', np.cross(r, a), z_syn_norm), z_syn_norm/nm.norm(z_syn.T))) # noqa

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

        r1 = self.p1.r(t)
        r2 = self.p2.r(t)

        r = r2 - r1

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

        v1 = self.p1.v(t)
        v2 = self.p2.v(t)

        v = v2 - v1

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

        # Assuming that rxa is zero (as GMAT)

        a = np.zeros((3, len(t)))

        return a


class Ephemeris():
    """
    Ephemeris class

    Attributes
    ----------
    name : str
        Name of the model
    """

    def __init__(self, epoch, bodies, tf, dT, reference='Sun'):
        """
        Constructor

        Parameters
        ----------
        epoch : DateTime class
            Epoch used as time reference
        bodies : list
            List of strings with the names of the celestial bodies whose
            ephemeris are generated
        tf : float
            Extent of time for which the ephemeris are generated (s)
        dT : float
            Time step
        reference : str
            NAIF id of the body used as reference for the ephemeris
        """

        self.epoch = epoch
        self.bodies = bodies
        self.tf = tf
        self.dT = dT
        self.reference = reference

        self.load_kernels()
        self.load_ephemeris()

    def load_kernels(self):
        """
        Load SPICE kernels.

        If kernel files are not in the system, it will try to download them.
        If the kernel are already loaded, it will do nothing.
        """

        self.kernels_folder_path = pkg_resources.resource_filename('mubody', 'data/')
        self.kernels_list = ['de405.bsp', 'naif0011.txt']

        if self.check_kernels_files():
            pass
        else:
            if not os.path.exists("src/mubody/data"):
                os.makedirs("src/mubody/data")
            try:
                self.download_kernels()
            except Exception:
                raise Exception("Error downloading SPICE kernels.")

        if self.check_kernels_load():
            pass
        else:
            for kernel in self.kernels_list:
                file_path = self.kernels_folder_path + kernel
                spice.furnsh(file_path)

        return 0

    def check_kernels_files(self):
        """
        Checks if the required kernels files are present in the data folder.

        Returns
        -------
        kernels_files_flag : boolean
            If True, all required kernels files are present
        """

        kernels_files_flag_list = []

        for kernel in self.kernels_list:
            file_path = self.kernels_folder_path + kernel
            kernels_files_flag_list.append(Path(file_path).is_file())

        kernels_files_flag = all(kernels_files_flag_list)

        return kernels_files_flag

    def check_kernels_load(self):
        """
        Checks if the required kernels files have been loaded.

        Returns
        -------
        kernels_load_flag : boolean
            If True, all required kernels files are present
        """

        n_kernels = spice.ktotal('ALL')
        loaded_kernels_list = []

        for i in range(0, n_kernels):
            [file, _, _, _] = spice.kdata(i, 'ALL')
            loaded_kernels_list.append(file)

        kernels_load_flag = set(loaded_kernels_list) == set(self.kernels_list)

        return kernels_load_flag

    def download_kernels(self):
        """
        Downloads the required kernels.
        """

        url_dict = {'de405.bsp': 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de405.bsp', # noqa
                    'naif0011.txt': 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0011.tls'
                    }

        print("Downloading required kernels...")

        os.makedirs(os.path.dirname(self.kernels_folder_path), exist_ok=True)

        for kernel in self.kernels_list:
            r = requests.get(url_dict[kernel])
            file_path = self.kernels_folder_path + kernel
            open(file_path, 'wb').write(r.content)

        print("Done")

        return 0

    def get_spice_eph(self, date, body, time, reference):
        """
        Retrieves ephemeris from spice kernels

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        states : ndarray (6,n)
            State vectors of the target body
        """

        t_ephem = time/(3600*24) + date.jd

        et_f = []

        for item in np.asarray([t_ephem]).flatten():
            et = spice.str2et(str(item) + 'JD')
            et_f = np.append(et_f, et)

        body_id = cte.id_dict_V2[body]
        reference_id = cte.id_dict_V2[reference]
        states, _ = spice.spkezr(body_id, et_f, 'J2000', 'NONE', reference_id)
        states = np.asarray(states).T * 1e3

        return states

    def generate_ephemeris_dict(self, epoch, bodies, tf, dT, reference):
        """
        Retrieves ephemeris from spice kernels and stores them for interpolation

        The epehemeris are retrieved for a period of time with a sample time. Then,
        tck parameters are generated for interpolation of intermediate times. The
        parameters of each body/point are stored in a dict as a global variable.

        Parameters
        ----------
        epoch : DateTime class
            Epoch of time[0]
        bodies : list
            List of names of the target celestial bodies/points
        tf : float
            Extent of time for which the ephemeris are generated (s)
        dT : float
            Time step
        reference : str
            Name of the celestial body/point used as reference
        """
        # global ephemeris_dict
        ephemeris_dict = {}

        k = 3
        time_margin = 10 * 86400

        time = np.arange(-time_margin, tf + time_margin, dT)

        for body in bodies:
            ephemeris = self.get_spice_eph(epoch, body, time, reference)

            r_eph = ephemeris[0:3, :]
            v_eph = ephemeris[3:6, :]

            x_slp = splrep(time, r_eph[0], k=k)
            y_slp = splrep(time, r_eph[1], k=k)
            z_slp = splrep(time, r_eph[2], k=k)
            vx_slp = splrep(time, v_eph[0], k=k)
            vy_slp = splrep(time, v_eph[1], k=k)
            vz_slp = splrep(time, v_eph[2], k=k)

            slp_dict = {'x': x_slp, 'y': y_slp, 'z': z_slp, 'vx': vx_slp, 'vy': vy_slp, 'vz': vz_slp}

            ephemeris_dict.update({body: slp_dict})

        return ephemeris_dict

    def load_ephemeris(self):
        """
        Retrieves ephemeris from spice kernels and stores them for interpolation

        The epehemeris are retrieved for a period of time with a sample time. Then,
        tck parameters are generated for interpolation of intermediate times. The
        parameters of each body/point are stored in a dict as a global variable.

        """

        self.ephemeris_dict = self.generate_ephemeris_dict(self.epoch, self.bodies, self.tf, self.dT, self.reference)

        return 0

    def get_eph_r_sp(self, date, body, time, reference):
        """
        Retrieves position of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        r : ndarray (3,n)
            Position vectors of the target body
        """

        states = self.get_spice_eph(date, body, time, reference)

        r = states[0:3, :]

        return r

    def get_eph_v_sp(self, date, body, time, reference):
        """
        Retrieves velocity of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        v : ndarray (3,n)
            Velocity vectors of the target body
        """

        states = self.get_spice_eph(date, body, time, reference)

        v = states[3:6, :]

        return v

    def r_sp(self, body, time):
        """
        Retrieves position of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position vectors of the target body
        """

        states = self.get_eph_r_sp(self.epoch, body, time, self.reference)

        r = states[0:3, :]

        return r

    def v_sp(self, body, time):
        """
        Retrieves velocity of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Velocity vectors of the target body
        """

        states = self.get_eph_v_sp(self.epoch, body, time, self.reference)

        v = states[3:6, :]

        return v

    def get_eph_r(self, date, body, time, reference):
        """
        Interpolates position from ephemeris

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        r : ndarray (3,n)
            Position vectors of the target body
        """

        slp = self.ephemeris_dict[body]
        x_slp = slp['x']
        y_slp = slp['y']
        z_slp = slp['z']

        x = splev(time, x_slp)
        y = splev(time, y_slp)
        z = splev(time, z_slp)

        r = np.array([x, y, z]).reshape(3, -1)

        return r

    def get_eph_v(self, date, body, time, reference):
        """
        Interpolates velocity from ephemeris

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        v : ndarray (3,n)
            Velocity vectors of the target body
        """

        slp = self.ephemeris_dict[body]
        vx_slp = slp['vx']
        vy_slp = slp['vy']
        vz_slp = slp['vz']

        vx = splev(time, vx_slp)
        vy = splev(time, vy_slp)
        vz = splev(time, vz_slp)

        v = np.array([vx, vy, vz]).reshape(3, -1)

        return v

    def r(self, body, time):
        """
        Interpolates position from ephemeris

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3,n)
            Position vectors of the target body
        """

        r = self.get_eph_r(self.epoch, body, time, self.reference)

        return r

    def v(self, body, time):
        """
        Interpolates velocity from ephemeris

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest

        Returns
        -------
        v : ndarray (3,n)
            Velocity vectors of the target body
        """

        v = self.get_eph_v(self.epoch, body, time, self.reference)

        return v
