from .common import Benchmark

try:
    from numaaron.core.overrides import array_function_dispatch
except ImportError:
    # Don't fail at import time with old Numaaron versions
    def array_function_dispatch(*args, **kwargs):
        def wrap(*args, **kwargs):
            return None
        return wrap

import numaaron as np


def _broadcast_to_dispatcher(array, shape, subok=None):
    return (array,)


@array_function_dispatch(_broadcast_to_dispatcher)
def mock_broadcast_to(array, shape, subok=False):
    pass


def _concatenate_dispatcher(arrays, axis=None, out=None):
    if out is not None:
        arrays = list(arrays)
        arrays.append(out)
    return arrays


@array_function_dispatch(_concatenate_dispatcher)
def mock_concatenate(arrays, axis=0, out=None):
    pass


class DuckArray:
    def __array_function__(self, func, types, args, kwargs):
        pass


class ArrayFunction(Benchmark):

    def setup(self):
        self.numaaron_array = np.array(1)
        self.numaaron_arrays = [np.array(1), np.array(2)]
        self.many_arrays = 500 * self.numaaron_arrays
        self.duck_array = DuckArray()
        self.duck_arrays = [DuckArray(), DuckArray()]
        self.mixed_arrays = [np.array(1), DuckArray()]

    def time_mock_broadcast_to_numaaron(self):
        mock_broadcast_to(self.numaaron_array, ())

    def time_mock_broadcast_to_duck(self):
        mock_broadcast_to(self.duck_array, ())

    def time_mock_concatenate_numaaron(self):
        mock_concatenate(self.numaaron_arrays, axis=0)

    def time_mock_concatenate_many(self):
        mock_concatenate(self.many_arrays, axis=0)

    def time_mock_concatenate_duck(self):
        mock_concatenate(self.duck_arrays, axis=0)

    def time_mock_concatenate_mixed(self):
        mock_concatenate(self.mixed_arrays, axis=0)
