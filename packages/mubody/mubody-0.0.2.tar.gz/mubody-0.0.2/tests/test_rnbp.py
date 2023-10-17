from mubody.core.rnbp import libration_point
from mubody.mission import Mission
import numpy as np
from math import sqrt


def test_libration_point_location_primary_123():

    '''
    Tests the location_primary function for L1, L2 and L3, which calculates the libration points distance to the
    nearest primary.

    Reference:
        - Results checked by knowing real Lagrangian points' positions in the Sun-Earth system.
          ESA article: https://sci.esa.int/web/planck/-/30983-orbit-navigation
    '''

    test_mission = Mission(mission_time=10*24*3600)

    Sun = test_mission.DS.ss.star
    Earth = test_mission.DS.ss.Earth

    L1 = libration_point(Sun, Earth, 1)
    L2 = libration_point(Sun, Earth, 2)
    L3 = libration_point(Sun, Earth, 3)

    gammax1, gammay1 = L1.location_primary()
    gammax2, gammay2 = L2.location_primary()
    gammax3, gammay3 = L3.location_primary()

    resultx1 = np.isclose(gammax1, 0.01, atol=1e-4)
    resulty1 = gammay1
    resultx2 = np.isclose(gammax2, 0.01, atol=1e-4)
    resulty2 = gammay2
    resultx3 = np.isclose(gammax3, 0.999998, atol=1e-4)
    resulty3 = gammay3
    assert resultx1 == 1
    assert resultx2 == 1
    assert resultx3 == 1
    assert resulty1 + resulty2 + resulty3 == 0


def test_libration_point_location_primary_45():

    '''
    Tests the location_primary function for L4 and L5, which calculates the libration points distance to the
    nearest primary.

    Reference:
        - GMATMathSpec, page 77.
    '''

    test_mission = Mission(mission_time=10*24*3600)

    Sun = test_mission.DS.ss.star
    Earth = test_mission.DS.ss.Earth

    L4 = libration_point(Sun, Earth, 4)
    L5 = libration_point(Sun, Earth, 5)

    gammax4, gammay4 = L4.location_primary()
    gammax5, gammay5 = L5.location_primary()

    resultx4 = np.isclose(gammax4, 1/2)
    resulty4 = np.isclose(gammay4, sqrt(3) / 2)

    assert resultx4 == 1
    assert resulty4 == 1
    assert gammax5 == gammax4
    assert gammay5 == gammay4


def test_libration_point_location_CoM():
    '''
    Tests the location_CoM function, which calculates the libration points location with respect to the CoM
    of the primaries.

    Reference:
        - GMATMathSpec, page 77.
    '''

    test_mission = Mission(mission_time=10*24*3600)

    Sun = test_mission.DS.ss.star
    Earth = test_mission.DS.ss.Earth

    L1 = libration_point(Sun, Earth, 1)
    L2 = libration_point(Sun, Earth, 2)
    L3 = libration_point(Sun, Earth, 3)
    L4 = libration_point(Sun, Earth, 4)
    L5 = libration_point(Sun, Earth, 5)

    gammax1, gammay1 = L1.location_primary()
    gammax2, gammay2 = L2.location_primary()
    gammax3, gammay3 = L3.location_primary()
    gammax4, gammay4 = L4.location_primary()
    gammax5, gammay5 = L5.location_primary()

    x1, y1 = L1.location_CoM()
    x2, y2 = L2.location_CoM()
    x3, y3 = L3.location_CoM()
    x4, y4 = L4.location_CoM()
    x5, y5 = L5.location_CoM()

    resultx1 = np.isclose(x1, 1 - L1.mu - gammax1)
    resulty1 = y1
    resultx2 = np.isclose(x2, 1 - L1.mu + gammax2)
    resulty2 = y2
    resultx3 = np.isclose(x3, - (gammax3 + L3.mu))
    resulty3 = y3
    resultx4 = np.isclose(x4, gammax4 - L4.mu)
    resulty4 = y4
    resultx5 = np.isclose(x5, gammax5 - L5.mu)
    resulty5 = y5

    assert resultx1 == 1
    assert resultx2 == 1
    assert resultx3 == 1
    assert resulty1 + resulty2 + resulty3 == 0
    assert resultx4 == 1
    assert resultx5 == 1
    assert resulty4 == gammay4
    assert resulty5 == - gammay5


def test_plot_libration_points():
    """
    Tests function that plots the primaries, their orbits and the five libration points' locations runs.
    """

    test_mission = Mission(mission_time=10*24*3600)

    Sun = test_mission.DS.ss.star
    Earth = test_mission.DS.ss.Earth

    L1 = libration_point(Sun, Earth, 1)
    L2 = libration_point(Sun, Earth, 2)
    L3 = libration_point(Sun, Earth, 3)
    L4 = libration_point(Sun, Earth, 4)
    L5 = libration_point(Sun, Earth, 5)

    x1, y1 = L1.location_CoM()
    x2, y2 = L2.location_CoM()
    x3, y3 = L3.location_CoM()
    x4, y4 = L4.location_CoM()
    x5, y5 = L5.location_CoM()

    positions = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]

    result = L1.plot_libration_points(positions)

    assert result == 0
