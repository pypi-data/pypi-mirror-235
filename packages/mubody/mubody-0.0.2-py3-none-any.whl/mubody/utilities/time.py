from astropy.time import TimeFormat


class TimeMJDG(TimeFormat):
    """
    Modified Julian Date GMAT time format.
    """

    name = "mjdg"  # Unique format name

    def set_jds(self, val1, val2):
        self._check_scale(self._scale)  # Validate scale.
        jd1, jd2 = val1, val2
        self.jd1, self.jd2 = jd1, jd2

    @property
    def value(self):
        return self.jd1 + self.jd2 - 2430000.0
