import numpy as np
import pandas as pd
from tqdm.auto import tqdm
import mubody.numeric as nm
import numpy.linalg as LA


def targeting_method(model, tra_ref_points_df, bar, orbit_type, max_iter=100):
    """
    Targeting method algorithm

    Parameters
    ----------
    model : str
        Physical model to be used (CRTBP/ERTBP/FETBP)
    tra_ref_points_df : dataframe
        Trajectory reference points
    dT : float
        Time step (seconds)
    bar : bool
        If True, shows progress bar
    max_iter : integer
        Maximum number of iterations
    error_thres : float
        Error threshold (m)

    Returns
    -------
    time : 1-D array (1000*(n-1)+1)
        Time step (seconds)
    position : ndarray (3,1000*(n-1)+1)
        Trajectory (m)
    velocity : ndarray (3,1000*(n-1))
        Velocity along trajectory (m/s)
    DV : ndarray (3,n)
        Velocity impulses for each segment initial point (m/s)
    DT : ndarray (3,n)
        DT array (seconds)
    phi : ndarray (6,6,1000*(n-1)+1)
        phi matrix along trajectory
    """

    N_points = len(tra_ref_points_df.index)
    N_segments = N_points - 1

    time_points = tra_ref_points_df.index.values
    states_points_ref = tra_ref_points_df.values.T

    phi_conc = np.empty((6, 6, 0))
    position = np.empty((3, 0))
    velocity = np.empty((3, 0))
    time = np.empty(0)

    phi0 = np.eye(6)
    DT = np.zeros(N_points)
    DV = np.zeros((3, N_points))

    dummy_velocity = np.zeros((3, 1))

    int_tol = (1e-11, 1e-11)
    phi_tol = (1e-5, 1e-5)

    if bar:
        pbar = tqdm(total=N_segments)

    for i in range(N_segments):

        if i == 0:
            v_original = np.copy(states_points_ref[3:6, i])

        else:
            v_original = dummy_velocity
            # v_original = np.copy(states_points_ref[3:6,i])
            pass

        t_original = np.copy(time_points[i+1])

        for j in range(max_iter):

            time_discretized, integration_output = nm.integrator(model.F,
                                                                 time_points[i],
                                                                 time_points[i+1],
                                                                 states_points_ref[:, i],
                                                                 1000,
                                                                 model.ts,
                                                                 tols=int_tol)

            model.add_trajectory(time_discretized, integration_output[0:3])

            _, phi_segments = nm.integrator(model.phi_dot_vec,
                                            time_points[i],
                                            time_points[i+1],
                                            phi0.flatten('F'),
                                            3,
                                            model.ts,
                                            tols=phi_tol)

            r_reached = integration_output[0:3, -1:]
            r_desired = states_points_ref[0:3, [i+1]]

            error_v = r_reached - r_desired
            error_m = np.linalg.norm((r_reached - r_desired))/np.linalg.norm(r_desired)

            error_tol = 1e-11

            if error_m < error_tol:
                break

            if j == (max_iter - 1):
                print("WARNING - Convergence non reached", int(np.log10(error_tol) - np.log10(error_m)))

            L = np.concatenate((phi_segments[:, -1].reshape(6, 6, order='F')[0:3, 3:6],
                                integration_output[3:6, -1:]), axis=1)

            u = np.matmul(L.T @ np.linalg.inv(L @ L.T), error_v)

            states_points_ref[3:6, [i]] -= u[0:3].reshape(-1, 1)
            time_points[i+1] -= u[3]

        DV[:, i] = states_points_ref[3:6, i] - v_original

        phi_conc = np.append(phi_conc, phi_segments[:, -1].reshape(6, 6, order='F').reshape(6, 6, 1), axis=2)

        DT[i+1] = time_points[i+1] - t_original

        if bar:
            pbar.update(1)

        position = np.append(position, integration_output[0:3, :-1], axis=1)
        velocity = np.append(velocity, integration_output[3:6, :-1], axis=1)
        time = np.append(time, time_discretized[:-1])
        dummy_velocity = integration_output[3:6, -1]

    position = np.append(position, integration_output[0:3, [-1]], axis=1)
    velocity = np.append(velocity, integration_output[3:6, [-1]], axis=1)

    time = np.append(time, time_discretized[-1])

    if bar:
        pbar.close()
        print("\n")

    return time, position, velocity, DV, DT, phi_conc


