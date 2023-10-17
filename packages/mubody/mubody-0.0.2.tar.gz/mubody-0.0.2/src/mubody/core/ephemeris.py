import os
from pathlib import Path

import numpy as np
import pkg_resources
import requests
from scipy.interpolate import splev, splrep

import spiceypy as spice
from mubody.constants import (J2000_epoch, SolarSystemBodies_list,
                              naif_names_ids)


class Ephemeris:
    """
    Ephemeris class

    Attributes
    ----------
    name : str
        Name of the model
    """

    def __init__(
        self,
        epoch=J2000_epoch,
        bodies=SolarSystemBodies_list,
        tf=365 * 86400,
        dT=86400,
        reference="Sun",
        test=False
    ):
        """
        Constructor

        Parameters
        ----------
        epoch : DateTime class
            Epoch used as time reference
        bodies : list
            List of strings with the names of the celestial bodies whose
            ephemeris are generated
        tf : float
            Extent of time for which the ephemeris are generated [s]
        dT : float
            Time step [s]
        reference : str
            NAIF ID of the body used as reference for the ephemeris
        """

        self.epoch = epoch
        self.bodies = bodies
        self.tf = tf
        self.dT = dT
        self.reference = reference

        self.kernels_list = ["de405.bsp", "naif0011.txt"]
        self.kernels_folder_path = pkg_resources.resource_filename("mubody", "data/")
        self.url_dict = {
            "de405.bsp": "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de405.bsp",  # noqa
            "naif0011.txt": "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0011.tls",
        }

        if not test:
            self.load_kernels()
            self.load_ephemeris()

    def get_body_ID(self, body_identifier):
        """
        Return the NAIF ID of the body.

        Parameters
        ----------
        body_identifier : str
            Name or NAIF ID of body

        Returns
        -------
        naif_id : str
            NAIF ID
        """

        if body_identifier.isdigit():
            naif_id = body_identifier
        else:
            try:
                naif_id = naif_names_ids[body_identifier]
            except KeyError:
                raise ValueError("Invalid Name")

        return naif_id

    def load_kernels(self):
        """
        Load SPICE kernels.

        If kernel files are not in the system, it will try to download them.
        If the kernel are already loaded, it will do nothing.
        """

        if self.check_kernels_files():
            pass
        else:
            if not os.path.exists("src/mubody/data"):
                os.makedirs("src/mubody/data")
            try:
                self.download_kernels()
            except Exception:
                raise Exception("Error downloading SPICE kernels.")

        if self.check_kernels_load():
            pass
        else:
            for kernel in self.kernels_list:
                file_path = self.kernels_folder_path + kernel
                spice.furnsh(file_path)

        return 0

    def check_kernels_files(self):
        """
        Checks if the required kernels files are present in the data folder.

        Returns
        -------
        kernels_files_flag : boolean
            If True, all required kernels files are present
        """

        kernels_files_flag_list = []

        for kernel in self.kernels_list:
            file_path = self.kernels_folder_path + kernel
            kernels_files_flag_list.append(Path(file_path).is_file())

        kernels_files_flag = all(kernels_files_flag_list)

        return kernels_files_flag

    def check_kernels_load(self):
        """
        Checks if the required kernels files have been loaded.

        Returns
        -------
        kernels_load_flag : boolean
            If True, all required kernels files are present
        """

        n_kernels = spice.ktotal("ALL")
        loaded_kernels_list = []

        for i in range(0, n_kernels):
            [file, _, _, _] = spice.kdata(i, "ALL")
            loaded_kernels_list.append(file)

        kernels_load_flag = set(loaded_kernels_list) == set(self.kernels_list)

        return kernels_load_flag

    def download_kernels(self):
        """
        Downloads the required kernels.
        """

        print("Downloading required kernels...")

        os.makedirs(os.path.dirname(self.kernels_folder_path), exist_ok=True)

        for kernel in self.kernels_list:
            r = requests.get(self.url_dict[kernel])
            file_path = self.kernels_folder_path + kernel
            open(file_path, "wb").write(r.content)

        print("Done")

        return 0

    def get_spice_eph(self, date, body, time, reference):
        """
        Retrieves ephemeris from spice kernels

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        states : ndarray (6, n)
            State vectors of the target body [km, km/s]
        """

        body_id = self.get_body_ID(body)
        reference_id = self.get_body_ID(reference)

        t_ephem = time / (3600 * 24) + date.jd

        et_f = []

        for item in np.asarray([t_ephem]).flatten():
            et = spice.str2et(str(item) + "JD")
            et_f = np.append(et_f, et)

        states, _ = spice.spkezr(body_id, et_f, "J2000", "NONE", reference_id)
        states = np.asarray(states).T

        return states

    def generate_ephemeris_dict(self, epoch, bodies, tf, dT, reference):
        """
        Retrieves ephemeris from spice kernels and stores them for interpolation

        The epehemeris are retrieved for a period of time with a sample time. Then,
        tck parameters are generated for interpolation of intermediate times. The
        parameters of each body/point are stored in a dict as a global variable.

        Parameters
        ----------
        epoch : DateTime class
            Epoch of time[0]
        bodies : list
            List of names of the target celestial bodies/points
        tf : float
            Extent of time for which the ephemeris are generated [s]
        dT : float
            Time step [s]
        reference : str
            Name of the celestial body/point used as reference
        """

        # global ephemeris_dict
        ephemeris_dict = {}

        k = 3
        time_margin = 10 * 86400

        time = np.arange(-time_margin, tf + time_margin, dT)

        for body in bodies:
            body_id = self.get_body_ID(body)
            ephemeris = self.get_spice_eph(epoch, body_id, time, reference)

            r_eph = ephemeris[0:3, :]
            v_eph = ephemeris[3:6, :]

            x_slp = splrep(time, r_eph[0], k=k)
            y_slp = splrep(time, r_eph[1], k=k)
            z_slp = splrep(time, r_eph[2], k=k)
            vx_slp = splrep(time, v_eph[0], k=k)
            vy_slp = splrep(time, v_eph[1], k=k)
            vz_slp = splrep(time, v_eph[2], k=k)

            slp_dict = {
                "x": x_slp,
                "y": y_slp,
                "z": z_slp,
                "vx": vx_slp,
                "vy": vy_slp,
                "vz": vz_slp,
            }

            ephemeris_dict.update({body_id: slp_dict})

        return ephemeris_dict

    def load_ephemeris(self):
        """
        Retrieves ephemeris from spice kernels and stores them for interpolation

        The epehemeris are retrieved for a period of time with a sample time. Then,
        tck parameters are generated for interpolation of intermediate times. The
        parameters of each body/point are stored in a dict as a global variable.

        """

        self.ephemeris_dict = self.generate_ephemeris_dict(
            self.epoch, self.bodies, self.tf, self.dT, self.reference
        )

        return 0

    def get_eph_r_sp(self, date, body, time, reference):
        """
        Retrieves position of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        r : ndarray (3,n)
            Position vectors of the target body [km]
        """

        states = self.get_spice_eph(date, body, time, reference)

        r = states[0:3, :]

        return r

    def get_eph_v_sp(self, date, body, time, reference):
        """
        Retrieves velocity of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        v : ndarray (3, n)
            Velocity vectors of the target body [km/s]
        """

        states = self.get_spice_eph(date, body, time, reference)

        v = states[3:6, :]

        return v

    def r_sp(self, body, time):
        """
        Retrieves position of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest

        Returns
        -------
        r : ndarray (3, n)
            Position vectors of the target body [km]
        """

        r = self.get_eph_r_sp(self.epoch, body, time, self.reference)

        return r

    def v_sp(self, body, time):
        """
        Retrieves velocity of body from the spice kernels ephemeris.

        Wrapper of get_spice_eph.

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]

        Returns
        -------
        v : ndarray (3, n)
            Velocity vectors of the target body [km/s]
        """

        v = self.get_eph_v_sp(self.epoch, body, time, self.reference)

        return v

    def get_eph_r(self, date, body, time, reference):
        """
        Interpolates position from ephemeris

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        r : ndarray (3, n)
            Position vectors of the target body [km]
        """

        body_id = self.get_body_ID(body)

        slp = self.ephemeris_dict[body_id]
        x_slp = slp["x"]
        y_slp = slp["y"]
        z_slp = slp["z"]

        x = splev(time, x_slp)
        y = splev(time, y_slp)
        z = splev(time, z_slp)

        r = np.array([x, y, z]).reshape(3, -1)

        return r

    def get_eph_v(self, date, body, time, reference):
        """
        Interpolates velocity from ephemeris

        Parameters
        ----------
        date : DateTime class
            Epoch of time[0]
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]
        reference : str
            Name of the celestial body/point used as reference

        Returns
        -------
        v : ndarray (3, n)
            Velocity vectors of the target body [km/s]
        """

        body_id = self.get_body_ID(body)

        slp = self.ephemeris_dict[body_id]
        vx_slp = slp["vx"]
        vy_slp = slp["vy"]
        vz_slp = slp["vz"]

        vx = splev(time, vx_slp)
        vy = splev(time, vy_slp)
        vz = splev(time, vz_slp)

        v = np.array([vx, vy, vz]).reshape(3, -1)

        return v

    def r(self, body, time):
        """
        Interpolates position from ephemeris

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]

        Returns
        -------
        r : ndarray (3, n)
            Position vectors of the target body [km]
        """

        r = self.get_eph_r(self.epoch, body, time, self.reference)

        return r

    def v(self, body, time):
        """
        Interpolates velocity from ephemeris

        Parameters
        ----------
        body : str
            Name of the target celestial body/point
        time : 1D-array (n)
            Instants of interest [s]

        Returns
        -------
        v : ndarray (3, n)
            Velocity vectors of the target body [km/s]
        """

        v = self.get_eph_v(self.epoch, body, time, self.reference)

        return v
