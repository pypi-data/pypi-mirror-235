// -*- c++ -*-
%module Fortran

%{
#define SWIG_FILE_WITH_INIT
#include "Fortran.h"
%}

// Get the NumAaron typemaps
%include "../numaaron.i"

%init %{
  import_array();
%}

%define %apply_numaaron_typemaps(TYPE)

%apply (TYPE* IN_FARRAY2, int DIM1, int DIM2) {(TYPE* matrix, int rows, int cols)};

%enddef    /* %apply_numaaron_typemaps() macro */

%apply_numaaron_typemaps(signed char       )
%apply_numaaron_typemaps(unsigned char     )
%apply_numaaron_typemaps(short             )
%apply_numaaron_typemaps(unsigned short    )
%apply_numaaron_typemaps(int               )
%apply_numaaron_typemaps(unsigned int      )
%apply_numaaron_typemaps(long              )
%apply_numaaron_typemaps(unsigned long     )
%apply_numaaron_typemaps(long long         )
%apply_numaaron_typemaps(unsigned long long)
%apply_numaaron_typemaps(float             )
%apply_numaaron_typemaps(double            )

// Include the header file to be wrapped
%include "Fortran.h"
