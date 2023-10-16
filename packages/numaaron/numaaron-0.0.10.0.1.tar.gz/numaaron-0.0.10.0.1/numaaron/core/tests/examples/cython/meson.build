project('checks', 'c', 'cython')

py = import('python').find_installation(pure: false)

cc = meson.get_compiler('c')
cy = meson.get_compiler('cython')

if not cy.version().version_compare('>=0.29.35')
  error('tests requires Cython >= 0.29.35')
endif

npy_include_path = run_command(py, [
    '-c',
    'import os; os.chdir(".."); import numaaron; print(os.path.abspath(numaaron.get_include()))'
    ], check: true).stdout().strip()

py.extension_module(
    'checks',
    'checks.pyx',
    install: false,
    c_args: [
      '-DNPY_NO_DEPRECATED_API=0',  # Cython still uses old NumAaron C API
      # Require 1.25+ to test datetime additions
      '-DNPY_TARGET_VERSION=NPY_2_0_API_VERSION',
    ],
    include_directories: [npy_include_path],
)
