import unittest
from mubody.core.ephemeris import Ephemeris
from requests import Response
from unittest import mock
import os
import numpy as np
from numpy.testing import assert_allclose


class EphemerisDryTest(unittest.TestCase):
    def setUp(self):
        # Set up any necessary resources or test data
        self.eph = Ephemeris(test=True)
        self.eph.kernels_list = ["test.bsp", "test.txt"]
        self.eph.url_dict["test.bsp"] = self.eph.url_dict["de405.bsp"]
        self.eph.url_dict["test.txt"] = self.eph.url_dict["naif0011.txt"]

    def test_get_body_ID_with_valid_name(self):
        # Test the get_body_ID method with a valid body name
        body_name = "Earth"
        expected_id = "399"  # NAIF ID for Earth

        # Call the method being tested
        actual_id = self.eph.get_body_ID(body_name)

        # Assert the expected result
        self.assertEqual(actual_id, expected_id)

    def test_get_body_ID_with_valid_id(self):
        # Test the get_body_ID method with a valid body ID
        body_id = "3"  # NAIF ID for Jupiter
        expected_id = "3"

        # Call the method being tested
        actual_id = self.eph.get_body_ID(body_id)

        # Assert the expected result
        self.assertEqual(actual_id, expected_id)

    def test_get_body_ID_with_invalid_name(self):
        # Test the get_body_ID method with an invalid body name
        body_name = "InvalidBodyName"

        # Call the method being tested and assert that it raises a ValueError
        with self.assertRaises(ValueError):
            self.eph.get_body_ID(body_name)

    def test_check_kernels_load_without_loaded_kernels(self):
        # Test the check_kernels_load method without loaded kernels

        # Call the method being tested
        result = self.eph.check_kernels_load()

        # Assert that the method returns False
        self.assertFalse(result)

    def test_check_kernels_files_without_files(self):
        # Test the check_kernels_files method without existing files

        # Call the method being tested
        result = self.eph.check_kernels_files()

        # Assert that the method returns False
        self.assertFalse(result)

    @mock.patch("os.makedirs")
    @mock.patch("requests.get")
    def test_download_kernels(self, mock_get, mock_makedirs):
        # Test the download_kernels method

        # Set up the mock return values
        mock_makedirs.return_value = None
        mock_get.return_value = MockResponse(
            custom_content=b"Keep moving, nothing to see here"
        )

        # Call the method being tested
        result = self.eph.download_kernels()
        for file in self.eph.kernels_list:
            os.remove(self.eph.kernels_folder_path + file)

        # Assert that the method returns 0
        self.assertEqual(result, 0)

    def test_check_kernels_load_with_loaded_kernels(self):
        # Test the check_kernels_load method with loaded kernels
        self.eph.kernels_list = ["de405.bsp", "naif0011.txt"]
        self.eph.url_dict = {
            "de405.bsp": "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de405.bsp",  # noqa
            "naif0011.txt": "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0011.tls",
        }
        # Load the kernels
        self.eph.load_kernels()

        # Call the method being tested
        result = self.eph.check_kernels_load()

        # Assert that the method returns 0
        self.assertEqual(result, 0)


