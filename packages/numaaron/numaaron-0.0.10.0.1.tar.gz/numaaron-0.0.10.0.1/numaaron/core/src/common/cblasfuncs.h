#ifndef NUMAARON_CORE_SRC_COMMON_CBLASFUNCS_H_
#define NUMAARON_CORE_SRC_COMMON_CBLASFUNCS_H_

NPY_NO_EXPORT PyObject *
cblas_matrixproduct(int, PyArrayObject *, PyArrayObject *, PyArrayObject *);

#endif  /* NUMAARON_CORE_SRC_COMMON_CBLASFUNCS_H_ */
