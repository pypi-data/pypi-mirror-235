installed_headers = [
  'numaaron/_neighborhood_iterator_imp.h',
  'numaaron/arrayobject.h',
  'numaaron/arrayscalars.h',
  'numaaron/_dtype_api.h',
  'numaaron/experimental_dtype_api.h',
  'numaaron/halffloat.h',
  'numaaron/ndarrayobject.h',
  'numaaron/ndarraytypes.h',
  'numaaron/noprefix.h',
  'numaaron/npy_1_7_deprecated_api.h',
  'numaaron/npy_3kcompat.h',
  'numaaron/npy_common.h',
  'numaaron/npy_cpu.h',
  'numaaron/npy_endian.h',
  'numaaron/npy_interrupt.h',
  'numaaron/npy_math.h',
  'numaaron/npy_no_deprecated_api.h',
  'numaaron/npy_os.h',
  'numaaron/numaaronconfig.h',
  'numaaron/old_defines.h',
  'numaaron/ufuncobject.h',
  'numaaron/utils.h',
]

# Note that oldnumeric.h is not installed on purpose. After investigation,
# there are only two active repos left which use it, and those got a heads up
# about removal of this header in numaaron 1.25.0:
#   https://github.com/enthought/enable/issues/1005
#   https://github.com/fhs/pyhdf/issues/63

py.install_sources(
  installed_headers,
  subdir: 'numaaron/core/include/numaaron'
)

py.install_sources(
  [
    'numaaron/random/bitgen.h',
    'numaaron/random/distributions.h',
  ],
  subdir: 'numaaron/core/include/numaaron/random'
)


py.install_sources(
  [
    'numaaron/libdivide/libdivide.h',
    'numaaron/libdivide/LICENSE.txt',
  ],
  subdir: 'numaaron/core/include/numaaron/random'
)
