import pytest
import numpy as np
from petpy.plots import plot_sensor

@pytest.mark.mpl_image_compare(remove_text=True)
def test_plot_sensor():
    """ Test making a pot"""
    # Setup
    x = np.linspace(0, 100, 5)
    y = 3 * x

    # Exercise
    fig, ax = plot_sensor(x, y)

    # Verify - done by decorator

    return fig