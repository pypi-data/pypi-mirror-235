from mubody.mission import Mission
from mubody.utilities.io import load_mat, save_mat
import numpy as np
import shutil
import os


def test_save_pickle():

    mission_save = Mission()

    mission_save.AO(bar=False)

    result = mission_save.save("saving_test", "tests")

    shutil.rmtree("Results/tests")

    try:
        os.rmdir("Results")
    except Exception:
        pass

    assert result == 0


def test_load_pickle():

    mission_save = Mission()
    mission_load = Mission()

    mission_save.AO(bar=False)

    mission_save.save("loading_test", "tests")

    result = mission_load.load("loading_test", "tests")

    shutil.rmtree("Results/tests")

    try:
        os.rmdir("Results")
    except Exception:
        pass

    assert result == 0


def test_save_mat():

    data = np.random.random(100)

    result = save_mat("save_test.mat", data, "data_test")

    os.remove("Results/save_test.mat")

    try:
        os.rmdir("Results")
    except Exception:
        pass

    assert result == 0


def test_load_mat():

    data = np.random.random(100)

    save_mat("load_test.mat", data, "data_test")

    data_loaded = load_mat("load_test.mat")

    result = len(data) == len(data_loaded)

    os.remove("Results/load_test.mat")

    try:
        os.rmdir("Results")
    except Exception:
        pass

    assert result == 0
