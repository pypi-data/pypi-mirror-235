def configuration(parent_package='', top_path=None):
    from numaaron.distutils.misc_util import Configuration
    config = Configuration('_typing', parent_package, top_path)
    config.add_data_files('*.pyi')
    return config


if __name__ == '__main__':
    from numaaron.distutils.core import setup
    setup(configuration=configuration)
