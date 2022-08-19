"""Tests calculations for the calcs submodule"""
from time import sleep

import numpy as np
import petpy
import pytest
from numpy.testing import assert_array_equal, assert_array_almost_equal
from petpy.calcs import acoustic_impedance, read_sensor_calibrated, get_current_utc_time, classifier
from unittest.mock import patch
from datetime import datetime

def test_acoustic_impedance_valid_values():
    """ Tests with valid numbers"""
    # Setup
    vp = 2200
    rho = 2400
    truth = 5280000

    # Exercise
    result = acoustic_impedance(rho, vp)

    # Verify
    assert truth == result

def test_acoustic_impedance_valid_array():
    """ Tests with valid array"""
    # Setup
    vp = np.array([2000., 2500., 2750., 3000.])
    rho = np.array([1900., 2200., 2300., 2500.])
    #truth = 967
    truth = np.array([3800000., 5500000., 6325000., 7500000.])

    # Exercise
    result = acoustic_impedance(rho, vp)

    # Verify
    assert_array_almost_equal(truth, result)

def mocked_read_sensor():
    """Mock the sensor by always returning unity"""
    return 1

@patch('petpy.calcs.read_sensor', new=mocked_read_sensor)
def test_read_sensor_calibrated():
    """Test the calibration worys with a unity sensor input"""

    # Setup
    truth = 2.2

    # Exercise
    result = read_sensor_calibrated()

    # Verify
    assert_array_almost_equal(truth, result)

def mocked_current_utc_time():
    """Mock the timefunction for testing"""
    return datetime(1989, 3, 26, 12)
    
@patch('petpy.calcs.get_current_utc_time', new=mocked_current_utc_time)
def test_current_utc_time():
    # Setup
    truth = datetime(1989, 3, 26, 12)
    sleep(1)

    # Exercise
    result = petpy.calcs.get_current_utc_time()

    # Verify
    assert truth == result

@pytest.mark.parametrize('density, expected, will_fail',
                         [(2750, 'granite', False),
                        (2500, 'sandstone', False),
                        (1000, 'not a rock', False),
                        (2800, 'granite', False),
                        (-5, '', True)
                        ])
def test_classifier(density, expected, will_fail):
    """
    Verify that we correctly identified a grainite
    """
    # Setup

    if will_fail:
        with pytest.raises(ValueError):
            classifier(density)
    else:
        result = classifier(density)
        assert result == expected

