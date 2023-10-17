import os
import pickle
import scipy.io


def save_eph(mission, file_name):
    mission.coordinate_frame_change("SunJ2000Eq")
    tra_df = mission.sat.orbit.tra_df
    date = mission.DS.date
    txt = tra_df.to_string(header=False)
    times = tra_df.index.values

    file_path = "Results"

    os.makedirs(file_path, exist_ok=True)

    f = open(file_path + "/" + file_name + ".e", "w+")

    f.write(
        (
            "stk.v.10.0"
            + "\n# WrittenBy    GMAT R2018a"
            + "\nBEGIN Ephemeris"
            + "\nNumberOfEphemerisPoints "
            + str(len(times))
            + "\nScenarioEpoch "
            + date.strftime("%d %b %Y %H:%M:%S.%f")
            + "\nCentralBody             Sun"
            + "\nCoordinateSystem        J2000"
            + "\nDistanceUnit            Meters"
            + "\n"
            + "\nEphemerisTimePosVel"
            + "\n"
            + "\n"
            + txt
            + "\n"
            + "\nEND Ephemeris"
        )
    )

    f.close()


def store(data, file_name, dir_name):
    """
    Stores data in pickle object

    Parameters
    ----------
    data : -
        Data to be stored
    file_name : str
        File name
    dir_name : str
        Folder name
    """

    file_path = "Results/" + dir_name

    os.makedirs(file_path, exist_ok=True)

    file_handler = open(file_path + "/" + file_name, "wb")

    pickle.dump(data, file_handler)

    file_handler.close()

    return 0


def recover(file_name, dir_name):
    """
    Recovers data from pickle object

    Parameters
    ----------
    file_name : str
        File name
    dir_name : str
        Folder name

    Returns
    -------
    data : -
        Data retrieved
    """

    file_path = "Results/" + dir_name
    file_handler = open(file_path + "/" + file_name, "rb")

    data = pickle.load(file_handler)

    file_handler.close()

    return data


def save_mat(file_name, data, data_name):
    """
    Saves data in a .mat file

    Parameters
    ----------
    file_name : str
        Data to be stored
    data : -
        Variable to be saved
    data_name : str
        Name of the variable
    """

    file_path = "Results"

    os.makedirs(file_path, exist_ok=True)

    scipy.io.savemat(file_path + "/" + file_name, {data_name: data})

    print("Data successfully saved")

    return 0


def load_mat(file_name):
    """
    Loada data from .mat file

    Parameters
    ----------
    file_name : str
        Name of the .mat file

    Returns
    -------
    data_loaded : -
        Data retrieved
    """

    file_path = "Results"

    data_loaded = scipy.io.loadmat(file_path + "/" + file_name)

    print("Data successfully loaded")

    return data_loaded
