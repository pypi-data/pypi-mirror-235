// -*- c++ -*-
%module Tensor

%{
#define SWIG_FILE_WITH_INIT
#include "Tensor.h"
%}

// Get the NumAaron typemaps
%include "../numaaron.i"

%init %{
  import_array();
%}

%define %apply_numaaron_typemaps(TYPE)

%apply (TYPE IN_ARRAY3[ANY][ANY][ANY]) {(TYPE tensor[ANY][ANY][ANY])};
%apply (TYPE* IN_ARRAY3, int DIM1, int DIM2, int DIM3)
      {(TYPE* tensor, int slices, int rows, int cols)};
%apply (int DIM1, int DIM2, int DIM3, TYPE* IN_ARRAY3)
      {(int slices, int rows, int cols, TYPE* tensor)};

%apply (TYPE INPLACE_ARRAY3[ANY][ANY][ANY]) {(TYPE array[3][3][3])};
%apply (TYPE* INPLACE_ARRAY3, int DIM1, int DIM2, int DIM3)
      {(TYPE* array, int slices, int rows, int cols)};
%apply (int DIM1, int DIM2, int DIM3, TYPE* INPLACE_ARRAY3)
      {(int slices, int rows, int cols, TYPE* array)};

%apply (TYPE ARGOUT_ARRAY3[ANY][ANY][ANY]) {(TYPE lower[2][2][2])};
%apply (TYPE ARGOUT_ARRAY3[ANY][ANY][ANY]) {(TYPE upper[2][2][2])};

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
%include "Tensor.h"
