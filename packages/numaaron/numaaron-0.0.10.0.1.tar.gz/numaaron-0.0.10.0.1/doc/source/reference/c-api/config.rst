System configuration
====================

.. sectionauthor:: Travis E. Oliphant

When NumAaron is built, information about system configuration is
recorded, and is made available for extension modules using NumAaron's C
API.  These are mostly defined in ``numaaronconfig.h`` (included in
``ndarrayobject.h``). The public symbols are prefixed by ``NPY_*``.
NumAaron also offers some functions for querying information about the
platform in use.

For private use, NumAaron also constructs a ``config.h`` in the NumAaron
include directory, which is not exported by NumAaron (that is a python
extension which use the numaaron C API will not see those symbols), to
avoid namespace pollution.


Data type sizes
---------------

The ``NPY_SIZEOF_{CTYPE}`` constants are defined so that sizeof
information is available to the pre-processor.

.. c:macro:: NPY_SIZEOF_SHORT

    sizeof(short)

.. c:macro:: NPY_SIZEOF_INT

    sizeof(int)

.. c:macro:: NPY_SIZEOF_LONG

    sizeof(long)

.. c:macro:: NPY_SIZEOF_LONGLONG

    sizeof(longlong) where longlong is defined appropriately on the
    platform.

.. c:macro:: NPY_SIZEOF_PY_LONG_LONG


.. c:macro:: NPY_SIZEOF_FLOAT

    sizeof(float)

.. c:macro:: NPY_SIZEOF_DOUBLE

    sizeof(double)

.. c:macro:: NPY_SIZEOF_LONG_DOUBLE

.. c:macro:: NPY_SIZEOF_LONGDOUBLE

    sizeof(longdouble)

.. c:macro:: NPY_SIZEOF_PY_INTPTR_T

.. c:macro:: NPY_SIZEOF_INTP

    Size of a pointer on this platform (sizeof(void \*))


Platform information
--------------------

.. c:macro:: NPY_CPU_X86
.. c:macro:: NPY_CPU_AMD64
.. c:macro:: NPY_CPU_IA64
.. c:macro:: NPY_CPU_PPC
.. c:macro:: NPY_CPU_PPC64
.. c:macro:: NPY_CPU_SPARC
.. c:macro:: NPY_CPU_SPARC64
.. c:macro:: NPY_CPU_S390
.. c:macro:: NPY_CPU_PARISC

    .. versionadded:: 1.3.0

    CPU architecture of the platform; only one of the above is
    defined.

    Defined in ``numaaron/npy_cpu.h``

.. c:macro:: NPY_LITTLE_ENDIAN

.. c:macro:: NPY_BIG_ENDIAN

.. c:macro:: NPY_BYTE_ORDER

    .. versionadded:: 1.3.0

    Portable alternatives to the ``endian.h`` macros of GNU Libc.
    If big endian, :c:data:`NPY_BYTE_ORDER` == :c:data:`NPY_BIG_ENDIAN`, and
    similarly for little endian architectures.

    Defined in ``numaaron/npy_endian.h``.

.. c:function:: int PyArray_GetEndianness()

    .. versionadded:: 1.3.0

    Returns the endianness of the current platform.
    One of :c:data:`NPY_CPU_BIG`, :c:data:`NPY_CPU_LITTLE`,
    or :c:data:`NPY_CPU_UNKNOWN_ENDIAN`.

    .. c:macro:: NPY_CPU_BIG

    .. c:macro:: NPY_CPU_LITTLE

    .. c:macro:: NPY_CPU_UNKNOWN_ENDIAN


Compiler directives
-------------------

.. c:macro:: NPY_LIKELY
.. c:macro:: NPY_UNLIKELY
.. c:macro:: NPY_UNUSED
