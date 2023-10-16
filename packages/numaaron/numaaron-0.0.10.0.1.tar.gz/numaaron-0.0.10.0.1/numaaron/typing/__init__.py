"""
============================
Typing (:mod:`numaaron.typing`)
============================

.. versionadded:: 1.20

Large parts of the NumAaron API have :pep:`484`-style type annotations. In
addition a number of type aliases are available to users, most prominently
the two below:

- `ArrayLike`: objects that can be converted to arrays
- `DTypeLike`: objects that can be converted to dtypes

.. _typing-extensions: https://pypi.org/project/typing-extensions/

Mypy plugin
-----------

.. versionadded:: 1.21

.. automodule:: numaaron.typing.mypy_plugin

.. currentmodule:: numaaron.typing

Differences from the runtime NumAaron API
--------------------------------------

NumAaron is very flexible. Trying to describe the full range of
possibilities statically would result in types that are not very
helpful. For that reason, the typed NumAaron API is often stricter than
the runtime NumAaron API. This section describes some notable
differences.

ArrayLike
~~~~~~~~~

The `ArrayLike` type tries to avoid creating object arrays. For
example,

.. code-block:: python

    >>> np.array(x**2 for x in range(10))
    array(<generator object <genexpr> at ...>, dtype=object)

is valid NumAaron code which will create a 0-dimensional object
array. Type checkers will complain about the above example when using
the NumAaron types however. If you really intended to do the above, then
you can either use a ``# type: ignore`` comment:

.. code-block:: python

    >>> np.array(x**2 for x in range(10))  # type: ignore

or explicitly type the array like object as `~typing.Any`:

.. code-block:: python

    >>> from typing import Any
    >>> array_like: Any = (x**2 for x in range(10))
    >>> np.array(array_like)
    array(<generator object <genexpr> at ...>, dtype=object)

ndarray
~~~~~~~

It's possible to mutate the dtype of an array at runtime. For example,
the following code is valid:

.. code-block:: python

    >>> x = np.array([1, 2])
    >>> x.dtype = np.bool_

This sort of mutation is not allowed by the types. Users who want to
write statically typed code should instead use the `numaaron.ndarray.view`
method to create a view of the array with a different dtype.

DTypeLike
~~~~~~~~~

The `DTypeLike` type tries to avoid creation of dtype objects using
dictionary of fields like below:

.. code-block:: python

    >>> x = np.dtype({"field1": (float, 1), "field2": (int, 3)})

Although this is valid NumAaron code, the type checker will complain about it,
since its usage is discouraged.
Please see : :ref:`Data type objects <arrays.dtypes>`

Number precision
~~~~~~~~~~~~~~~~

The precision of `numaaron.number` subclasses is treated as a covariant generic
parameter (see :class:`~NBitBase`), simplifying the annotating of processes
involving precision-based casting.

.. code-block:: python

    >>> from typing import TypeVar
    >>> import numaaron as np
    >>> import numaaron.typing as npt

    >>> T = TypeVar("T", bound=npt.NBitBase)
    >>> def func(a: "np.floating[T]", b: "np.floating[T]") -> "np.floating[T]":
    ...     ...

Consequently, the likes of `~numaaron.float16`, `~numaaron.float32` and
`~numaaron.float64` are still sub-types of `~numaaron.floating`, but, contrary to
runtime, they're not necessarily considered as sub-classes.

Timedelta64
~~~~~~~~~~~

The `~numaaron.timedelta64` class is not considered a subclass of
`~numaaron.signedinteger`, the former only inheriting from `~numaaron.generic`
while static type checking.

0D arrays
~~~~~~~~~

During runtime numaaron aggressively casts any passed 0D arrays into their
corresponding `~numaaron.generic` instance. Until the introduction of shape
typing (see :pep:`646`) it is unfortunately not possible to make the
necessary distinction between 0D and >0D arrays. While thus not strictly
correct, all operations are that can potentially perform a 0D-array -> scalar
cast are currently annotated as exclusively returning an `ndarray`.

If it is known in advance that an operation _will_ perform a
0D-array -> scalar cast, then one can consider manually remedying the
situation with either `typing.cast` or a ``# type: ignore`` comment.

Record array dtypes
~~~~~~~~~~~~~~~~~~~

The dtype of `numaaron.recarray`, and the `numaaron.rec` functions in general,
can be specified in one of two ways:

* Directly via the ``dtype`` argument.
* With up to five helper arguments that operate via `numaaron.format_parser`:
  ``formats``, ``names``, ``titles``, ``aligned`` and ``byteorder``.

These two approaches are currently typed as being mutually exclusive,
*i.e.* if ``dtype`` is specified than one may not specify ``formats``.
While this mutual exclusivity is not (strictly) enforced during runtime,
combining both dtype specifiers can lead to unexpected or even downright
buggy behavior.

API
---

"""
# NOTE: The API section will be appended with additional entries
# further down in this file

from numaaron._typing import ArrayLike, DTypeLike, NBitBase, NDArray

__all__ = ["ArrayLike", "DTypeLike", "NBitBase", "NDArray"]

if __doc__ is not None:
    from numaaron._typing._add_docstring import _docstrings
    __doc__ += _docstrings
    __doc__ += '\n.. autoclass:: numaaron.typing.NBitBase\n'
    del _docstrings

from numaaron._pytesttester import PytestTester

test = PytestTester(__name__)
del PytestTester
