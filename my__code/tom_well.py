import numpy as np

class Well(object):
    def __init__(self, name, tops, location=(None, None)):
        self.name = name
        self.tops = tops
        self.location = location

    @staticmethod
    def parse_csv(path):
        tops = {}
        with open(path, 'r') as f:
            data = f.readlines()
            for x in data:
                if 'Full Name' in x:
                    full_name = x.split(':')[-1]
                if 'Latitude (NAD27)' in x:
                    latitude = float(x.split(':')[-1])
                if 'Longitude (NAD27)' in x:
                    longitude = float(x.split(':')[-1])
                if x.startswith('#'):
                    continue
                top_name = x.split(',')[-1].strip()
                tops[top_name] = {}
                subs = x.split(',')[-4]
                tops[top_name]['top'] = float(subs) if subs else np.nan
                subs = x.split(',')[-3]
                tops[top_name]['base'] = float(subs) if subs else np.nan

                units = x.split(',')[-2]
                tops[top_name]['units'] = units

            return full_name, (latitude, longitude), tops

    @classmethod
    def from_csv(cls, path):
        name, location, tops = cls.parse_csv(path)
        return cls(name, tops, location)

inF = "../data/tops/ABENAKI_L-57.tops"
mywell = Well.from_csv(inF)
print(mywell.location)
