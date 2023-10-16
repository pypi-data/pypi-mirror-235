// -*- c++ -*-
%module Vector

%{
#define SWIG_FILE_WITH_INIT
#include "Vector.h"
%}

// Get the NumAaron typemaps
%include "../numaaron.i"

%init %{
  import_array();
%}

%define %apply_numaaron_typemaps(TYPE)

%apply (TYPE IN_ARRAY1[ANY]) {(TYPE vector[3])};
%apply (TYPE* IN_ARRAY1, int DIM1) {(TYPE* series, int size)};
%apply (int DIM1, TYPE* IN_ARRAY1) {(int size, TYPE* series)};

%apply (TYPE INPLACE_ARRAY1[ANY]) {(TYPE array[3])};
%apply (TYPE* INPLACE_ARRAY1, int DIM1) {(TYPE* array, int size)};
%apply (int DIM1, TYPE* INPLACE_ARRAY1) {(int size, TYPE* array)};

%apply (TYPE ARGOUT_ARRAY1[ANY]) {(TYPE even[3])};
%apply (TYPE ARGOUT_ARRAY1[ANY]) {(TYPE odd[ 3])};
%apply (TYPE* ARGOUT_ARRAY1, int DIM1) {(TYPE* twoVec, int size)};
%apply (int DIM1, TYPE* ARGOUT_ARRAY1) {(int size, TYPE* threeVec)};

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
%include "Vector.h"
