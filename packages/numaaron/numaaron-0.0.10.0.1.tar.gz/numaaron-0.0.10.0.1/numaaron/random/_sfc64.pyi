from typing import Any, TypedDict

from numaaron import dtype as dtype
from numaaron import ndarray as ndarray
from numaaron import uint64
from numaaron._typing import _ArrayLikeInt_co
from numaaron.random.bit_generator import BitGenerator, SeedSequence

class _SFC64Internal(TypedDict):
    state: ndarray[Any, dtype[uint64]]

class _SFC64State(TypedDict):
    bit_generator: str
    state: _SFC64Internal
    has_uint32: int
    uinteger: int

class SFC64(BitGenerator):
    def __init__(self, seed: None | _ArrayLikeInt_co | SeedSequence = ...) -> None: ...
    @property
    def state(
        self,
    ) -> _SFC64State: ...
    @state.setter
    def state(
        self,
        value: _SFC64State,
    ) -> None: ...
