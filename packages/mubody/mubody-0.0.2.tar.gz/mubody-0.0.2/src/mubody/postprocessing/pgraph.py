import matplotlib.pyplot as plt
import numpy as np


def plot_trajectory(trajectory, fig, equal):

    if fig is None:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.set_xlabel('X', fontsize=15)
        ax.set_ylabel('Y', fontsize=15)
        ax.set_zlabel('Z', fontsize=15)

    else:
        ax = fig.gca()

    ax.plot(trajectory[0], trajectory[1], trajectory[2])

    # subcode for equal axis
    if equal:
        X = trajectory[0]
        Y = trajectory[1]
        Z = trajectory[2]

        max_range = np.array([X.max() - X.min(), Y.max() - Y.min(), Z.max() - Z.min()]).max()/2.0

        mid_x = (X.max() + X.min()) * 0.5
        mid_y = (Y.max() + Y.min()) * 0.5
        mid_z = (Z.max() + Z.min()) * 0.5
        ax.set_xlim(mid_x - max_range, mid_x + max_range)
        ax.set_ylim(mid_y - max_range, mid_y + max_range)
        ax.set_zlim(mid_z - max_range, mid_z + max_range)

    return fig


def plot_scatter(trajectory, fig):

    if fig is None:
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.set_xlabel('X', fontsize=15)
        ax.set_ylabel('Y', fontsize=15)
        ax.set_zlabel('Z', fontsize=15)

        ax.scatter(trajectory[0], trajectory[1], trajectory[2])

    else:
        ax = fig.gca()
        ax.scatter(trajectory[0], trajectory[1], trajectory[2])

    return fig


def plotxy(x, y_list):

    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(x, y_list[0])
    ax2.plot(x, y_list[1])

    return f


########
# FUNCTION to PLOT HALO
extra_points = {"libration_point": False,
                "Ln_coords": [],
                "primary_1": False,
                "p1_coords": [],
                "primary_2": False,
                "p2_coords": []
                }


