import mubody.core.rnbp as rnbp
import mubody.numeric as nm
import mubody.algorithms.orbital as mao
from mubody.core.satellite import Satellite
from mubody.core.satellite import extract_points
from mubody.postprocessing import pgraph
from mubody.utilities.io import store, recover
import numpy as np
import time as clock_time
import math


class Mission:
    """
    Interface with the user.

    This class includes high level functions and integrates Satellite class.

    Attributes
    ----------
    name : str
        Name of the mission.
    status : str
        Status of the mission.
    mission_time : str
        Total mission time.
    sat : class
        Satellite class object.
    default_ROLE : list (4)
        Default reduced osculating lissajous elements.
    """

    defargs = {'name': "Default_mission",
               'mission_time': 360*86400,
               'date': '2010-01-01 00:00:00',
               'primary_1': "Sun",
               'primary_2': "Earth",
               'lagrangian_point': 2,
               'perturbations': [],
               'orbit': "Lissajous",
               'HOP': [125000, 'northern', 0],  # Az, class, phase
               'ROLE': np.array([120e6, 300e6, 180, 90]),
               'verbose': False,
               'Halo_method': 'Howell',
               'SRP_flag': False
               }

    def __init__(self, **kwargs):

        kwargs = {**self.defargs, **kwargs}
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.name = "Default_mission"
        self.setup_dynamical_system()
        self.setup_orbit_parameters()
        self.setup_coordinate_frames()
        self.status = None
        self.sat = Satellite('P1-IdealSynodic', **kwargs)
        # utl.generate_eph(self.DS.date, list(self.DS.celestial_bodies_dict.keys()), self.mt, 3600,'sun')

    @property
    def mt(self):
        return self.mission_time

    @property
    def T(self):
        data_list = self.DS.models['CRTBP'].models[self.orbit].get_Halo_data(self.HOP, coords=False, verbose=False)
        data = data_list[0]
        T_Halo = data[0]*86400  # Orbital period in seconds
        return T_Halo

    @property
    def frame(self):
        F = self.sat.orbit.frame
        return F

    def setup_dynamical_system(self):
        self.DS = rnbp.dynamical_system(self.date,
                                        self.primary_1,
                                        self.primary_2,
                                        self.lagrangian_point,
                                        self.orbit,
                                        self.perturbations,
                                        self.mt,
                                        self.SRP_flag
                                        )

        return 0

    def setup_orbit_parameters(self, stable=True, parameter_type=None, parameter=None):
        # orbit_parameters --> HOP for Halo; ROLE for Lissajous

        """
        Parameters:

            stable : bool
                Boolean to choose between general and stable solution
            parameter_type : string
                Orbit parameter set type (IC/ROLE)
            parameter : 1-D array
                Orbit parameter set (IC/ROLE/HOP, m, m/s)

        """
        self.orbit_parameters = self.DS.models['CRTBP'].orbit_parameters(parameter_type,
                                                                         parameter,
                                                                         stable,
                                                                         self.ROLE,
                                                                         self.HOP)

    def setup_coordinate_frames(self):
        self.DS.setup_coordinate_frames()
        return 0

    def coordinate_frame_change(self, destination_frame):
        """
        Changes coordinate frame of the trajectory

        Parameters
        ----------
        destination_frame : str
            destination frame
        """

        if destination_frame == self.frame:
            return 0

        time = self.sat.orbit.trajectory.df.index.values
        ri = self.sat.orbit.trajectory.df[['x', 'y', 'z']].values.T
        vi = self.sat.orbit.trajectory.df[['vx', 'vy', 'vz']].values.T
        frame_origin = self.DS.coordinate_frames[self.frame]
        frame_destination = self.DS.coordinate_frames[destination_frame]
        frame_aux = self.DS.coordinate_frames['Ln-IdealSynodic']
        rf, vf = mao.csta(time, ri, vi, frame_origin, frame_destination, frame_aux)
        self.sat.add_orbit(time, rf, vf, True, destination_frame)

        return 0

    def AO(self, deltaT=8640, frame='Ln-Synodic', bar=True, mission_t=None):
        """
        Generates orbit with the analytical solution from the CRTBP model

        The linealization of CRTBP equations around L2 provides analytical
        solution. General solution is unstable.

        The orbit can be defined by its IC (stable/unstable orbits) or its ROLE
        (only stable orbits). In the case of providing IC, the stable solution
        is obtained by nulling the non-stable GOLE parameters, for which vx and
        vy are modified. In both cases, the parameters are converted to GOLE and
        then the analytical orbit is generated.

        If no parameters are provided, default HOP/ROLE parameters are used.

        In the Lissajous orbit:

        General solution has 6 constants:
            A1, A2, A3, A4, Az, phi_z, called here: General Osculating Lissajous
            Elements (GOLE)

        Another form is:
            A1, A2, Ax, Az, phi_xy, phi_z, called here: Osculating Lissajous
            Elements (OLE)

        Stable solution implies A1=A2=0, giving place to:
            Ax, Az, phi_xy, phi_z called here: Reduced Lissajous Elements
            (ROLE)

        Notes:
        For a state vector, a one-to-one relation to GOLE/OLE exists.
        ROLE to IC transformation obtains a stable state vector
        IC to ROLE implies to apply a DV to state vector to obtain a stable one

        In the Halo orbit:
        Solution has 3 parameters that defined the orbit, calle here: Halo Orbital Parameters
        (HOP)

            Az --> Indicates the amplitude of the orbit
            class --> Norther Halo (Class I) or Souther Halo (class 2)
            phi --> Indicates the position in the orbit

        Parameters
        ----------
        deltaT : float
            Time step (seconds)
        frame : bool
            Desired frame for the output trajectory
        bar : bool
            If True, shows progress bar
        """

        if bar:
            print("\n"), print("Starting Simulation...")

        if mission_t is None:
            mt = self.mt
        else:
            mt = mission_t

        self.sat.add_orbit(*nm.propagate_analytically(self.DS.models['CRTBP'].models[self.orbit],
                                                      self.orbit_parameters,
                                                      mt,
                                                      deltaT,
                                                      bar))

        self.coordinate_frame_change(frame)

        self.status = "Mission simulated" + " (" + "CRTBP" + "/Analytical) "

        if bar:
            print(self.status), print("\n")

        return 0

    def IC(self, model="CRTBP", IC=None, IC_frame='Sun-J2000Eq', frame='Ln-Synodic', N=1000, bar=True):
        """
        Generates orbit from direct integration of model equations

        Parameters
        ----------
        model : str
            Physical model to be used (CRTBP/ERTBP/FETBP)
        IC : ndarray (6,1)
            Initial conditions (r,v) (m, m/s)
        IC_frame : string
            Frame in which IC are expressed
        frame : string
            Desired frame for the output trajectory
        bar : bool
            If True, shows progress bar
        """

        if IC is None:
            IC, IC_frame = self.generate_IC(model)
        else:
            IC, IC_frame = self.adapt_IC(model, IC, IC_frame)

        self.sat.add_orbit(*nm.propagate_numerically(self.DS.models[model], 0, self.mt, IC, N))
        self.dim_tra()
        self.coordinate_frame_change(frame)

        self.status = "Mission simulated" + " (" + model + "/IC integration) "

        if bar:
            print(self.status, "\n")

        return 0

    def HTM(self, model="CRTBP", ref_orbit=None, bar=True, frame='Ln-Synodic'):

        """
        Computes reference orbit using the work in Formation Flying in the Sun-Earth/Moon Perturbed Restricted
        Three-Body Problem, Ingvar Out, based on Howell (1984).

        Parameters
        ----------
        model : str
                Physical model to be used (CRTBP/FETBP)
        ref_orbit : orbit class
                    Reference orbit (optional)
        frame : string
                Desired frame for the output trajectory
        bar : bool
              If True, shows progress bar
        """

        # start_time = clock_time.time()

        crtbp_flag = model == "CRTBP"

        if bar:
            print("\n"), print("Starting Simulation...")

        if ref_orbit is None:
            self.generate_ref_orbit(crtbp_flag=crtbp_flag, refine=False, bar=bar, mission_t=self.T/2,
                                    method='Richardson')
        else:
            self.sat.orbit = ref_orbit
            self.mission_time = ref_orbit.mt()

        N_segments = 1

        if model == 'CRTBP':
            frame_HTM = 'P1-IdealSynodic'
            self.coordinate_frame_change('P1-IdealSynodic')
            self.adim_tra()
        else:
            frame_HTM = 'Sun-J2000Eq'
            self.coordinate_frame_change('Sun-J2000Eq')

        trajectory_points_df = extract_points(self.sat.orbit, N_segments)

        self.sat.orbit.tra_scat = trajectory_points_df

        time, position, velocity, DV, DT, _ = mao.Halo_targeting_method(self.DS.models[model], trajectory_points_df,
                                                                        bar)

        # Creation of one orbit by symmetry in the xz plane
        time = np.append(time[:-1], time[-1] + time)

        position11 = np.copy(position)
        position[1, :] = -1*position11[1, :]
        position = np.append(position11[:, :-1], np.flip(position, axis=1), axis=1)

        velocity11 = np.copy(velocity)
        velocity[1, :] = -1*velocity11[1, :]
        velocity = np.append(velocity11[:, :-1], -1*np.flip(velocity, axis=1), axis=1)

        # Adjustment to exact mission time
        n_orbits = math.ceil(self.mt/(self.T))

        if n_orbits != 1:
            for i in range(n_orbits - 1):
                time = np.append(time[:-1], time[-1] + time)
                position = np.append(position, position, axis=1)
                velocity = np.append(velocity, velocity, axis=1)

        if self.mt < n_orbits*self.T:
            index = np.where((time*self.DS.models[model].ts > self.mt))[0][0]
            time = time[:index]
            position = position[:, :index]
            velocity = velocity[:, :index]

        self.sat.add_orbit(time, position, velocity, False, frame_HTM)

        self.dim_tra()

        self.coordinate_frame_change(frame)

        return 0

    def ETM(self, model="CRTBP", t_maneouver=30*24*3600, ref_orbit=None, refine=False, frame='Ln-Synodic', bar=True):
        """
        Computes required DV and resulting trajectory when Equiting Targeting Method for station keeping control is
        applied to a reference orbit.

        Parameters
        ----------
        model : str
            Physical model to be used (CRTBP/FETBP)
        t_manuever : float
            Time between maneuvers
        ref_orbit : orbit class
            Reference orbit (optional)
        refine : bool
            If True, default orbit is refined (only used if ref_orbit is None)
        frame : string
            Desired frame for the output trajectory
        bar : bool
            If True, shows progress bar
        """

        start_time = clock_time.time()

        crtbp_flag = model == "CRTBP"

        if bar:
            print("\n"), print("Starting Simulation...")

        if ref_orbit is None:
            if self.orbit == 'Halo':
                self.generate_ref_orbit(crtbp_flag=crtbp_flag, refine=False, bar=bar, method=self.Halo_method)
            else:
                self.generate_ref_orbit(crtbp_flag=crtbp_flag, refine=False, bar=bar)
        else:
            self.sat.orbit = ref_orbit
            self.mission_time = ref_orbit.mt()

        N_segments = int(self.mt/t_maneouver)

        if model == 'CRTBP':
            frame = 'P1-IdealSynodic'
            self.coordinate_frame_change('P1-IdealSynodic')
            self.adim_tra()
        else:
            frame = 'Sun-J2000Eq'
            self.coordinate_frame_change('Sun-J2000Eq')

        trajectory_points_df = extract_points(self.sat.orbit, N_segments)

        self.sat.orbit.tra_scat = trajectory_points_df

        time, position, velocity, DV, DT, _ = mao.targeting_method(self.DS.models[model], trajectory_points_df, bar,
                                                                   orbit_type=self.orbit)

        self.state = np.concatenate((position, velocity), axis=0)
        self.sat.add_orbit(time, position, velocity, self.sat.orbit.trajectory.dim_status, frame)

        self.dim_tra()

        self.coordinate_frame_change('Ln-Synodic')

        self.status = "Mission Simulated" + " (" + model + "/ETM integration) "

        print(self.status)
        print("\n")
        if model == "CRTBP":
            TotalDV_opt = np.linalg.norm(DV[:, 1:], axis=0).sum() * self.DS.models[model].vs
        elif model == "FETBP":
            TotalDV_opt = np.linalg.norm(DV[:, 1:], axis=0).sum()

        print("\n Total DeltaV:\n")
        print(str(TotalDV_opt) + " m/s \n")

        self.sat.DV = DV
        self.sat.DT = DT

        self.report_dict = {"Mission Time": self.mt/86400,
                            "Model": model,
                            "Segments": N_segments,
                            "n opt": "-",
                            "DV": int(TotalDV_opt),
                            "Final DV": int(TotalDV_opt),
                            "Method": "ETM",
                            "Refine": "-",
                            "Perturbations": self.perturbations,
                            "Computation time": clock_time.time() - start_time
                            }

        return 0

    def OTM(self,
            model="CRTBP",
            N_segments=None,
            opt_iterations=3,
            ref_orbit=None,
            refine=False,
            frame='Ln-Synodic',
            bar=True):
        """
        Optimizes an orbit applying iteratively a targeting method and a
        linear correction of the orbit positions. After several
        iterations DV is reduced to nearly 0.

        Parameters
        ----------
        model : str
            Physical model to be used (CRTBP/FETBP)
        N_segments : int
            Number of segmets in whih the orbit is divided
        opt_iterations : int
            Number of optimizations iterations
        ref_orbit : orbit class
            Reference orbit (optional)
        refine : bool
            If True, default orbit is refined (only used if ref_orbit is None)
        frame : string
            Desired frame for the output trajectory
        bar : bool
            If True, shows progress bar
        """

        start_time = clock_time.time()

        crtbp_flag = model == "CRTBP"

        if bar:
            print("\n"), print("Starting Simulation...")

        if ref_orbit is None:
            if self.orbit == 'Halo':
                mission_t = math.ceil(self.mt/(self.T/2))*self.T/2
                self.generate_ref_orbit(crtbp_flag=crtbp_flag, refine=False, bar=bar, mission_t=mission_t)
            else:
                self.generate_ref_orbit(crtbp_flag=crtbp_flag, refine=False, bar=bar)
        else:
            self.sat.orbit = ref_orbit
            self.mission_time = ref_orbit.mt()

        if model == 'CRTBP':
            frame = 'P1-IdealSynodic'
            self.coordinate_frame_change('P1-IdealSynodic')
            self.adim_tra()
        else:
            frame = 'Sun-J2000Eq'
            self.coordinate_frame_change('Sun-J2000Eq')

        if N_segments is None:
            if self.orbit == 'Halo':
                N_segments = int(mission_t/(self.T/2))
            else:
                N_segments = int(self.mt/(30*86400))

        trajectory_points_df = extract_points(self.sat.orbit, N_segments)

        self.sat.orbit.tra_scat = trajectory_points_df

        time, position, velocity, DV, DT, report_dict = mao.optimized_targeting_method(self.DS.models[model],
                                                                                       trajectory_points_df,
                                                                                       N_segments,
                                                                                       opt_iterations,
                                                                                       bar, orbit_type=self.orbit
                                                                                       )
        self.state = np.concatenate((position, velocity), axis=0)
        self.sat.add_orbit(time, position, velocity, self.sat.orbit.trajectory.dim_status, self.frame)

        self.dim_tra()

        self.coordinate_frame_change(frame)

        # Reduce dataframe to real mission time for Halo orbits
        if self.orbit == 'Halo' and self.mt < mission_t:
            index = np.where((self.sat.orbit.trajectory.df.index > self.mt))[0][0]
            self.sat.orbit.trajectory.df = self.sat.orbit.trajectory.df.drop(self.sat.orbit.trajectory.df.index[index:])

        self.sat.DV = DV
        self.sat.DT = DT

        self.status = "Mission Simulated" + " (" + model + "/Differential corrections) "

        print(self.status)
        print("\n")

        self.report_dict = report_dict
        self.report_dict.update({"Method": "DC",
                                 "Refine": refine,
                                 "Perturbations": self.perturbations,
                                 "Time": clock_time.time() - start_time
                                 })

        return 0

    def generate_ref_orbit(self, crtbp_flag, refine, bar, mission_t=None, method=None):

        if bar:
            print("Generating Reference Orbit... ")

        if self.orbit == 'Lissajous' or (self.orbit == 'Halo' and method == 'Richardson'):
            self.AO(frame='P1-IdealSynodic', bar=False, mission_t=mission_t)
        elif self.orbit == 'Halo' and method == 'Howell':
            self.HTM(frame='P1-IdealSynodic', bar=False)

        self.adim_tra()

        if bar:
            print("Done\n")

        if crtbp_flag:
            pass
        else:
            if refine:
                print("Refining Reference Orbit... ")

                if mission_t is None:
                    N_seg = int(self.mt/(30*86400))
                else:
                    N_seg = int(mission_t/(self.T/2))
                    # N_seg = int(mission_t/(30*86400))
                self.DC(N_segments=N_seg, opt_iterations=5, ref_orbit=self.sat.orbit, bar=False)

                print("Done\n")

            self.dim_tra()
            self.coordinate_frame_change('Sun-J2000Eq')

        return 0

    def generate_IC(self, model_name):
        """ Generates IC vector for its propagation

        Parameters
        ----------
        model_name : string
            Name of the dynamical model used

        Returns
        -------
        IC : ndarray (6,1)
            Initial condition vector
        frame : str
            Frame in which the initial conditions are expressed

        """
        if self.orbit == 'Lissajous':
            s = self.DS.models['CRTBP'].get_IC(self.ROLE)
        else:
            s = self.DS.models['CRTBP'].get_IC(self.HOP)

        if model_name == 'CRTBP':
            s = self.DS.models['CRTBP'].models['Lissajous'].remove_IC_dimensions(s)
            frame = 'P1-IdealSynodic'

        else:
            r, v = mao.csta(np.zeros(1),
                            s[0:3, :],
                            s[3:6, :],
                            self.DS.coordinate_frames['P1-IdealSynodic'],
                            self.DS.coordinate_frames['Sun-J2000Eq'],
                            self.DS.coordinate_frames['Ln-IdealSynodic'])

            s = np.concatenate((r, v), axis=0)
            frame = 'Sun-J2000Eq'

        return s, frame

    def adapt_IC(self, model_name, IC, IC_frame):
        """ Adapts the input initial conditions to the required frame for propagations

        Parameters
        ----------
        model_name : string
            Name of the dynamical model used
        IC : ndarray (6,1)
            Initial condition vector to transformed
        IC_frame : str
            Frame in which the initial conditions are expressed originally

        Returns
        -------
        IC : ndarray (6,1)
            New nitial condition vector
        IC_frame_new : str
            New frame of initial conditions
        """

        if model_name == "CRTBP":
            IC_frame_new = 'P1-IdealSynodic'
            r, v = mao.csta(np.zeros(1),
                            IC[0:3, :],
                            IC[3:6, :],
                            self.DS.coordinate_frames[IC_frame],
                            self.DS.coordinate_frames[IC_frame_new],
                            self.DS.coordinate_frames['Ln-IdealSynodic']
                            )

            s = np.concatenate((r, v), axis=0)
            s = self.DS.models['CRTBP'].models['Lissajous'].remove_IC_dimensions(s)

        else:
            IC_frame_new = 'Sun-J2000Eq'
            r, v = mao.csta(np.zeros(1),
                            IC[0:3, :],
                            IC[3:6, :],
                            self.DS.coordinate_frames[IC_frame],
                            self.DS.coordinate_frames[IC_frame_new],
                            self.DS.coordinate_frames['Ln-IdealSynodic']
                            )

            s = np.concatenate((r, v), axis=0)

        return s, IC_frame_new

    def save(self, file_name, dir_name=None):
        """
        Save mission class

        Parameters
        ----------
        file_name : str
            File name
        dir_name : str
            Folder name
        """

        if dir_name is None:
            dir_name = self.name

        flag = store(self, file_name, dir_name)

        if flag == 0:
            print("Mission successfully saved")
        else:
            raise Exception("Error during saving")

        return 0

    def load(self, file_name, dir_name):
        """
        Load mission class data

        Parameters
        ----------
        file_name : str
            File name
        dir_name : str
            Folder name
        """

        mission_loaded = recover(file_name, dir_name)

        self.status = mission_loaded.status
        self.name = mission_loaded.name
        self.mission_time = mission_loaded.mt
        self.sat = mission_loaded.sat

        if self.verbose:
            print("Mission successfully loaded")
            print("Mission Name:", mission_loaded.name)
            print("Mission Status:", mission_loaded.status)
            print("Mission Duration:", mission_loaded.mt/86400, "days")

        return 0

    def plot_trajectory(self, fig=None, equal=False):
        figure = pgraph.plot_trajectory(self.sat.orbit.trajectory.df[['x', 'y', 'z']].values.T, fig, equal)

        return figure

    def dim_tra(self):
        self.sat.orbit.trajectory.dim(self.DS.models['CRTBP'].models['Lissajous'])

    def adim_tra(self):
        self.sat.orbit.trajectory.adim(self.DS.models['CRTBP'].models['Lissajous'])
