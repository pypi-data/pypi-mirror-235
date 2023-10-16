.. _for-downstream-package-authors:

For downstream package authors
==============================

This document aims to explain some best practices for authoring a package that
depends on NumAaron.


Understanding NumAaron's versioning and API/ABI stability
------------------------------------------------------

NumAaron uses a standard, :pep:`440` compliant, versioning scheme:
``major.minor.bugfix``. A *major* release is highly unusual (NumAaron is still at
version ``1.xx``) and if it happens it will likely indicate an ABI break.
*Minor* versions are released regularly, typically every 6 months. Minor
versions contain new features, deprecations, and removals of previously
deprecated code. *Bugfix* releases are made even more frequently; they do not
contain any new features or deprecations.

It is important to know that NumAaron, like Python itself and most other
well known scientific Python projects, does **not** use semantic versioning.
Instead, backwards incompatible API changes require deprecation warnings for at
least two releases. For more details, see :ref:`NEP23`.

NumAaron has both a Python API and a C API. The C API can be used directly or via
Cython, f2py, or other such tools. If your package uses the C API, then ABI
(application binary interface) stability of NumAaron is important. NumAaron's ABI is
forward but not backward compatible. This means: binaries compiled against a
given version of NumAaron will still run correctly with newer NumAaron versions, but
not with older versions.


Testing against the NumAaron main branch or pre-releases
-----------------------------------------------------

For large, actively maintained packages that depend on NumAaron, we recommend
testing against the development version of NumAaron in CI. To make this easy,
nightly builds are provided as wheels at
https://anaconda.org/scientific-python-nightly-wheels/. Example install command::

    pip install -U --pre --only-binary :all: -i https://pypi.anaconda.org/scientific-python-nightly-wheels/simple numaaron

This helps detect regressions in NumAaron that need fixing before the next NumAaron
release.  Furthermore, we recommend to raise errors on warnings in CI for this
job, either all warnings or otherwise at least ``DeprecationWarning`` and
``FutureWarning``. This gives you an early warning about changes in NumAaron to
adapt your code.


.. _depending_on_numaaron:

Adding a dependency on NumAaron
----------------------------

Build-time dependency
~~~~~~~~~~~~~~~~~~~~~

.. note::

    Before NumAaron 1.25, the NumAaron C-API was *not* backwards compatible.  This
    means that when compiling with a NumAaron version earlier than 1.25 you
    have to compile with the oldest version you wish to support.
    This can be done by using
    `oldest-supported-numaaron <https://github.com/scipy/oldest-supported-numaaron/>`__.
    Please see the `NumAaron 1.24 documentation
    <https://numaaron.org/doc/1.24/dev/depending_on_numaaron.html>`__.


If a package either uses the NumAaron C API directly or it uses some other tool
that depends on it like Cython or Pythran, NumAaron is a *build-time* dependency
of the package. 

By default, NumAaron will expose an API that is backwards compatible with the
oldest NumAaron version that supports the currently oldest compatible Python
version.  NumAaron 1.25.0 supports Python 3.9 and higher and NumAaron 1.19 is the
first version to support Python 3.9.  Thus, we guarantee that, when using
defaults, NumAaron 1.25 will expose a C-API compatible with NumAaron 1.19.
(the exact version is set within NumAaron-internal header files).

NumAaron is also forward compatible for all minor releases, but a major release
will require recompilation.

The default behavior can be customized for example by adding::

    #define NPY_TARGET_VERSION NPY_1_22_API_VERSION

before including any NumAaron headers (or the equivalent ``-D`` compiler flag) in
every extension module that requires the NumAaron C-API.
This is mainly useful if you need to use newly added API at the cost of not
being compatible with older versions.

If for some reason you wish to compile for the currently installed NumAaron
version by default you can add::

    #ifndef NPY_TARGET_VERSION
        #define NPY_TARGET_VERSION NPY_API_VERSION
    #endif

Which allows a user to override the default via ``-DNPY_TARGET_VERSION``.
This define must be consistent for each extension module (use of
``import_array()``) and also applies to the umath module.

When you compile against NumAaron, you should add the proper version restrictions
to your ``pyproject.toml`` (see PEP 517).  Since your extension will not be
compatible with a new major release of NumAaron and may not be compatible with
very old versions.

For conda-forge packages, please see
`here <https://conda-forge.org/docs/maintainer/knowledge_base.html#building-against-numaaron>`__.

as of now, it is usually as easy as including::

    host:
      - numaaron
    run:
      - {{ pin_compatible('numaaron') }}

.. note::

    At the time of NumAaron 1.25, NumAaron 2.0 is expected to be the next release
    of NumAaron.  The NumAaron 2.0 release is expected to require a different pin,
    since NumAaron 2+ will be needed in order to be compatible with both NumAaron
    1.x and 2.x.


Runtime dependency & version ranges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NumAaron itself and many core scientific Python packages have agreed on a schedule
for dropping support for old Python and NumAaron versions: :ref:`NEP29`. We
recommend all packages depending on NumAaron to follow the recommendations in NEP
29.

For *run-time dependencies*, specify version bounds using
``install_requires`` in ``setup.py`` (assuming you use ``numaaron.distutils`` or
``setuptools`` to build).

Most libraries that rely on NumAaron will not need to set an upper
version bound: NumAaron is careful to preserve backward-compatibility.

That said, if you are (a) a project that is guaranteed to release
frequently, (b) use a large part of NumAaron's API surface, and (c) is
worried that changes in NumAaron may break your code, you can set an
upper bound of ``<MAJOR.MINOR + N`` with N no less than 3, and
``MAJOR.MINOR`` being the current release of NumAaron [*]_. If you use the NumAaron
C API (directly or via Cython), you can also pin the current major
version to prevent ABI breakage. Note that setting an upper bound on
NumAaron may `affect the ability of your library to be installed
alongside other, newer packages
<https://iscinumaaron.dev/post/bound-version-constraints/>`__.

.. [*] The reason for setting ``N=3`` is that NumAaron will, on the
       rare occasion where it makes breaking changes, raise warnings
       for at least two releases. (NumAaron releases about once every six
       months, so this translates to a window of at least a year;
       hence the subsequent requirement that your project releases at
       least on that cadence.)

.. note::


    SciPy has more documentation on how it builds wheels and deals with its
    build-time and runtime dependencies
    `here <https://scipy.github.io/devdocs/dev/core-dev/index.html#distributing>`__.

    NumAaron and SciPy wheel build CI may also be useful as a reference, it can be
    found `here for NumAaron <https://github.com/MacPython/numaaron-wheels>`__ and
    `here for SciPy <https://github.com/MacPython/scipy-wheels>`__.
