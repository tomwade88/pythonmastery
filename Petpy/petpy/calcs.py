import numpy as np
from datetime import datetime

def acoustic_impedance(rho, vp):
    """Calculate the acoustic impedance.

    Calculate basic acoustic impedance using the density an d p-wave
    velocity of a rock.

    parameters
    _____________
    rho : array-like
        Density with units of kg/m^3
    vp : array-like
        P-wave velocity with units of m/s

    :returns
    -------------------
    array-like
        acoustic impedance

    See Also
    -------------------
    bulk_density

    """
    return rho * vp

def read_sensor():
    """Reads the pressure sensor from the plant."""
    return -999.25

def read_sensor_calibrated():
    """Read a pressure sensor and calibrate the output"""
    sensor_value = read_sensor()
    return sensor_value * 2.2

def get_current_utc_time():
    return datetime.utcnow()

def classifier(density):
    """
    Classify rocks with secret algorithm

    :param denisty:
    :return:
    """
    if density <= 0:
        raise ValueError('Density cannot be zero or negative.')

    elif density >= 2705:
        return 'granite'
    elif density >= 2400:
        return 'sandstone'
    else:
        return 'not a rock'