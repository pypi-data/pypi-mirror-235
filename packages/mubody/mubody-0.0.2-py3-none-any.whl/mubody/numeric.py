import numpy as np
import numpy.linalg as LA
from scipy.integrate import solve_ivp
from numba import jit


def propagate_analytically(model, inputs, tf, dT, bar):
    """
    Propagates the trajectory according to analytical solution of the
    linearised CRTBP model

    Parameters
    ----------
    model : CRTBP class
        class with physical model
    GOLE : list
        set of General Osculating Lissajous Elements
    tf : float
        simulation time
    dT : float
        step time
    bar : boolean
        if True, shows progress bar

    Returns
    -------
    time : ndarray
        Discretized time
    position : ndarray
        Position vector in each time step (3,n)
    velocity : float, optional
        Velocity vector in each time step (3,n)
    """

    dimensional_flag = True

    frame = "P1-IdealSynodic"

    N = int(np.ceil(tf/dT))

    time = np.linspace(0, tf, N)

    position = model.r_linear(inputs, time)   # Inputs: GOLE if CRTBP
    velocity = model.v_linear(inputs, time)   # Inputs: HALO inputs if CRTBP

    return time, position, velocity, dimensional_flag, frame


def propagate_numerically(model, t0, tf, IC, N):
    """
    Function to propagate motion numerically

    Parameters
    ----------
    model : CRTBP class
        Physical model with the equations of motions
    IC : ndarray
        State vector of initial conditions [x, y, z, vx, vy, vz]
        (m, m/s)
    tf : float
        End time for propagation (s)
    dT : float
        Step time for integration (s)
    bar : bool
        If True, shows progress bar

    Returns
    -------
    time : ndarray
        Discretized time (s)
    position : ndarray
        Position vector in each time step [nx3] (m)
    velocity : float, optional
        Velocity vector in each time step [nx3] (m/s)
    """

    if model.name == "CRTBP":
        dimensional_flag = False
        frame = 'P1-IdealSynodic'
    else:
        dimensional_flag = True
        frame = 'Sun-J2000Eq'

    tf /= model.ts
    time, states = integrator(model.F, t0, tf, IC.flatten(), N, model.ts)

    position = states[0:3]
    velocity = states[3:6]

    return time, position, velocity, dimensional_flag, frame


def integrator(F, t0, tf, y0, N, ts, tols=(1e-11, 1e-11), events=None):
    """
    Integrates function over a time period.

    The value of rtol is the maximum allowed while atol is choosen to produce
    an error of 1 mm in x axis in the CRTBP problem

    Parameters
    ----------
    F : callable function
        Returns 1D-array (n,)
    t0 : float
        Starting integration time
    tf : float
        Final integration time
    y0 : 1d-array (n,)
        Initial conditions
    N : integer
        Number of discretization points for the solution
    ts : float
        Nondimensionalization factor

    Returns
    -------
    time : 1D-array (N,)
        Intermediate times where solution is calculated
    states : ndarray (6, N)
        Solution in intermidiate points
    """

    rtol = tols[0]
    atol = tols[1]

    first_step = 0.1/ts

    time = np.linspace(t0, tf, N)

    solution = solve_ivp(F,
                         [t0, tf],
                         y0,
                         t_eval=time,
                         method='DOP853',
                         vectorized=True,
                         first_step=first_step,
                         rtol=rtol,
                         atol=atol,
                         events=events
                         )

    time = solution.t
    states = solution.y

    if events is not None:
        return time, states, solution.t_events
    else:
        return time, states


def generate_M(ap, an, vp, vn, phi):
    """
    Builds the M matrix

    Parameters
    ----------
    ap : ndarray (3xn) (m/s2)
        acceleration after correction
    an : ndarray (3xn) (m/s2)
        acceleration before correction
    vp : ndarray (3xn) (m/s)
        velocity after correction
    vn : ndarray (3xn) (m/s)
        velocity before correction
    phi : ndarray (6x6xn)
        STM of each segment

    Returns
    -------
    M_M : ndarray (3(n-1) x 4(n+1))
        M matrix
    """

    # number of intermediate points
    Nip = np.size(phi, 2) - 1

    n = Nip + 1
    M_M = np.zeros(((3 * n - 3), (4 * n + 4)))

    nr = 3
    nc = 4

    for i in range(Nip):

        pf, p0 = matrix(phi[:, :, i], phi[:, :, i + 1])

        M0 = p0[3] @ LA.inv(p0[1]) @ p0[0] - p0[2]
        Mt0 = an[:, [i]] - p0[3] @ LA.inv(p0[1]) @ vn[:, [i]]

        Mp = pf[3] @ LA.inv(pf[1]) - p0[3] @ LA.inv(p0[1])
        Mtp = p0[3] @ LA.inv(p0[1]) @ vn[:, [i]] - pf[3] @ LA.inv(pf[1]) @ vp[:, [i]] + ap[:, [i]] - an[:, [i]]

        Mf = pf[2] - pf[3] @ LA.inv(pf[1]) @ pf[0]
        Mtf = pf[3] @ LA.inv(pf[1]) @ vp[:, [i]] - ap[:, [i]]

        M_sub = np.block([M0, Mt0*0, Mp, Mtp*0, Mf, Mtf*0])

        M_M[nr * i:nr * (i + 1), nc * i:nc * (i+3)] = M_sub

    return M_M


def matrix(phi0, phif):
    """this method obtains matrix A, B, C and D from phi"""
    # state transition matrix from f to p
    phipf = np.linalg.inv(phif)

    Apf = phipf[0:3, 0:3]
    Bpf = phipf[0:3, 3:6]
    Cpf = phipf[3:6, 0:3]
    Dpf = phipf[3:6, 3:6]

    pf = [Apf, Bpf, Cpf, Dpf]

    # state transition matrix from 0 to p
    phip0 = phi0

    Ap0 = phip0[0:3, 0:3]
    Bp0 = phip0[0:3, 3:6]
    Cp0 = phip0[3:6, 0:3]
    Dp0 = phip0[3:6, 3:6]

    p0 = [Ap0, Bp0, Cp0, Dp0]

    return pf, p0


def norm(v):
    """
    Calculates norm of vector

    Parameters
    ----------
    v : ndarray (3xn)
        Input vector

    Returns
    -------
    v_mod : ndarray (nx1)
        vector of norms

    """
    x, y, z = v

    v_mod = np.sqrt(x**2 + y**2 + z**2).reshape(-1, 1)

    return v_mod


@jit
def norm_sc(x, y, z):
    """
    Calculates norm of vector

    Parameters
    ----------
    v : ndarray (3x1)
        Input vector

    Returns
    -------
    mod : float
        Norm of vector

    """

    mod = np.sqrt(x**2 + y**2 + z**2)

    return mod