def Halo_targeting_method(model, tra_ref_points_df, bar, max_iter=100):
    """
    Targeting method algorithm for Halo orbits. Returns one period of Halo orbit.
    Reference: Formation Flying in the Sun-Earth/Moon Perturbed Restricted Three-Body Problem, Ingvar Out.

    Parameters
    ----------
    model : str
        Physical model to be used (CRTBP/ERTBP/FETBP)
    tra_ref_points_df : dataframe
        Trajectory reference points
    bar : bool
        If True, shows progress bar
    max_iter : integer
        Maximum number of iterations

    Returns
    -------
    time : 1-D array (1000*(n-1)+1)
           Time instant (adimensional)
    position : ndarray (3,1000*(n-1)+1)
               Trajectory (adimensional)
    velocity : ndarray (3,1000*(n-1))
               Velocity along trajectory (adimensional)
    DV : ndarray (3,n)
         Velocity impulses for each segment initial point (adimensional)
    DT : ndarray (3,n)
         DT array (adimensional)
    phi_conc : ndarray (6,6,1000*(n-1)+1)
               phi matrix along trajectory
    """

    N_points = len(tra_ref_points_df.index)
    N_segments = N_points - 1

    time_points = tra_ref_points_df.index.values
    states_points_ref = tra_ref_points_df.values.T

    phi_conc = np.empty((6, 6, 0))
    position = np.empty((3, 0))
    velocity = np.empty((3, 0))
    time = np.empty(0)

    phi0 = np.eye(6)
    DT = np.zeros(N_points)
    DV = np.zeros((3, N_points))

    dummy_velocity = np.zeros((3, 1))

    Dstate = np.zeros((6, N_points))
    int_tol = (1e-11, 1e-11)
    phi_tol = (1e-5, 1e-5)

    if bar:
        pbar = tqdm(total=N_segments)

    for i in range(N_segments):

        DVT2 = np.ones((2, 1))

        if i == 0:
            v_original = np.copy(states_points_ref[:, i])
        else:
            v_original = dummy_velocity
            # v_original = np.copy(states_points_ref[3:6,i])
            pass

        t_original = np.copy(time_points[i+1])

        def XZ_crossing(t, y): return y[1]

        XZ_crossing.terminal = True

        # XZ_crossing.direction = -1

        for j in range(max_iter):

            time_discretized, integration_output, tf = nm.integrator(model.F,
                                                                     time_points[i],
                                                                     time_points[i+1]*1.2,
                                                                     states_points_ref[:, i],
                                                                     100,
                                                                     model.ts,
                                                                     tols=int_tol,
                                                                     events=XZ_crossing)

            tf = tf[0][0]
            time_discretized, integration_output = nm.integrator(model.F,
                                                                 time_points[i],
                                                                 tf,
                                                                 states_points_ref[:, i],
                                                                 1000,
                                                                 model.ts,
                                                                 tols=phi_tol)

            model.add_trajectory(time_discretized, integration_output[0:3])

            _, phi_segments = nm.integrator(model.phi_dot_vec,
                                            time_points[i],
                                            tf,
                                            phi0.flatten('F'),
                                            3,
                                            model.ts,
                                            tols=phi_tol)

            r_reached = integration_output[0:3, -1:]
            r_desired = states_points_ref[0:3, [i+1]]

            error_m = np.linalg.norm((r_reached - r_desired))/np.linalg.norm(r_desired)

            error_tol = 1e-8
            # if states_points_ref[1, [i+1]] < 10**-11 and states_points_ref[3, [i+1]] < error_tol \
            # and states_points_ref[5, [i+1]] < error_tol:
            if np.all(abs(DVT2) < error_tol):
                break

            if j == (max_iter - 1):
                print("WARNING - Convergence non reached", int(np.log10(error_tol) - np.log10(error_m)))

            phi = phi_segments[:, -1].reshape(6, 6, order='F').reshape(6, 6, 1)

            aT2 = model.a(tf, integration_output[:, [-1]])

            DVT2[0, 0] = integration_output[3, -1:] - states_points_ref[3, [i+1]]
            DVT2[1, 0] = integration_output[5, -1:] - states_points_ref[5, [i+1]]

            A1 = np.array([[phi[3, 2, 0], phi[3, 4, 0]], [phi[5, 2, 0], phi[5, 4, 0]]])
            acc = np.array([aT2[0], aT2[2]])
            A2 = np.array([[phi[1, 2, 0]], [phi[1, 4, 0]]])
            vyT2 = integration_output[4, -1]

            Ds = np.dot(np.linalg.inv(A1 - 1/vyT2*np.dot(acc, A2)), DVT2)  # For one segment, it does not append

            states_points_ref[2, [i]] -= Ds[0, 0]
            states_points_ref[4, [i]] -= Ds[1, 0]

        Dstate[:, i] = states_points_ref[:, i] - v_original  # State vector variation
        DV[:, i] = Dstate[3:6, i]

        phi_conc = np.append(phi_conc, phi_segments[:, -1].reshape(6, 6, order='F').reshape(6, 6, 1), axis=2)

        DT[i+1] = time_points[i+1] - t_original

        if bar:
            pbar.update(1)

        position = np.append(position, integration_output[0:3, :-1], axis=1)
        velocity = np.append(velocity, integration_output[3:6, :-1], axis=1)
        time = np.append(time, time_discretized[:-1])
        dummy_velocity = integration_output[:, -1]

    position = np.append(position, integration_output[0:3, [-1]], axis=1)
    velocity = np.append(velocity, integration_output[3:6, [-1]], axis=1)

    time = np.append(time, time_discretized[-1])

    if bar:
        pbar.close()
        print("\n")

    # print('states points ref', states_points_ref[1, :], states_points_ref[3, :], states_points_ref[5, :])
    # print('DVT2', DVT2)

    return time, position, velocity, DV, DT, phi_conc


