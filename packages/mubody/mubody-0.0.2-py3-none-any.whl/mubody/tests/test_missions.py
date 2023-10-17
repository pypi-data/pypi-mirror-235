from mubody.mission import Mission
import numpy.testing as npt
import numpy as np


def test_analytical_CRTBP():
    """
    Test analytical orbit generation
    """

    test_mission = Mission()

    result = test_mission.AO(bar=False)

    assert result == 0


def test_IC_propagation_CRTBP():
    """
    Test propagation from initial condition
    """

    test_mission = Mission(mission_time=10*24*3600)

    result = test_mission.IC(bar=False)

    assert result == 0


def test_ETM_CRTBP():
    """
    Test equiting target method (ETM) for Lissajous and Halo orbits
    """

    test_mission_Lissajous = Mission(mission_time=120*24*3600)
    test_mission_Halo = Mission(mission_time=120*24*3600, orbit='Halo', method='Howell')

    result_Lissajous = test_mission_Lissajous.ETM(bar=False)
    result_Halo = test_mission_Halo.ETM(bar=False)

    assert result_Lissajous == 0
    assert result_Halo == 0


def test_OTM_CRTBP():
    """
    Test optimized targeting method (OTM) for Lissajous and Halo orbits
    """

    test_mission_Liss = Mission(mission_time=120*24*3600)
    # test_mission_Halo = Mission(mission_time=120*24*3600, orbit='Halo')

    result_Lissajous = test_mission_Liss.OTM(N_segments=4, bar=False)
    # result_Halo = test_mission_Halo.OTM(opt_iterations=1, bar=False)

    DV_Lissajous = np.linalg.norm(test_mission_Liss.sat.DV, axis=0).sum() * test_mission_Liss.DS.models['CRTBP'].vs

    assert result_Lissajous == 0
    # assert result_Halo == 0
    assert DV_Lissajous < 1


def test_targeting_method_CRTBP():
    """
    Check that first OTM iteration returns same DV as ETM
    """

    test_mission_a = Mission(mission_time=120*24*3600)

    test_mission_a.ETM(bar=False)

    DV_a = test_mission_a.report_dict['DV']

    test_mission_b = Mission(mission_time=120*24*3600)

    test_mission_b.OTM(bar=False, N_segments=4, opt_iterations=0)

    DV_b = test_mission_b.report_dict['DV'][-1]

    npt.assert_almost_equal(DV_a, DV_b, decimal=3)


def test_IC_propagation_FETBP():
    """
    Test propagation from initial condition with FETBP
    """

    test_mission = Mission(mission_time=10*24*3600)

    result = test_mission.IC(model="FETBP", bar=False)

    assert result == 0


def test_ETM_FETBP():
    """
    Test equiting target method (ETM) with FETBP
    """

    test_mission = Mission(mission_time=120*24*3600)

    result = test_mission.ETM(model="FETBP", bar=False)

    assert result == 0


def test_OTM_FETBP():
    """
    Test optimized targeting method (OTM) with FETBP
    """

    test_mission = Mission(mission_time=120*24*3600)

    result = test_mission.OTM(model="FETBP", N_segments=4, bar=False)

    DV = np.linalg.norm(test_mission.sat.DV, axis=0).sum()

    assert result == 0
    assert DV < 1
