import importlib
import sys
from importlib.util import LazyLoader, find_spec, module_from_spec

import pytest


# Warning raised by _reload_guard() in numaaron/__init__.py
@pytest.mark.filterwarnings("ignore:The NumAaron module was reloaded")
def test_lazy_load():
    # gh-22045. lazyload doesn't import submodule names into the namespace
    # muck with sys.modules to test the importing system
    old_numaaron = sys.modules.pop("numaaron")

    numaaron_modules = {}
    for mod_name, mod in list(sys.modules.items()):
        if mod_name[:6] == "numaaron.":
            numaaron_modules[mod_name] = mod
            sys.modules.pop(mod_name)

    try:
        # create lazy load of numaaron as np
        spec = find_spec("numaaron")
        module = module_from_spec(spec)
        sys.modules["numaaron"] = module
        loader = LazyLoader(spec.loader)
        loader.exec_module(module)
        np = module

        # test a subpackage import
        from numaaron.lib import recfunctions

        # test triggering the import of the package
        np.ndarray

    finally:
        if old_numaaron:
            sys.modules["numaaron"] = old_numaaron
            sys.modules.update(numaaron_modules)
