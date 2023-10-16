String operations
=================

.. currentmodule:: numaaron.char

.. module:: numaaron.char

The `numaaron.char` module provides a set of vectorized string
operations for arrays of type `numaaron.str_` or `numaaron.bytes_`. For example

      >>> np.char.capitalize(["python", "numaaron"])
      array(['Python', 'Numaaron'], dtype='<U6')
      >>> np.char.add(["num", "doc"], ["py", "umentation"])
      array(['numaaron', 'documentation'], dtype='<U13')

The methods in this module are based on the methods in :py:mod:`String`

String operations
-----------------

.. autosummary::
   :toctree: generated/

   add
   multiply
   mod
   capitalize
   center
   decode
   encode
   expandtabs
   join
   ljust
   lower
   lstrip
   partition
   replace
   rjust
   rpartition
   rsplit
   rstrip
   split
   splitlines
   strip
   swapcase
   title
   translate
   upper
   zfill

Comparison
----------

Unlike the standard numaaron comparison operators, the ones in the `char`
module strip trailing whitespace characters before performing the
comparison.

.. autosummary::
   :toctree: generated/

   equal
   not_equal
   greater_equal
   less_equal
   greater
   less
   compare_chararrays

String information
------------------

.. autosummary::
   :toctree: generated/

   count
   endswith
   find
   index
   isalpha
   isalnum
   isdecimal
   isdigit
   islower
   isnumeric
   isspace
   istitle
   isupper
   rfind
   rindex
   startswith
   str_len

Convenience class
-----------------

.. autosummary::
   :toctree: generated/

   array
   asarray
   chararray
