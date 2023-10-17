import requests
import warnings
import pandas as pd


def jpl_periodic_orbits_catalog(family_parameters):
    """
    This function articulates the operations needed to retrieve the JPL Periodic Orbits
    from CRTBP catalog

    Parameters
    ----------
    family_parameters : dict
        Selection criteria

    Returns
    -------
    orbit_family : pandas DataFrame
        Normalized initial conditions of selected periodic orbits (P1-IdealSynodic)

    References
    ----------
    .. [1] JPL https://ssd.jpl.nasa.gov/tools/periodic_orbits.html#/periodic
    """

    query_url = create_jpl_poc_query(family_parameters)

    catalog = request_catalog(query_url)

    orbit_family = process_catalog(catalog)

    return orbit_family


def create_jpl_poc_query(family_parameters):
    """
    Creates query JPL Periodic Orbit Catalog from provided parameters in mubody format

    Parameters
    ----------
    family_parameters : dict
        Selection criteria

    Returns
    -------
    query_url : string
        Query for JPL API

    References
    ----------
    .. [1] JPL https://ssd-api.jpl.nasa.gov/doc/periodic_orbits.html
    """

    query_parameters_equivalence = {
        "system": "sys",
        "orbit_type": "family",
        "libration_point": "libr",
        "branch": "branch",
        "periodmin": "periodmin",
        "periodmax": "periodmax",
        "periodunits": "periodunits",
        "jacobimin": "jacobmin",
        "jacobimax": "jacobimax",
        "stabmin": "stabmin",
        "stabmax": "stabmax",
    }

    base_url = "https://ssd-api.jpl.nasa.gov/periodic_orbits.api?"

    query_parameters = [
        str(query_parameters_equivalence[key]) + "=" + str(values)
        for key, values in family_parameters.items()
    ]
    query_url = base_url + "&".join(query_parameters)

    return query_url


def request_catalog(query_url):
    """
    Sends request to JPL Periodic Orbit Catalog server and receives
    response

    Parameters
    ----------
    query_url : string
        Query for JPL API

    Returns
    -------
    catalog : dict
        Catalog of orbits

    References
    ----------
    .. [1] JPL https://ssd-api.jpl.nasa.gov/doc/periodic_orbits.html
    """

    response_codes = {
        200: "OK",
        400: "Bad Request: the request contained invalid keywords and/or content "
        "(details returned in the JSON payload)",
        405: "Method Not Allowed: the request used an incorrect method (see the HTTP "
        "Request section)",
        500: "Internal Server Error: the database is not available at the time of "
        "request",
        503: "Service Unavailable: the server is currently unable to handle the "
        "request due to a temporary overloading or  maintenance of the server, which "
        "will likely be alleviated after some delay",
    }

    response = requests.get(query_url)

    if response.status_code == 200:
        catalog = dict(response.json())
        if catalog["count"] == '0':
            print("No orbits were founds based on the requested parameters")

    else:
        raise ValueError(response_codes[response.status_code], response.content)

    return catalog


def process_catalog(catalog):
    """
    Converts the JPL Periodic Orbit Catalog into a pandas DataFrame

    Parameters
    ----------
    catalog : dict
        Catalog of orbits

    Returns
    -------
    orbit_family : pandas DataFrame
        Normalized initial conditions of selected periodic orbits (P1-IdealSynodic)

    References
    ----------
    .. [1] JPL https://ssd-api.jpl.nasa.gov/doc/periodic_orbits.html
    """

    if catalog["signature"]["version"] != "1.0":
        warnings.warn("API version different from expected, format may have changed")

    orbit_family = pd.DataFrame(data=catalog["data"], columns=catalog["fields"], dtype=float)

    return orbit_family
