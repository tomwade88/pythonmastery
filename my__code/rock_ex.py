import numpy as np
import csv
from functools import total_ordering
import bruges
import doctest

@total_ordering
class Rock:
    """
    A Class to hold rock properties
    """
    def __init__(self, vp, vs, rho=None, name=None):
        self.vp = vp
        self.vs = vs
        self.rho = rho
        self.name = name

    def __repr__(self):
        return "Rock({}, {}, {}, {})".format(self.name, self.vp, self.vs, self.rho)

    def __eq__(self, other):
        return self.acoustic_impedance == other.acoustic_impedance

    def __lt__(self, other):
        return self.acoustic_impedance < other.acoustic_impedance

    def elastic_impedance(self, angle):
        """
        Returns the elastic impedance as defined by Connolly,
        :param angle: Incident angle(s) in degrees, scalar or array.
        :return:

        >>> r = Rock(2300, 1200, 2500)
        >>> r.elastic_impedance(15)
        2013737.0019058161
        """
        return bruges.rockphysics.elastic_impedance(self.vp, self.vs, self.rho, angle)

    @property
    def acoustic_impedance(self):
        return self.vp * self.rho

    @classmethod
    def from_csv(cls, r):
        r = r.split(',')
        name = r[0]
        vp = float(r[1]) if r[1] else np.nan
        vs = float(r[2]) if r[2] else np.nan
        rho = float(r[3]) if r[3] else np.nan
        return cls(vp, vs, rho, name)



def objects_from_csv(filename):
    with open(filename, 'r') as f:
        rocks = []
        reader = f.readlines()
        for row in reader:
            rocks.append(Rock.from_csv(row))
        return rocks

dataIn = '../data/my_rock_data.txt'
myrocks = objects_from_csv(dataIn)

print(myrocks[2]>myrocks[1])

print(myrocks[1].vp)