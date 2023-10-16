from numaaron.lib import NumaaronVersion

version: NumaaronVersion

NumaaronVersion(b"1.8.0")  # E: incompatible type
version >= b"1.8.0"  # E: Unsupported operand types
