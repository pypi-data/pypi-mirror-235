from mubody.utilities.external_apis import (
    create_jpl_poc_query,
    request_catalog,
    process_catalog,
)
from numpy.testing import assert_allclose
import numpy as np


def test_create_jpl_poc_query():
    query_url_reference = "https://ssd-api.jpl.nasa.gov/periodic_orbits.api?sys=earth-moon&family=halo&libr=2&branch=N"

    family_parameters = {
        "system": "earth-moon",
        "orbit_type": "halo",
        "libration_point": "2",
        "branch": "N",
    }

    query_url = create_jpl_poc_query(family_parameters)

    assert query_url == query_url_reference


def test_request_catalog():
    query_url = "https://ssd-api.jpl.nasa.gov/periodic_orbits.api?sys=earth-moon&family=halo&libr=2&branch=N"

    catalog = request_catalog(query_url)

    # number of orbits returned for the given query
    assert catalog["count"] == "1535"


def test_process_catalog():
    query_url = "https://ssd-api.jpl.nasa.gov/periodic_orbits.api?sys=earth-moon&family=halo&libr=2&branch=N"

    # first orbit of the catalog for the given query
    orbit_reference = np.array(
        [
            1.08295518e00,
            0.00000000e00,
            2.02317446e-01,
            9.78887918e-15,
            -2.01026449e-01,
            -2.47448665e-14,
            3.01517767e00,
            2.38349101e00,
            1.01524697e00,
        ]
    )

    catalog = request_catalog(query_url)

    orbit = process_catalog(catalog).iloc[0].values

    assert_allclose(orbit, orbit_reference)
