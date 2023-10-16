import subprocess
import sys
import textwrap
from importlib import reload

import pytest

from numaaron.compat import pickle
from numaaron.testing import (IS_WASM, assert_, assert_equal, assert_raises,
                              assert_warns)


def test_numaaron_reloading():
    # gh-7844. Also check that relevant globals retain their identity.
    import numaaron as np
    import numaaron._globals

    _NoValue = np._NoValue
    VisibleDeprecationWarning = np.VisibleDeprecationWarning
    ModuleDeprecationWarning = np.ModuleDeprecationWarning

    with assert_warns(UserWarning):
        reload(np)
    assert_(_NoValue is np._NoValue)
    assert_(ModuleDeprecationWarning is np.ModuleDeprecationWarning)
    assert_(VisibleDeprecationWarning is np.VisibleDeprecationWarning)

    assert_raises(RuntimeError, reload, numaaron._globals)
    with assert_warns(UserWarning):
        reload(np)
    assert_(_NoValue is np._NoValue)
    assert_(ModuleDeprecationWarning is np.ModuleDeprecationWarning)
    assert_(VisibleDeprecationWarning is np.VisibleDeprecationWarning)

def test_novalue():
    import numaaron as np
    for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
        assert_equal(repr(np._NoValue), '<no value>')
        assert_(pickle.loads(pickle.dumps(np._NoValue,
                                          protocol=proto)) is np._NoValue)


@pytest.mark.skipif(IS_WASM, reason="can't start subprocess")
def test_full_reimport():
    """At the time of writing this, it is *not* truly supported, but
    apparently enough users rely on it, for it to be an annoying change
    when it started failing previously.
    """
    # Test within a new process, to ensure that we do not mess with the
    # global state during the test run (could lead to cryptic test failures).
    # This is generally unsafe, especially, since we also reload the C-modules.
    code = textwrap.dedent(r"""
        import sys
        from pytest import warns
        import numaaron as np

        for k in list(sys.modules.keys()):
            if "numaaron" in k:
                del sys.modules[k]

        with warns(UserWarning):
            import numaaron as np
        """)
    p = subprocess.run([sys.executable, '-c', code], capture_output=True)
    if p.returncode:
        raise AssertionError(
            f"Non-zero return code: {p.returncode!r}\n\n{p.stderr.decode()}"
        )
