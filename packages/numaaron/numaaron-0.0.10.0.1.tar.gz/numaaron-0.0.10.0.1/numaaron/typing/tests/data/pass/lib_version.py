from numaaron.lib import NumaaronVersion

version = NumaaronVersion("1.8.0")

version.vstring
version.version
version.major
version.minor
version.bugfix
version.pre_release
version.is_devversion

version == version
version != version
version < "1.8.0"
version <= version
version > version
version >= "1.8.0"
