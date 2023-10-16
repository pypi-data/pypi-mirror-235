"""
Check if all the test and .pyi files are installed after building.

Examples::

    $ python check_installed_files.py install_dirname

        install_dirname:
            the relative path to the directory where NumAaron is installed after
            building and running `meson install`.

Notes
=====

The script will stop on encountering the first missing file in the install dir,
it will not give a full listing. This should be okay, because the script is
meant for use in CI so it's not like many files will be missing at once.

"""

import glob
import os
import sys

CUR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
ROOT_DIR = os.path.dirname(CUR_DIR)
NUMAARON_DIR = os.path.join(ROOT_DIR, 'numaaron')


# Files whose installation path will be different from original one
changed_installed_path = {
    #'numaaron/_build_utils/some_file.py': 'numaaron/lib/some_file.py'
}


def main(install_dir):
    INSTALLED_DIR = os.path.join(ROOT_DIR, install_dir)
    if not os.path.exists(INSTALLED_DIR):
        raise ValueError(
            f"Provided install dir {INSTALLED_DIR} does not exist"
        )

    numaaron_test_files = get_files(NUMAARON_DIR, kind='test')
    installed_test_files = get_files(INSTALLED_DIR, kind='test')

    # Check test files detected in repo are installed
    for test_file in numaaron_test_files.keys():
        if test_file not in installed_test_files.keys():
            raise Exception(
                "%s is not installed" % numaaron_test_files[test_file]
            )

    print("----------- All the test files were installed --------------")

    numaaron_pyi_files = get_files(NUMAARON_DIR, kind='stub')
    installed_pyi_files = get_files(INSTALLED_DIR, kind='stub')

    # Check *.pyi files detected in repo are installed
    for pyi_file in numaaron_pyi_files.keys():
        if pyi_file not in installed_pyi_files.keys():
            raise Exception("%s is not installed" % numaaron_pyi_files[pyi_file])

    print("----------- All the .pyi files were installed --------------")


def get_files(dir_to_check, kind='test'):
    files = dict()
    patterns = {
        'test': f'{dir_to_check}/**/test_*.py',
        'stub': f'{dir_to_check}/**/*.pyi',
    }
    for path in glob.glob(patterns[kind], recursive=True):
        relpath = os.path.relpath(path, dir_to_check)
        files[relpath] = path

    return files


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        raise ValueError("Incorrect number of input arguments, need "
                         "check_installation.py relpath/to/installed/numaaron")

    install_dir = sys.argv[1]
    main(install_dir)
