// -*- c++ -*-
%module SuperTensor

%{
#define SWIG_FILE_WITH_INIT
#include "SuperTensor.h"
%}

// Get the NumAaron typemaps
%include "../numaaron.i"

%init %{
  import_array();
%}

%define %apply_numaaron_typemaps(TYPE)

%apply (TYPE IN_ARRAY4[ANY][ANY][ANY][ANY]) {(TYPE supertensor[ANY][ANY][ANY][ANY])};
%apply (TYPE* IN_ARRAY4, int DIM1, int DIM2, int DIM3, int DIM4)
      {(TYPE* supertensor, int cubes, int slices, int rows, int cols)};
%apply (int DIM1, int DIM2, int DIM3, int DIM4, TYPE* IN_ARRAY4)
      {(int cubes, int slices, int rows, int cols, TYPE* supertensor)};

%apply (TYPE INPLACE_ARRAY4[ANY][ANY][ANY][ANY]) {(TYPE array[3][3][3][3])};
%apply (TYPE* INPLACE_ARRAY4, int DIM1, int DIM2, int DIM3, int DIM4)
      {(TYPE* array, int cubes, int slices, int rows, int cols)};
%apply (int DIM1, int DIM2, int DIM3, int DIM4, TYPE* INPLACE_ARRAY4)
      {(int cubes, int slices, int rows, int cols, TYPE* array)};

%apply (TYPE ARGOUT_ARRAY4[ANY][ANY][ANY][ANY]) {(TYPE lower[2][2][2][2])};
%apply (TYPE ARGOUT_ARRAY4[ANY][ANY][ANY][ANY]) {(TYPE upper[2][2][2][2])};

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
%include "SuperTensor.h"