def plot_HALO(r,
              loop=False,
              legend=[],
              save_plot=False,
              plot_3D=True,
              plot_2D=True,
              frame="SEMIdealSynodic",
              title="",
              extra_points=extra_points,
              *args,
              **kwargs):

    r_shape = np.shape(r)

    if plot_3D and loop:
        fig1 = plt.figure(figsize=(8, 8))
        ax = fig1.add_subplot(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        for i in range(r_shape[0]):
            ax.plot(r[i, 0, :], r[i, 1, :], r[i, 2, :])

        if extra_points['libration_point'] is True:
            ax.plot((extra_points['Ln_coords'][0],
                     extra_points['Ln_coords'][1],
                     extra_points['Ln_coords'][2],
                     'ro'))

        if extra_points['primary_1'] is True:
            ax.plot((extra_points['p1_coords'][0],
                     extra_points['p1_coords'][1],
                     extra_points['p1_coords'][2],
                     'go'))

        if extra_points['primary_2'] is True:
            ax.plot((extra_points['p2_coords'][0],
                     extra_points['p2_coords'][1],
                     extra_points['p2_coords'][2],
                     'bo'))

        ax.set_title("3D-Representation")
        ax.legend(legend)

    if plot_3D and loop is False:
        fig1 = plt.figure()
        ax = fig1.add_subplot(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        ax.plot(r[0], r[1], r[2])
        if extra_points['libration_point'] is True:
            ax.plot((extra_points['Ln_coords'][0],
                     extra_points['Ln_coords'][1],
                     extra_points['Ln_coords'][2],
                     'ro'))

        if extra_points['primary_1'] is True:
            ax.plot((extra_points['p1_coords'][0],
                     extra_points['p1_coords'][1],
                     extra_points['p1_coords'][2],
                     'go'))

        if extra_points['primary_2'] is True:
            ax.plot((extra_points['p2_coords'][0],
                     extra_points['p2_coords'][1],
                     extra_points['p2_coords'][2],
                     'bo'))

        ax.set_title("3D-Representation")
        ax.legend(legend)

    if plot_2D and loop:
        # x_lim = max(abs(r[-1, 0, :]))
        # y_lim = max(abs(r[-1, 1, :]))
        # z_lim = max(abs(r[-1, 2, :]))

        fig2, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 10))

        fig2.suptitle(frame, fontsize=20)

        for i in range(r_shape[0]):
            # We plot x-y plane
            ax[0].plot(r[i, 0, :], r[i, 1, :])
            # We plot x-z plane
            ax[1].plot(r[i, 0, :], r[i, 2, :])
            # We plot y-z plane
            ax[2].plot(r[i, 1, :], r[i, 2, :])

        if extra_points['libration_point'] is True:
            ax[0].plot((extra_points['Ln_coords'][0],
                        extra_points['Ln_coords'][1],
                        'ro'))
            ax[1].plot((extra_points['Ln_coords'][0],
                        extra_points['Ln_coords'][2],
                        'ro'))
            ax[2].plot((extra_points['Ln_coords'][1],
                        extra_points['Ln_coords'][2],
                        'ro'))

        if extra_points['primary_1'] is True:
            ax[0].plot((extra_points['p1_coords'][0],
                        extra_points['p1_coords'][1],
                        'go'))
            ax[1].plot((extra_points['p1_coords'][0],
                        extra_points['p1_coords'][2],
                        'go'))
            ax[2].plot((extra_points['p1_coords'][1],
                        extra_points['p1_coords'][2],
                        'go'))

        if extra_points['primary_2'] is True:
            ax[0].plot((extra_points['p2_coords'][0],
                        extra_points['p2_coords'][1],
                        'bo'))
            ax[1].plot((extra_points['p2_coords'][0],
                        extra_points['p2_coords'][2],
                        'bo'))
            ax[2].plot((extra_points['p2_coords'][1],
                        extra_points['p2_coords'][2],
                        'bo'))

        ax[0].grid(True)
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        # ax[0].set_xlim(-lim,lim)
        # ax[0].set_ylim(-lim,lim)
        ax[0].set_title("X-Y Plane")

        ax[1].grid(True)
        ax[1].set_xlabel('x')
        ax[1].set_ylabel('z')
        # ax[1].set_xlim(-lim,lim)
        # ax[1].set_ylim(-lim,lim)
        ax[1].set_title("X-Z Plane")

        ax[2].grid(True)
        ax[2].set_xlabel('y')
        ax[2].set_ylabel('z')
        # ax[2].set_xlim(-lim,lim)
        # ax[2].set_ylim(-lim,lim)
        ax[2].set_title("Y-Z Plane")

        ax[2].legend(legend)
        # ax[0].plot(0,0,'ro'); ax[1].plot(0,0,'ro'); ax[2].plot(0,0,'ro')

    if plot_2D and loop is False:
        fig2, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 10))
        fig2.suptitle(frame, fontsize=20)
        # We plot x-y plane
        ax[0].plot(r[0], r[1])
        ax[0].grid(True)
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        # ax[0].set_xlim(-10e5,10e5)
        # ax[0].set_ylim(-10e5,10e5)
        # We plot x-z plane
        ax[1].plot(r[0], r[2])
        ax[1].grid(True)
        ax[1].set_xlabel('x')
        ax[1].set_ylabel('z')
        # ax[1].set_xlim(-10e5,10e5)
        # ax[1].set_ylim(-10e5,10e5)
        # We plot y-z plane
        ax[2].plot(r[1], r[2])
        ax[2].grid(True)
        ax[2].set_xlabel('y')
        ax[2].set_ylabel('z [km]')
        # ax[2].set_xlim(-10e5,10e5)
        # ax[2].set_ylim(-10e5,10e5)

        if extra_points['libration_point'] is True:
            ax[0].plot((extra_points['Ln_coords'][0],
                        extra_points['Ln_coords'][1],
                        'ro'))

            ax[1].plot((extra_points['Ln_coords'][0],
                        extra_points['Ln_coords'][2],
                        'ro'))

            ax[2].plot((extra_points['Ln_coords'][1],
                        extra_points['Ln_coords'][2],
                        'ro'))

        ax[2].legend(legend)

    plt.show()

    if save_plot:
        plt.savefig(title+'.png', dpi=300)


def plot_manifolds(manifold, mu):

    plot_line = manifold

    fig1, fig2, fig3 = plt.figure(), plt.figure(), plt.figure()
    ax1, ax2, ax3 = fig1.add_subplot(), fig2.add_subplot(), fig3.add_subplot(projection='3d')
    for N in range(len(plot_line)):
        x, y, z, vx, vy, vz = plot_line[N]

        # X-Y Plot
        ax1.plot(x, y)
        ax1.set_xlabel('X', fontsize=15)
        ax1.set_ylabel('Y', fontsize=15)
        # ax1.plot(-mu, 0, 'ro')
        ax1.plot(1-mu, 0, 'bo')
        # X-Z Plot
        ax2.plot(x, z)
        ax2.set_xlabel('X', fontsize=15)
        ax2.set_ylabel('Z', fontsize=15)
        # ax2.plot(-mu, 0, 'ro')
        ax2.plot(1 - mu, 0, 'bo')
        # 3D Plot
        ax3.plot(x, y, z, 'k')

    plt.show()
