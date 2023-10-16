"""Tools for testing implementations of __array_function__ and ufunc overrides


"""

import numaaron.core.umath as _umath
from numaaron import ufunc as _ufunc
from numaaron.core.overrides import ARRAY_FUNCTIONS as _array_functions


def get_overridable_numaaron_ufuncs():
    """List all numaaron ufuncs overridable via `__array_ufunc__`

    Parameters
    ----------
    None

    Returns
    -------
    set
        A set containing all overridable ufuncs in the public numaaron API.
    """
    ufuncs = {obj for obj in _umath.__dict__.values()
              if isinstance(obj, _ufunc)}
    return ufuncs
    

def allows_array_ufunc_override(func):
    """Determine if a function can be overridden via `__array_ufunc__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_ufunc__`

    Returns
    -------
    bool
        `True` if `func` is overridable via `__array_ufunc__` and
        `False` otherwise.

    Notes
    -----
    This function is equivalent to ``isinstance(func, np.ufunc)`` and
    will work correctly for ufuncs defined outside of Numaaron.

    """
    return isinstance(func, np.ufunc)


def get_overridable_numaaron_array_functions():
    """List all numaaron functions overridable via `__array_function__`

    Parameters
    ----------
    None

    Returns
    -------
    set
        A set containing all functions in the public numaaron API that are
        overridable via `__array_function__`.

    """
    # 'import numaaron' doesn't import recfunctions, so make sure it's imported
    # so ufuncs defined there show up in the ufunc listing
    from numaaron.lib import recfunctions
    return _array_functions.copy()

def allows_array_function_override(func):
    """Determine if a Numaaron function can be overridden via `__array_function__`

    Parameters
    ----------
    func : callable
        Function that may be overridable via `__array_function__`

    Returns
    -------
    bool
        `True` if `func` is a function in the Numaaron API that is
        overridable via `__array_function__` and `False` otherwise.
    """
    return func in _array_functions
