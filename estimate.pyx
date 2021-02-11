# cython: language_level=3
import numpy as np
cimport numpy as np

cpdef np.ndarray[np.double_t, ndim=1] estimate_pi(np.ndarray[np.double_t, ndim=2] points):
    """Estimate value of pi for each iteration"""
    cdef int i
    cdef int in_circle
    cdef double pi_value
    cdef double distance
    cdef np.ndarray[np.double_t, ndim=1] pi_values

    pi_values = np.ndarray(len(points))

    in_circle = 0
    for i in range(0, len(points)):
        distance = (points[i-1, 0] - 0.5)**2 + (points[i-1, 1] - 0.5)**2

        # checks if point is in circle
        if distance <= 0.5**2:
            in_circle += 1

        pi_value = 4 * in_circle / (i + 1)
        pi_values[i] = pi_value

    return pi_values

