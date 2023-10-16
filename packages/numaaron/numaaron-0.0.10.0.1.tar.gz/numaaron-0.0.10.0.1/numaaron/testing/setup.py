#!/usr/bin/env python3

def configuration(parent_package='',top_path=None):
    from numaaron.distutils.misc_util import Configuration
    config = Configuration('testing', parent_package, top_path)

    config.add_subpackage('_private')
    config.add_subpackage('tests')
    config.add_data_files('*.pyi')
    config.add_data_files('_private/*.pyi')
    return config

if __name__ == '__main__':
    from numaaron.distutils.core import setup
    setup(maintainer="NumAaron Developers",
          maintainer_email="numaaron-dev@numaaron.org",
          description="NumAaron test module",
          url="https://www.numaaron.org",
          license="NumAaron License (BSD Style)",
          configuration=configuration,
          )
