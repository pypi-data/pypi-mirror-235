import numpy as np


def Cx(theta):
    """
    Coordinate rotation around X-axis.

    This matrix transforms the coordinates of a vector from a reference system (S1) to a
    rotated one (S2) (u2 = C @ u1). S2 is obtained rotating S1 an angle theta around X-axis.

    Parameters
    ----------
    theta : float
        Rotated angle (rad).

    Returns
    -------
    C : ndarray (3,3)
        Coordinate rotation matrix around X-axis.

    References
    ----------
    .. [1] Diebel, J. (2006). Representing attitude: Euler angles,
           unit quaternions, and rotation vectors. Matrix, 58(15-16), 1-35.
    """

    C = np.array(
        [
            [1, 0, 0],
            [0, np.cos(theta), np.sin(theta)],
            [0, -np.sin(theta), np.cos(theta)],
        ]
    )

    return C


def Cy(theta):
    """
    Coordinate rotation around Y-axis.

    This matrix transforms the coordinates of a vector from a reference system (S1) to a
    rotated one (S2) (u2 = C @ u1). S2 is obtained rotating S1 an angle theta around Y-axis.

    Parameters
    ----------
    theta : float
        Rotated angle (rad).

    Returns
    -------
    C : ndarray (3,3)
        Coordinate rotation matrix around Y-axis.

    References
    ----------
    .. [1] Diebel, J. (2006). Representing attitude: Euler angles,
           unit quaternions, and rotation vectors. Matrix, 58(15-16), 1-35.
    """

    C = np.array(
        [
            [np.cos(theta), 0, -np.sin(theta)],
            [0, 1, 0],
            [np.sin(theta), 0, np.cos(theta)],
        ]
    )

    return C


def Cz(theta):
    """
    Coordinate rotation around Z-axis.

    This matrix transforms the coordinates of a vector from a reference system (S1) to a
    rotated one (S2) (u2 = C @ u1). S2 is obtained rotating S1 an angle theta around Z-axis.

    Parameters
    ----------
    theta : float
        Rotated angle (rad).

    Returns
    -------
    C : ndarray (3,3)
        Coordinate rotation matrix around Z-axis.

    References
    ----------
    .. [1] Diebel, J. (2006). Representing attitude: Euler angles,
           unit quaternions, and rotation vectors. Matrix, 58(15-16), 1-35.
    """

    C = np.array(
        [
            [np.cos(theta), np.sin(theta), 0],
            [-np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )

    return C
