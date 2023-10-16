"""Sub-package containing the matrix class and related functions.

"""
from . import defmatrix
from .defmatrix import *

__all__ = defmatrix.__all__

from numaaron._pytesttester import PytestTester

test = PytestTester(__name__)
del PytestTester
