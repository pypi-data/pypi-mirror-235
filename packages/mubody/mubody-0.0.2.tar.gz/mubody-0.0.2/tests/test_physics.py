from mubody.mission import Mission
import mubody.constants as cte
import mubody.core.physic as phy
import mubody.numeric as nm
import numpy as np


def test_gravity_law():
    g_gravity = np.around(phy.gravity_law(cte.m_earth, np.array([[0], [0], [6371e3]]))[2, 0], decimals=1)
    result_0 = np.isclose(g_gravity, -9.8)

    m = 1

    r = np.random.random((3, 2))

    g = phy.gravity_law(m, r)

    a = r[:, [0]]
    b = r[:, [1]]

    g1 = cte.G * b/np.linalg.norm(b)**3

    g2 = cte.G * a/np.linalg.norm(a)**3

    result_1 = np.isclose(np.linalg.norm(g1), np.linalg.norm(g[:, 0]))
    result_2 = np.isclose(np.linalg.norm(g2), np.linalg.norm(g[:, 1]))

    assert result_0 * result_1 * result_2


def test_gravity_jacobian():
    tf = 5400

    mission_test = Mission(mission_time=tf)

    phi0 = np.eye(6)

    model = mission_test.DS.models['FETBP']

    r_earth = mission_test.DS.ss.Earth.r(0)
    v_earth = mission_test.DS.ss.Earth.v(0)

    state0 = np.array([0, 0, 6771e3, 7670, 0, 0]).reshape(-1, 1) + np.concatenate((r_earth, v_earth), axis=0)
    delta = np.zeros((6, 1))
    delta[0:3] = np.random.random((3, 1)) * 50
    statep = state0
    statep[0:3] = state0[0:3] + delta[0:3]

    times, states = nm.integrator(model.F, 0, tf, state0.flatten(), 10, 1)
    statef = states[:, [-1]]

    model.add_trajectory(times, states[0:3])

    _, statesp = nm.integrator(model.F, 0, tf, statep.flatten(), 10, 1)
    statepf = statesp[:, [-1]]

    _, phi_segments = nm.integrator(model.phi_dot_vec, 0, tf, phi0.flatten('F'), 10, 1, tols=(1e-11, 1e-11))

    phi = phi_segments[:, -1].reshape(6, 6, order='F').reshape(6, 6, 1).squeeze()

    result = 100 * np.linalg.norm((statepf - (statef + phi @ delta))/statepf) < 0.5

    assert result