def optimized_targeting_method(model, tra_ref_points_df, N_segments, opt_iterations, bar, orbit_type):
    """
    Targeting method algorithm

    Parameters
    ----------
    model : str
        Physical model to be used (CRTBP/ERTBP/FETBP)
    tra_ref_points_df : dataframe
        Trajectory reference points
    dT : float
        Time step (seconds)
    N_segments : integer
        Number of segments
    opt_iterations : integer
        Number of iterations to optimize
    bar : bool
        If True, shows progress bar

    Returns
    -------
    time : 1-D array (n)
        Time step (seconds)
    position : ndarray (nx3)
        Trajectory (m)
    velocity : ndarray (nx3)
        Velocity along trajectory (m/s)
    DV : ndarray (nx3)
        DV array (seconds)
    """

    tf = tra_ref_points_df.tail(1).index.values[0] - tra_ref_points_df.head(1).index.values[0]
    # t_maneouver = tf/N_segments
    DR = np.zeros((3, N_segments + 1))
    DR_lin = DR.flatten() * 0
    DT = np.zeros(N_segments + 1)

    if bar:
        pbar = tqdm(total=opt_iterations + 1)

    states_ref = tra_ref_points_df.values.T
    times_ref = tra_ref_points_df.index.values

    DV_opt = np.zeros(opt_iterations + 1)

    for i in range(opt_iterations + 1):

        # TotalDV_opt = 0

        # times_ref += DT - DT[0]
        # dt = TimeDelta(DT[0], format='sec')
        # model.DS.date -= dt

        states_ref[0:3, :] += DR

        tra_ref_points_df = pd.DataFrame(data=states_ref.T, columns=tra_ref_points_df.columns, index=times_ref)

        time, position, velocity, DV, DT0, phi_data = targeting_method(model, tra_ref_points_df, bar=False,
                                                                       orbit_type=orbit_type)

        states_ref_before_correction = np.copy(states_ref)

        if orbit_type == 'Halo2':
            states_ref += DV
        else:
            states_ref[3:6, :] += DV

        # times_ref += DT0 - DT0[0]
        # dt = TimeDelta(DT0[0], format='sec')
        # model.DS.date -= dt

        an = model.a(times_ref[1:-1], states_ref_before_correction[:, 1:-1])
        vn = states_ref_before_correction[3:6, 1:-1]

        ap = model.a(times_ref[1:-1], states_ref[:, 1:-1])
        vp = states_ref[3:6, 1:-1]

        M = nm.generate_M(ap, an, vp, vn, phi_data)

        if orbit_type == 'Halo2':
            DV_flat = DV[3:6, 1:-1].flatten('F')
            DV_opt[i] = int(np.linalg.norm(DV[3:6, 1:-1] * model.vs, axis=0).sum())
        else:
            DV_flat = DV[:, 1:-1].flatten('F')
            DV_opt[i] = int(np.linalg.norm(DV[:, 1:-1] * model.vs, axis=0).sum())

        DD = -M.T @ LA.inv(M @ M.T) @ DV_flat

        for j in range(N_segments + 1):

            DR_lin[(3 * j):(3 * j + 3)] = DD[(4 * j):(4 * j + 3)]
            DT[j] = DD[(4 * j + 3)]

        DR = np.copy(DR_lin.reshape(N_segments + 1, 3).T)

        if bar:
            pbar.update(1)

        if bar:
            print("\n Total DeltaV for n=" + str(i) + ":\n")
            print(str(DV_opt[i]) + " m/s \n")
            if orbit_type == 'Halo2':
                print(np.linalg.norm(DV[3:6, 1:-1] * model.vs, axis=0).sum())

            else:
                print(np.linalg.norm(DV[:, 1:-1] * model.vs, axis=0).sum())

    if bar:
        pbar.close()
        print("\n")

    report_dict = {"Mission Time": tf/86400,
                   "Model": model.name,
                   "Segments": N_segments,
                   "n opt": opt_iterations,
                   "DV": DV_opt,
                   "Final DV": DV_opt[-1],
                   }

    return time, position, velocity, DV[:, 1:], DT, report_dict


