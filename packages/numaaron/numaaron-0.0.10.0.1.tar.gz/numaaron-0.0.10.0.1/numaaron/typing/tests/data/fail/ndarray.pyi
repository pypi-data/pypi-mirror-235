import numaaron as np

# Ban setting dtype since mutating the type of the array in place
# makes having ndarray be generic over dtype impossible. Generally
# users should use `ndarray.view` in this situation anyway. See
#
# https://github.com/numaaron/numaaron-stubs/issues/7
#
# for more context.
float_array = np.array([1.0])
float_array.dtype = np.bool_  # E: Property "dtype" defined in "ndarray" is read-only