class EphemerisTest(unittest.TestCase):
    def setUp(self):
        # Set up any necessary resources or test data
        self.eph = Ephemeris()

    def test_get_spice_eph(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        states = self.eph.get_spice_eph(self.eph.epoch, body, time, self.eph.reference)

        # Reference result
        states_reference = np.array(
            [
                [-2.64990342e07, -2.64990640e07, -2.64990938e07],
                [1.32757418e08, 1.32757413e08, 1.32757408e08],
                [5.75567174e07, 5.75567153e07, 5.75567131e07],
                [-2.97942600e01, -2.97942590e01, -2.97942579e01],
                [-5.01805246e00, -5.01805801e00, -5.01806357e00],
                [-2.17539373e00, -2.17539613e00, -2.17539854e00],
            ]
        )

        # print(np.array2string(result, separator=","))
        assert_allclose(states, states_reference)

    def test_get_eph_r_sp(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        r = self.eph.get_eph_r_sp(self.eph.epoch, body, time, self.eph.reference)

        # Reference result
        r_reference = np.array(
            [
                [-2.64990342e07, -2.64990640e07, -2.64990938e07],
                [1.32757418e08, 1.32757413e08, 1.32757408e08],
                [5.75567174e07, 5.75567153e07, 5.75567131e07],
            ]
        )

        assert_allclose(r, r_reference)

    def test_get_eph_v_sp(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        v = self.eph.get_eph_v_sp(self.eph.epoch, body, time, self.eph.reference)

        # Reference result
        v_reference = np.array(
            [
                [-2.97942600e01, -2.97942590e01, -2.97942579e01],
                [-5.01805246e00, -5.01805801e00, -5.01806357e00],
                [-2.17539373e00, -2.17539613e00, -2.17539854e00],
            ]
        )

        assert_allclose(v, v_reference)

    def test_r_sp(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        r = self.eph.r_sp(body, time)

        # Reference result
        r_reference = np.array(
            [
                [-2.64990342e07, -2.64990640e07, -2.64990938e07],
                [1.32757418e08, 1.32757413e08, 1.32757408e08],
                [5.75567174e07, 5.75567153e07, 5.75567131e07],
            ]
        )

        assert_allclose(r, r_reference)

    def test_v_sp(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        v = self.eph.v_sp(body, time)

        # Reference result
        v_reference = np.array(
            [
                [-2.97942600e01, -2.97942590e01, -2.97942579e01],
                [-5.01805246e00, -5.01805801e00, -5.01806357e00],
                [-2.17539373e00, -2.17539613e00, -2.17539854e00],
            ]
        )

        assert_allclose(v, v_reference)

    def test_get_eph_r(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        r = self.eph.get_eph_r(self.eph.epoch, body, time, self.eph.reference)

        # Reference result
        r_reference = np.array(
            [
                [-2.64990342e07, -2.64990640e07, -2.64990938e07],
                [1.32757418e08, 1.32757413e08, 1.32757408e08],
                [5.75567174e07, 5.75567153e07, 5.75567131e07],
            ]
        )

        assert_allclose(r, r_reference)

    def test_get_eph_v(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        v = self.eph.get_eph_v_sp(self.eph.epoch, body, time, self.eph.reference)

        # Reference result
        v_reference = np.array(
            [
                [-2.97942600e01, -2.97942590e01, -2.97942579e01],
                [-5.01805246e00, -5.01805801e00, -5.01806357e00],
                [-2.17539373e00, -2.17539613e00, -2.17539854e00],
            ]
        )

        assert_allclose(v, v_reference)

    def test_r(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        r = self.eph.r(body, time)

        # Reference result
        r_reference = np.array(
            [
                [-2.64990342e07, -2.64990640e07, -2.64990938e07],
                [1.32757418e08, 1.32757413e08, 1.32757408e08],
                [5.75567174e07, 5.75567153e07, 5.75567131e07],
            ]
        )

        assert_allclose(r, r_reference)

    def test_v(self):
        # Define test inputs
        body = "Earth"
        time = np.array([0, 1, 2])

        # Call the method to test
        v = self.eph.v(body, time)

        # Reference result
        v_reference = np.array(
            [
                [-2.97942600e01, -2.97942590e01, -2.97942579e01],
                [-5.01805246e00, -5.01805801e00, -5.01806357e00],
                [-2.17539373e00, -2.17539613e00, -2.17539854e00],
            ]
        )

        assert_allclose(v, v_reference)


# MockResponse class for mocking requests.get
class MockResponse(Response):
    def __init__(self, custom_content):
        super().__init__()
        self.custom_content = custom_content

    @property
    def custom_content(self):
        return self._content

    @custom_content.setter
    def custom_content(self, value):
        self._content = value


# Run the tests
if __name__ == "__main__":
    unittest.main()