def csta(time, ri, vi, frame_origin, frame_destination, frame_aux=None):
    """
    Coordinate System Transformation Algorithm

    Parameters
    ----------
    time : float, 1-D array
        Time in jd format
    ri : float, ndarray (3,n)
        Position in origin frame
    vi : float, ndarray (3,n)
        Velocity in origin frame
    frame_origin : frame class instance
        Origin frame
    frame_destination : frame class instance
        Destination frame
    frame_aux : IdealSynodic class instance
        P1-IdealSynodic frame for ideal-real transformations

    Returns
    -------
    rf : ndarray (3,n)
        Position in destination frame
    vf : ndarray (3,n)
        Velocity in destination frame
    """

    if (frame_origin.ftype == 'SynodicIdeal'):
        if (frame_destination.ftype == 'SynodicIdeal'):
            rf, vf = csta_ideal(time, ri, vi, frame_origin, frame_destination)
        else:
            if (frame_origin.origin.cetype == 'libration_point'):
                rf, vf = csta_real(time, ri, vi, frame_origin, frame_destination)
            else:
                r1, v1 = csta_ideal(time, ri, vi, frame_origin, frame_aux)
                rf, vf = csta_real(time, r1, v1, frame_aux, frame_destination)
    else:
        if (frame_destination.ftype == 'SynodicIdeal'):
            if (frame_destination.origin.cetype == 'libration_point'):
                rf, vf = csta_real(time, ri, vi, frame_origin, frame_destination)
            else:
                r1, v1 = csta_real(time, ri, vi, frame_origin, frame_aux)
                rf, vf = csta_ideal(time, r1, v1, frame_aux, frame_destination)
        else:
            rf, vf = csta_real(time, ri, vi, frame_origin, frame_destination)

    return rf, vf


def csta_real(time, ri, vi, frame_origin, frame_destination):
    """
    Coordinate System Transformation Algorithm

    Parameters
    ----------
    t : float, 1-D array
        time in jd format
    ri : float, ndarray (3,n)
        position in origin frame
    vi : float, ndarray (3,n)
        velocity in origin frame
    F1 : frame class instance
         origin frame
    F2 : frame class instance
         destination frame

    Returns
    -------
    rf : ndarray (3,n)
        position in destination frame
    vf : ndarray (3,n)
        velocity in destination frame
    """

    if frame_origin.ftype == 'FK5':
        r1 = ri
        v1 = vi
    else:
        r1 = np.einsum('ijk,jk->ik', frame_origin.R(time), ri)
        v1 = (np.einsum('ijk,jk->ik', frame_origin.Rp(time), ri)
              + np.einsum('ijk,jk->ik', frame_origin.R(time), vi))

    if frame_origin.origin.name == frame_destination.origin.name:
        r2 = r1
        v2 = v1
    else:
        r2 = r1 + (frame_origin.r_origin(time) - frame_destination.r_origin(time))
        v2 = v1 + (frame_origin.v_origin(time) - frame_destination.v_origin(time))

    if frame_destination.ftype == 'FK5':
        rf = r2
        vf = v2
    else:
        rf = np.einsum('ijk,jk->ik', frame_destination.R(time).transpose(1, 0, 2), r2)
        vf = (np.einsum('ijk,jk->ik', frame_destination.Rp(time).transpose(1, 0, 2), r2)
              + np.einsum('ijk,jk->ik', frame_destination.R(time).transpose(1, 0, 2), v2))

    return rf, vf


def csta_ideal(time, ri, vi, frame_origin, frame_destination):
    """
    Coordinate System Transformation Algorithm for transformations between
    IdealSynodic frames

    Parameters
    ----------
    t : float, 1-D array (n)
        time in jd format
    ri : float, ndarray (3,n)
        position in origin frame
    vi : float, ndarray (3,n)
        velocity in origin frame
    F1 : IdealSynodic class instance
         origin frame
    F2 : IdealSynodic class instance
         destination frame

    Returns
    -------
    rf : ndarray (3,n)
        position in destination frame
    vf : ndarray (3,n)
        velocity in destination frame
    """

    rf = ri + (frame_origin.r_origin(time, ideal=True) - frame_destination.r_origin(time, ideal=True))

    vf = vi

    return rf, vf
