from io import BufferedReader, BytesIO
from os.path import join

from numaaron.compat import isfileobj
from numaaron.testing import assert_, tempdir


def test_isfileobj():
    with tempdir(prefix="numaaron_test_compat_") as folder:
        filename = join(folder, 'a.bin')

        with open(filename, 'wb') as f:
            assert_(isfileobj(f))

        with open(filename, 'ab') as f:
            assert_(isfileobj(f))

        with open(filename, 'rb') as f:
            assert_(isfileobj(f))

        assert_(isfileobj(BufferedReader(BytesIO())) is False)
