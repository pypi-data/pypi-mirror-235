import os


def save_eph(mission, file_name):
    mission.coordinate_frame_change('SunJ2000Eq')
    tra_df = mission.sat.orbit.tra_df
    date = mission.DS.date
    txt = tra_df.to_string(header=False)
    times = tra_df.index.values

    file_path = "Results"

    os.makedirs(file_path, exist_ok=True)

    f = open(file_path + "/" + file_name + '.e', 'w+')

    f.write(('stk.v.10.0'
             + '\n# WrittenBy    GMAT R2018a'
             + '\nBEGIN Ephemeris'
             + '\nNumberOfEphemerisPoints ' + str(len(times))
             + '\nScenarioEpoch ' + date.strftime('%d %b %Y %H:%M:%S.%f')
             + '\nCentralBody             Sun'
             + '\nCoordinateSystem        J2000'
             + '\nDistanceUnit            Meters'
             + '\n'
             + '\nEphemerisTimePosVel'
             + '\n'
             + '\n'
             + txt
             + '\n'
             + '\nEND Ephemeris'))

    f.close()


def select_manifolds(manifold, time, direction="left", lagrangian_point=2):
    x_max = max([abs(x[0, 0]) for x in manifold])
    z_max = max([abs(x[2, 0]) for x in manifold])
    y_max = max([abs(x[1, 0]) for x in manifold])
    line, times = [], []

    if lagrangian_point == 2:
        if direction == "left":
            for x, t in zip(manifold, time):
                if abs(x[0, -1]) < x_max and abs(x[2, -1]) < 1.1 * z_max and abs(x[1, -1]) < 1.1 * y_max:
                    line.append(x)
                    times.append(t)

        elif direction == "right":
            for x, t in zip(manifold, time):
                if abs(x[1, -1]) > 1.1 * y_max:
                    line.append(x)
                    times.append(t)

    elif lagrangian_point == 1:
        if direction == "right":
            for x, t in zip(manifold, time):
                if abs(x[0, -1]) > x_max and abs(x[2, -1]) < 1.1 * z_max and abs(x[1, -1]) < 1.1 * y_max:
                    line.append(x)
                    times.append(t)

        elif direction == "left":
            for x, t in zip(manifold, time):
                if abs(x[1, -1]) > 1.1 * y_max:
                    line.append(x)
                    times.append(t)

    return line, times
