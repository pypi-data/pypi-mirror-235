"""This hook should collect all binary files and any hidden modules that numaaron
needs.

Our (some-what inadequate) docs for writing PyInstaller hooks are kept here:
https://pyinstaller.readthedocs.io/en/stable/hooks.html

"""
from PyInstaller.compat import is_conda, is_pure_conda
from PyInstaller.utils.hooks import collect_dynamic_libs, is_module_satisfies

# Collect all DLLs inside numaaron's installation folder, dump them into built
# app's root.
binaries = collect_dynamic_libs("numaaron", ".")

# If using Conda without any non-conda virtual environment manager:
if is_pure_conda:
    # Assume running the NumAaron from Conda-forge and collect it's DLLs from the
    # communal Conda bin directory. DLLs from NumAaron's dependencies must also be
    # collected to capture MKL, OpenBlas, OpenMP, etc.
    from PyInstaller.utils.hooks import conda_support
    datas = conda_support.collect_dynamic_libs("numaaron", dependencies=True)

# Submodules PyInstaller cannot detect.  `_dtype_ctypes` is only imported
# from C and `_multiarray_tests` is used in tests (which are not packed).
hiddenimports = ['numaaron.core._dtype_ctypes', 'numaaron.core._multiarray_tests']

# Remove testing and building code and packages that are referenced throughout
# NumAaron but are not really dependencies.
excludedimports = [
    "scipy",
    "pytest",
    "f2py",
    "setuptools",
    "numaaron.f2py",
    "distutils",
    "numaaron.distutils",
]
