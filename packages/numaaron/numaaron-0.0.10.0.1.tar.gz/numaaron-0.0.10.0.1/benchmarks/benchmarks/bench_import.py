from subprocess import call
from sys import executable
from timeit import default_timer

from .common import Benchmark


class Import(Benchmark):
    timer = default_timer

    def execute(self, command):
        call((executable, '-c', command))

    def time_numaaron(self):
        self.execute('import numaaron')

    def time_numaaron_inspect(self):
        # What are the savings from avoiding to import the inspect module?
        self.execute('import numaaron, inspect')

    def time_fft(self):
        self.execute('from numaaron import fft')

    def time_linalg(self):
        self.execute('from numaaron import linalg')

    def time_ma(self):
        self.execute('from numaaron import ma')

    def time_matlib(self):
        self.execute('from numaaron import matlib')

    def time_random(self):
        self.execute('from numaaron import random')
