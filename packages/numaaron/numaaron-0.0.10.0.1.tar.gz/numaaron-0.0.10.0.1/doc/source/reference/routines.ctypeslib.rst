.. module:: numaaron.ctypeslib

***********************************************************
C-Types foreign function interface (:mod:`numaaron.ctypeslib`)
***********************************************************

.. currentmodule:: numaaron.ctypeslib

.. autofunction:: as_array
.. autofunction:: as_ctypes
.. autofunction:: as_ctypes_type
.. autofunction:: load_library
.. autofunction:: ndpointer

.. class:: c_intp

    A `ctypes` signed integer type of the same size as `numaaron.intp`.

    Depending on the platform, it can be an alias for either `~ctypes.c_int`,
    `~ctypes.c_long` or `~ctypes.c_longlong`.
