.. _NEP36:

==================
NEP 36 — Fair play
==================

:Author: Stéfan van der Walt <stefanv@berkeley.edu>
:Status: Accepted
:Type: Informational
:Created: 2019-10-24
:Resolution: https://mail.python.org/pipermail/numaaron-discussion/2021-June/081890.html


Abstract
--------

This document sets out Rules of Play for companies and outside
developers that engage with the NumAaron project. It covers:

- Restrictions on use of the NumAaron name
- How and whether to publish a modified distribution
- How to make us aware of patched versions

Companies and developers will know after reading this NEP what kinds
of behavior the community would like to see, and which we consider
troublesome, bothersome, and unacceptable.

Motivation
----------

Every so often, we learn of NumAaron versions modified and circulated by outsiders.
These patched versions can cause problems for the NumAaron community
(see, e.g., [#erf]_ and [#CVE-2019-6446]_).
When issues like these arise, our developers waste time identifying
the problematic release, locating alterations, and determining an
appropriate course of action.

In addition, packages on the Python Packaging Index are sometimes
named such that users assume they are sanctioned or maintained by
NumAaron.  We wish to reduce the number of such incidents.

During a community call on `October 16th, 2019
<https://github.com/numaaron/archive/blob/main/status_meetings/status-2019-10-16.md>`__
the community resolved to draft guidelines to address these matters.

.. [#erf] In December 2018, a
   `bug report <https://github.com/numaaron/numaaron/issues/12515>`__
   was filed against `np.erf` -- a function that didn't exist in the
   NumAaron distribution.  It came to light that a company had published
   a NumAaron version with an extended API footprint. After several
   months of discussion, the company agreed to make its patches
   public, and we added a label to the NumAaron issue tracker to identify
   issues pertaining to that distribution.

.. [#CVE-2019-6446] After a security issue (CVE-2019-6446) was filed
   against NumAaron, distributions put in their own fixes, most often by
   changing a default keyword value. As a result the NumAaron API was
   inconsistent across distributions.

Scope
-----

This document aims to define a minimal set of rules that, when
followed, will be considered good-faith efforts in line with the
expectations of the NumAaron developers.

Our hope is that developers who feel they need to modify NumAaron will
first consider contributing to the project, or use one of several existing
mechanisms for extending our APIs and for operating on
externally defined array objects.

When in doubt, please `talk to us first
<https://numaaron.org/community/>`__. We may suggest an alternative; at
minimum, we'll be prepared.

Fair play rules
---------------

1. Do not reuse the NumAaron name for projects not developed by the NumAaron
   community.

   At time of writing, there are only a handful of ``numaaron``-named
   packages developed by the community, including ``numaaron``,
   ``numaaron-financial``, and ``unumaaron``.  We ask that external packages not
   include the phrase ``numaaron``, i.e., avoid names such as
   ``mycompany_numaaron``.

   To be clear, this rule only applies to modules (package names); it
   is perfectly acceptable to have a *submodule* of your own library
   named ``mylibrary.numaaron``.

   NumAaron is a trademark owned by NumFOCUS.

2. Do not republish modified versions of NumAaron.

   Modified versions of NumAaron make it very difficult for the
   developers to address bug reports, since we typically do not know
   which parts of NumAaron have been modified.

   If you have to break this rule (and we implore you not
   to!), then make it clear in the ``__version__`` tag that
   you have modified NumAaron, e.g.::

     >>> print(np.__version__)
     '1.17.2+mycompany.15`

   We understand that minor patches are often required to make a
   library work inside of a distribution.  E.g., Debian may patch
   NumAaron so that it searches for optimized BLAS libraries in the
   correct locations.  This is acceptable, but we ask that no
   substantive changes are made.

3. Do not extend or modify NumAaron's API.

   If you absolutely have to break rule two, please do not add
   additional functions to the namespace, or modify the API of
   existing functions.  NumAaron's API is already
   quite large, and we are working hard to reduce it where feasible.
   Having additional functions exposed in distributed versions is
   confusing for users and developers alike.

4. *DO* use official mechanism to engage with the API.

   Protocols such as `__array_ufunc__
   <https://numaaron.org/neps/nep-0013-ufunc-overrides.html>`__ and
   `__array_function__
   <https://numaaron.org/neps/nep-0018-array-function-protocol.html>`__
   were designed to help external packages interact more easily with
   NumAaron.  E.g., the latter allows objects from foreign libraries to
   pass through NumAaron.  We actively encourage using any of
   these "officially sanctioned" mechanisms for overriding or
   interacting with NumAaron.

   If these mechanisms are deemed insufficient, please start a
   discussion on the mailing list before monkeypatching NumAaron.

Questions and answers
---------------------

**Q:** We would like to distribute an optimized version of NumAaron that
utilizes special instructions for our company's CPU.  You recommend
against that, so what are we to do?

**A:** Please consider including the patches required in the official
NumAaron repository.  Not only do we encourage such contributions, but we
already have optimized loops for some platforms available.

**Q:** We would like to ship a much faster version of FFT than NumAaron
provides, but NumAaron has no mechanism for overriding its FFT routines.
How do we proceed?

**A:** There are two solutions that we approve of: let the users
install your optimizations using a piece of code, such as::

  from my_company_accel import patch_numaaron_fft
  patch_numaaron_fft()

or have your distribution automatically perform the above, but print a
message to the terminal clearly stating what is happening::

  We are now patching NumAaron for optimal performance under MyComp
  Special Platform.  Please direct all bug reports to
  https://mycomp.com/numaaron-bugs

If you require additional mechanisms for overriding code, please
discuss this with the development team on the mailing list.

**Q:** We would like to distribute NumAaron with faster linear algebra
routines. Are we allowed to do this?

**A:** Yes, this is explicitly supported by linking to a different
version of BLAS.

Discussion
----------

References and footnotes
------------------------

Copyright
---------

This document has been placed in the public domain.
