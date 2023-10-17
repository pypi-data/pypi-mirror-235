from astropy.time import Time

# File with astronomic constants
# All must be referenced
# All must be in IS units
# Angles in degrees

# physical constants
# https://ssd.jpl.nasa.gov/planets/phys_par.html

# orbital elements
# https://ssd.jpl.nasa.gov/sats/elem/
# Explanatory supplement to the Astronomical almanac: a revision to the
# Explanatory supplement to the astronomical ephemeris and the American
# ephemeris and nautical almanac


J2000_epoch = Time('2000-01-01 11:58:55.816', format='iso', scale='utc')

SolarSystemPlanets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

"""Dictionary"""
names_dict = {'Earth': 'earth',
              'Moon': 'moon',
              'Sun': 'sun',
              'Saturn': 'saturn',
              'Jupiter': 'j',
              'Venus': 'venus',
              'Mars': 'mars',
              'Mercury': 'mercury',
              'Neptune': 'neptune',
              'Uranus': 'uranus',
              'EM': 'em'
              }

# id_dict = {
#     'Earth': '399',
#     'Sun': '10',
#     'Moon': '301',
#     'Jupiter': '599',
#     'Saturn': '699',
#     'Venus': '2',
#     'Mars': '4',
#     'Mercury': '1',
#     'Uranus': '7',
#     'Neptune': '8',
#     'EM': '3'
#     }

id_dict = {'earth': '399',
           'sun': '10',
           'Luna': '301',
           'jupiter': '5',
           'saturn': '6',
           'venus': '2',
           'mars': '4',
           'mercury': '1',
           'uranus': '7',
           'neptune': '8',
           'earth-moon': '3',
           'L2': '392'
           }

id_dict_V2 = {'SSB': 0,
              'Sun': '10',
              'Mercury': '1',
              'Venus': '2',
              'Earth': '399',
              'Luna': '301',
              'Mars': '4',
              'Phobos': '401',
              'Deimos': '402',
              'Jupiter': '5',
              'Io': '501',
              'Europa': '502',
              'Ganymede': '503',
              'Callisto': '504',
              'Saturn': '6',
              'Uranus': '7',
              'Neptune': '8',
              'Pluto': '9',
              'L2': '392'
              }

naif_names_ids = id_dict_V2

planets_list = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]

moons_list = ["moon", "europa"]

"""General"""
G = 6.674e-11

J2000 = 2451545.0

equinox_date_2000 = 2455275.60764

sun_dict = {"name": "Sun",
            "type": "star",
            "id": "10",
            "mass": 1.9891e30,
            "radius": 6.69e8,
            "sma": 0,
            "planets": SolarSystemPlanets
            }

mercury_dict = {"name": "Mercury",
                "type": "planet",
                "id": "199",
                "mass": 3.33022e23,
                "radius": 2439.7e3,
                "moons": None,
                "central_body": "Sun",
                "frame": "Ecliptic",
                "sma": 5.7909083e10,
                "ecc": 0.205631752914,
                "inc": 7.004986253
                }

venus_dict = {"name": "Venus",
              "type": "planet",
              "id": "299",
              "mass": 5.9723e24,
              "radius": 6051.9e3,
              "moons": None,
              "central_body": "Sun",
              "frame": "Ecliptic",
              "sma": 1.08208601e11,
              "ecc": 0.0067718819142,
              "inc": 3.394466189
              }

earth_dict = {"name": "Earth",
              "type": "planet",
              "id": "399",
              "mass": 5.9721e24,
              "radius": 6378.14e3,
              "moons": ["Luna"],
              "central_body": "Sun",
              "frame": "Ecliptic",
              "sma": 1.49598023e11,
              "ecc": 0.016708617154,
              "inc": 0.
              }

# SSD JPL
luna_dict = {"name": "Luna",
             "type": "moon",
             "id": "301",
             "mass": 7.344777e22,  # mu/G
             "radius": 1737.4e3,  # mean
             "central_body": "Earth",
             "frame": "-",
             "sma": 3.844e8,
             "ecc": 0.0544,
             "inc": 5.16
             }

