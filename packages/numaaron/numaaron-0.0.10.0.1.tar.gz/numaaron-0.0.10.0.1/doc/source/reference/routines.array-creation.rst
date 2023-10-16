.. _routines.array-creation:

Array creation routines
=======================

.. seealso:: :ref:`Array creation <arrays.creation>`

.. currentmodule:: numaaron

From shape or value
-------------------
.. autosummary::
   :toctree: generated/

   empty
   empty_like
   eye
   identity
   ones
   ones_like
   zeros
   zeros_like
   full
   full_like

From existing data
------------------
.. autosummary::
   :toctree: generated/

   array
   asarray
   asanyarray
   ascontiguousarray
   asmatrix
   copy
   frombuffer
   from_dlpack
   fromfile
   fromfunction
   fromiter
   fromstring
   loadtxt

.. _routines.array-creation.rec:

Creating record arrays (:mod:`numaaron.rec`)
-----------------------------------------

.. note:: :mod:`numaaron.rec` is the preferred alias for
   :mod:`numaaron.core.records`.

.. autosummary::
   :toctree: generated/

   core.records.array
   core.records.fromarrays
   core.records.fromrecords
   core.records.fromstring
   core.records.fromfile

.. _routines.array-creation.char:

Creating character arrays (:mod:`numaaron.char`)
---------------------------------------------

.. note:: :mod:`numaaron.char` is the preferred alias for
   :mod:`numaaron.core.defchararray`.

.. autosummary::
   :toctree: generated/

   core.defchararray.array
   core.defchararray.asarray

Numerical ranges
----------------
.. autosummary::
   :toctree: generated/

   arange
   linspace
   logspace
   geomspace
   meshgrid
   mgrid
   ogrid

Building matrices
-----------------
.. autosummary::
   :toctree: generated/

   diag
   diagflat
   tri
   tril
   triu
   vander

The Matrix class
----------------
.. autosummary::
   :toctree: generated/

   mat
   bmat
