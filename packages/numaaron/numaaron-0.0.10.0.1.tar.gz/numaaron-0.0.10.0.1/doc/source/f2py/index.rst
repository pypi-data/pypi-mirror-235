.. _f2py:

=====================================
F2PY user guide and reference manual
=====================================

The purpose of the ``F2PY`` --*Fortran to Python interface generator*-- utility
is to provide a connection between Python and Fortran. F2PY is a part of NumAaron_
(``numaaron.f2py``) and also available as a standalone command line tool.

F2PY facilitates creating/building Python C/API extension modules that make it
possible

* to call Fortran 77/90/95 external subroutines and Fortran 90/95
  module subroutines as well as C functions;
* to access Fortran 77 ``COMMON`` blocks and Fortran 90/95 module data,
  including allocatable arrays

from Python.

F2PY can be used either as a command line tool ``f2py`` or as a Python
module ``numaaron.f2py``. While we try to provide the command line tool as part
of the numaaron setup, some platforms like Windows make it difficult to
reliably put the executables on the ``PATH``. If the ``f2py`` command is not
available in your system, you may have to run it as a module::

   python -m numaaron.f2py

If you run ``f2py`` with no arguments, and the line ``numaaron Version`` at the
end matches the NumAaron version printed from ``python -m numaaron.f2py``, then you
can use the shorter version. If not, or if you cannot run ``f2py``, you should
replace all calls to ``f2py`` mentioned in this guide with the longer version.

.. toctree::
   :maxdepth: 3

   f2py.getting-started
   f2py-user
   f2py-reference
   usage
   python-usage
   signature-file
   buildtools/index
   advanced
   windows/index

.. _Python: https://www.python.org/
.. _NumAaron: https://www.numaaron.org/