mars_dict = {"name": "Mars",
             "type": "planet",
             "id": "499",
             "mass": 6.4191e23,
             "radius": 3397e3,
             "moons": None,  # ["Phobos", "Deimos"],
             "central_body": "Sun",
             "frame": "Ecliptic",
             "sma": 2.27939186e11,
             "ecc": 0.0934006199474,
             "inc": 1.849726478
             }

# SSD JPL
phobos_dict = {"name": "Phobos",
               "type": "moon",
               "id": "401",
               "mass": 1.06077e16,  # mu/G
               "radius": 11.08e3,  # mean
               "central_body": "Mars",
               "frame": "Laplace",
               "sma": 9400e3,
               "ecc": 0.015,
               "inc": 1.1
               }

# SSD JPL
deimos_dict = {"name": "Deimos",
               "type": "moon",
               "id": "402",
               "mass": 1.441738479e15,  # mu/G
               "radius": 6.2e3,  # mean
               "central_body": "Mars",
               "frame": "Laplace",
               "sma": 2.35e7,
               "ecc": 0.,
               "inc": 1.8
               }

jupiter_dict = {"name": "Jupiter",
                "type": "planet",
                "id": "599",
                "mass": 1.8988e27,
                "radius": 71492e3,
                "moons": None,  # ["Io", "Europa", "Ganymede", "Callisto"],
                "central_body": "Sun",
                "frame": "Ecliptic",
                "sma": 7.78298361e11,
                "ecc": 0.0484948512199,
                "inc": 1.303269664
                }

# SSD JPL
io_dict = {"name": "Io",
           "type": "moon",
           "id": "501",
           "mass": 8.932056171e22,  # mu/G
           "radius": 1821.49e3,  # mean
           "central_body": "Jupiter",
           "frame": "Laplace",
           "sma": 4.218e8,
           "ecc": 0.004,
           "inc": 0.
           }

# SSD JPL
europa_dict = {"name": "Europa",
               "type": "moon",
               "id": "502",
               "mass": 4.7799867366e22,  # mu/G
               "radius": 1.5608e8,  # mean
               "central_body": "Jupiter",
               "frame": "Ecliptic",
               "sma": 6.711e8,
               "ecc": 0.009,
               "inc": 0.5
               }

# SSD JPL
ganymede_dict = {"name": "Ganymede",
                 "type": "moon",
                 "id": "503",
                 "mass": 1.481878708e23,  # mu/G
                 "radius": 2.6312e8,  # mean
                 "central_body": "Jupiter",
                 "frame": "Ecliptic",
                 "sma": 1.0704e9,
                 "ecc": 0.001,
                 "inc": 0.2
                 }

# SSD JPL
callisto_dict = {"name": "Callisto",
                 "type": "moon",
                 "id": "504",
                 "mass": 1.075951365e23,  # mu/G
                 "radius": 2.4103e3,  # mean
                 "central_body": "Jupiter",
                 "frame": "Ecliptic",
                 "sma": 1.8827e9,
                 "ecc": 0.007,
                 "inc": 0.3
                 }

saturn_dict = {"name": "Saturn",
               "type": "planet",
               "id": "699",
               "mass": 5.685e26,
               "radius": 60268e3,
               "moons": None,
               "central_body": "Sun",
               "frame": "Ecliptic",
               "sma": 14.29394133e11,
               "ecc": 0.0555086217172,
               "inc": 2.488878097
               }

uranus_dict = {"name": "Uranus",
               "type": "planet",
               "id": "799",
               "mass": 8.6625e25,
               "radius": 25559e3,
               "moons": None,
               "central_body": "Sun",
               "frame": "Ecliptic",
               "sma": 28.75038615e11,
               "ecc": 0.0462958985125,
               "inc": 0.7731961694
               }

