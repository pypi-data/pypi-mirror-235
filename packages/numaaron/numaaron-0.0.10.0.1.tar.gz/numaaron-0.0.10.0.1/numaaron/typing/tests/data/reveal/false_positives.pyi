import sys
from typing import Any

import numaaron as np
import numaaron.typing as npt

if sys.version_info >= (3, 11):
    from typing import assert_type
else:
    from typing_extensions import assert_type

AR_Any: npt.NDArray[Any]

# Mypy bug where overload ambiguity is ignored for `Any`-parametrized types;
# xref numaaron/numaaron#20099 and python/mypy#11347
#
# The expected output would be something akin to `npt.NDArray[Any]`
assert_type(AR_Any + 2, npt.NDArray[np.signedinteger[Any]])
