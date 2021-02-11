# helper functions for lesson 06 numpy

import numpy as np

def create_position(nframes=10**6):
    """Get array of x, y, and z position of a particle with time.

    Parameters
    ----------
    nframes: int
        number of frames; more frames increases the resolution
        of the trajectory, but not its length

    Returns
    -------
    position : `nframes` x 3 array
        (x, y, z) position of the particle with time

    """
    # generate x, y, z positions
    x = np.cos(np.linspace(0, 20, nframes))
    y = 3 * np.sin(np.linspace(0, 10, nframes))
    z = -2 * np.sin(np.pi * np.linspace(0, 5, nframes))

    # put them all in a single array; this gives
    # an array with 3 rows and nframes columns
    position = np.array([x, y, z])

    # transposing puts the array into the [[x, y, z], [x, y, z], ...] shape
    return position.transpose()