neptune_dict = {"name": "Neptune",
                "type": "planet",
                "id": "899",
                "mass": 1.0278e26,
                "radius": 24764e3,
                "moons": None,
                "central_body": "Sun",
                "frame": "Ecliptic",
                "sma": 45.04449769,
                "ecc": 0.0089880948652,
                "inc": 1.769952208
                }

pluto_dict = {"name": "Pluto",
              "type": "planet",
              "id": "999",
              "mass": 1.5e22,
              "radius": 1151e3,
              "moons": None,
              "central_body": "Sun",
              "frame": "Ecliptic",
              "sma": 59.15799e11,
              "ecc": 0.249050,
              "inc": 17.14216667
              }

SolarSystemPlanets_dict = {"Mercury": mercury_dict,
                           "Venus": venus_dict,
                           "Earth": earth_dict,
                           "Mars": mars_dict,
                           "Jupiter": jupiter_dict,
                           "Saturn": saturn_dict,
                           "Uranus": uranus_dict,
                           "Neptune": neptune_dict,
                           "Pluto": pluto_dict
                           }

SolarSystemMoons_dict = {"Luna": luna_dict}

# SolarSystemMoons_dict = {"Luna": luna_dict,
#                          "Phobos": phobos_dict,
#                          "Deimos": deimos_dict,
#                          "Io": io_dict,
#                          "Europa": europa_dict,
#                          "Ganymede": ganymede_dict,
#                          "Callisto": callisto_dict
#                          }

SolarSystemBodies_list = (list(SolarSystemPlanets_dict.keys())
                          + list(SolarSystemMoons_dict.keys())
                          + ['Sun'])

# Eccentricity
# Patter and Lissauer
e_e = 0.016708617

# Werz
AU = 149597870660

# NASA Goddard Space Flight Center David Williams
m_earth = 5.9723e24
m_earth = 398600.4415e9/G

# NASA Goddard Space Flight Center David Williams
# mean radius
R_earth = 6371e3

# NASA Goddard Space Flight Center David Williams
J2 = 1082.63e-6

# NASA Goddard Space Flight Center David Williams
# a_e = 149451940331.77
sma_earth = 149181538551.12744

# NASA Goddard Space Flight Center David Williams
i_e = 0

"""Moon"""
# Fhorbani and assadian
sma_moon = 381055426

# Eccentricity
# Fhorbani and assadian
e_moon = 0.033544
R_moon = 60e6
# Fhorbani and assadian
i_m = 5.04246

m_moon = 7.34e22
m_moon = 4902.8005821478e9/G

"""EM"""
# m_earth-moon = m_moon + m_earth
# a_em = a_e = 149181538551.12744

"""Sun"""

# NASA Goddard Space Flight Center David Williams
m_sun = 1.988500e30
m_sun = 132712440017.99e9/G
R_sun = 696340e3  # [m]
sma_sun = 500

"""Jupiter"""
m_jupiter = 1.89e27

mu_jupiter = 1.266e17

R_jupiter = 69.9e6

sma_jupiter = 1

"""Saturn"""

R_saturn = 58e6

m_saturn = 5.68e26

mu_saturn = 3.793e16
sma_saturn = 500e9
r_SOI_s = 54.6e9

"""Mars"""
m_mars = 6.39e23
R_mars = 5400e3
sma_mars = 250e9

"""Venus"""
m_venus = 4.867e24
R_venus = 6400e3
sma_venus = 100e9
"""Mercury"""
m_mercury = 3.285e23

"""Neptune"""
m_neptune = 1.024e26

"""Uranus"""
m_uranus = 8.681e25

# Solar pressure at Earth distance, obtained dividing solar irradiance by light speed
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
SOLAR_PRESSURE = 1361.0/299792458  # [N/m2]

# AU value comes from: The Planetary and Lunar Ephemeris DE430 and DE431
# https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf
# Mars high resolution gravity fields from MRO, Mars seasonal gravity, and other dynamical
# parameters
# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.454.8581&rep=rep1&type=pdf
AU = 149597870700  # [m]

# Gravity acceleration at Earth's surface
g0 = 9.81  # [m/s2]
