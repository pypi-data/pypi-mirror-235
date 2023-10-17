import unittest

import numpy as np
from numpy.testing import assert_allclose
from mubody.core.kepler import Bm, DeltaV_fb, lambert, reqins, rocket_eq, rocket_eq_mi


class KeplerTest(unittest.TestCase):
    def test_Bm(self):
        rper = 10000  # Perigee radius [km]
        Vinf = 10  # Hyperbolic excess of velocity [km/s]
        mu = 398600  # Earth's standard gravitational parameter [km^3/s^2]
        expected_result = 13405.9688  # Expected Bmod value [km]
        result = Bm(rper, Vinf, mu)

        assert_allclose(
            result,
            expected_result,
        )

    def test_DeltaV_fb(self):
        rper = 10000  # Perigee radius [km]
        Vinf = 12  # Hyperbolic excess of velocity [km/s]
        mu = 398600  # Earth's standard gravitational parameter [km^3/s^2]
        expected_result = 5.20309  # Expected DeltaV value [km/s]
        result = DeltaV_fb(rper, Vinf, mu)

        assert_allclose(result, expected_result, rtol=1e-12, atol=1e-6)

    def test_rocket_eq(self):
        Isp = 300  # Engine specific impulse [s]
        mi = 2000  # Initial mass (m0 + mp) [kg]
        mf = 1000  # Final mass after burn (m0) [kg]
        expected_result = 2.039932  # Expected DeltaV value [km/s]
        result = rocket_eq(Isp, mi, mf)

        assert_allclose(result, expected_result)

    def test_rocket_eq_mi(self):
        Isp = 300  # Engine specific impulse [s]
        DV = 2.5  # Delta-v performed [km/s]
        mf = 1000  # Final mass after burn (m0) [kg]
        expected_result = 2338.41494  # Expected initial mass (m0 + mp) [kg]
        result = rocket_eq_mi(Isp, DV, mf)

        assert_allclose(result, expected_result)

    def test_reqins(self):
        Isp = 300  # Engine specific impulse [s]
        DV = [1.2, 2.5, 1.7]  # Delta-v performed [km/s]
        mf = 1000  # Final mass after burn (m0) [kg]
        expected_result = [
            6264.27203,
            3515.636266,
            1503.427042,
            1000.0,
        ]  # Expected initial mass (m0 + mp) [kg]
        result = reqins(Isp, DV, mf)

        assert_allclose(result, expected_result)

    def test_lambert(self):
        r1 = 150e6  # Semi-major axis of departure planet [km]
        r2 = 250e6  # Semi-major axis of arrival planet [km]
        alpha = 1.2 * np.pi / 2  # Angle between r1 and r2 vectors [rad]
        TOF = 180  # Time of flight [days]
        expected_a = 195.449504942e6  # Expected semi-major axis of transfer orbit [km]
        expected_e = 0.3068124  # Expected eccentricity of transfer orbit [-]
        expected_nu = 0.942474626  # Expected TA of departure [rad]
        result_a, result_e, result_nu = lambert(r1, r2, alpha, TOF)

        assert_allclose(result_a, expected_a)
        assert_allclose(result_e, expected_e)
        assert_allclose(result_nu, expected_nu)


if __name__ == "__main__":
    unittest.main()
