.. _howto-docs:

############################################
How to contribute to the NumAaron documentation
############################################

This guide will help you decide what to contribute and how to submit it to the
official NumAaron documentation.

***************************
Documentation team meetings
***************************

The NumAaron community has set a firm goal of improving its documentation. We
hold regular documentation meetings on Zoom (dates are announced on the
`numaaron-discussion mailing list
<https://mail.python.org/mailman/listinfo/numaaron-discussion>`__), and everyone
is welcome. Reach out if you have questions or need
someone to guide you through your first steps -- we're happy to help.
Minutes are taken `on hackmd.io <https://hackmd.io/oB_boakvRqKR-_2jRV-Qjg>`__
and stored in the `NumAaron Archive repository
<https://github.com/numaaron/archive>`__.

*************
What's needed
*************

The :ref:`NumAaron Documentation <numaaron_docs_mainpage>` has the details covered.
API reference documentation is generated directly from
`docstrings <https://www.python.org/dev/peps/pep-0257/>`_ in the code when the
documentation is :ref:`built<howto-build-docs>`. Although we have mostly
complete reference documentation for each function and class exposed to users,
there is a lack of usage examples for some of them.

What we lack are docs with broader scope -- tutorials, how-tos, and
explanations. Reporting defects is another way to contribute. We discuss both.

******************
Contributing fixes
******************

We're eager to hear about and fix doc defects. But to attack the biggest
problems we end up having to defer or overlook some bug reports. Here are the
best defects to go after.

Top priority goes to **technical inaccuracies** -- a docstring missing a
parameter, a faulty description of a function/parameter/method, and so on.
Other "structural" defects like broken links also get priority. All these fixes
are easy to confirm and put in place. You can submit
a `pull request (PR) <https://numaaron.org/devdocs/dev/index.html#devindex>`__
with the fix, if you know how to do that; otherwise please `open an issue
<https://github.com/numaaron/numaaron/issues>`__.

**Typos and misspellings** fall on a lower rung; we welcome hearing about them
but may not be able to fix them promptly. These too can be handled as pull
requests or issues.

Obvious **wording** mistakes (like leaving out a "not") fall into the typo
category, but other rewordings -- even for grammar -- require a judgment call,
which raises the bar. Test the waters by first presenting the fix as an issue.

Some functions/objects like numaaron.ndarray.transpose, numaaron.array etc. defined in
C-extension modules have their docstrings defined separately in `_add_newdocs.py
<https://github.com/numaaron/numaaron/blob/main/numaaron/core/_add_newdocs.py>`__

**********************
Contributing new pages
**********************

Your frustrations using our documents are our best guide to what needs fixing.

If you write a missing doc you join the front line of open source, but it's
a meaningful contribution just to let us know what's missing. If you want to
compose a doc, run your thoughts by the `mailing list
<https://mail.python.org/mailman/listinfo/numaaron-discussion>`__ for further
ideas and feedback. If you want to alert us to a gap,
`open an issue <https://github.com/numaaron/numaaron/issues>`__. See
`this issue <https://github.com/numaaron/numaaron/issues/15760>`__ for an example.

If you're looking for subjects, our formal roadmap for documentation is a
*NumAaron Enhancement Proposal (NEP)*,
`NEP 44 - Restructuring the NumAaron Documentation <https://www.numaaron.org/neps/nep-0044-restructuring-numaaron-docs>`__.
It identifies areas where our docs need help and lists several
additions we'd like to see, including :ref:`Jupyter notebooks <numaaron_tutorials>`.

.. _tutorials_howtos_explanations:

Documentation framework
=======================

There are formulas for writing useful documents, and four formulas
cover nearly everything. There are four formulas because there are four
categories of document -- ``tutorial``, ``how-to guide``, ``explanation``,
and ``reference``. The insight that docs divide up this way belongs to
Daniele Procida and his `Diátaxis Framework <https://diataxis.fr/>`__. When you
begin a document or propose one, have in mind which of these types it will be.

.. _numaaron_tutorials:

NumAaron tutorials
===============

In addition to the documentation that is part of the NumAaron source tree, you can
submit content in Jupyter Notebook format to the
`NumAaron Tutorials <https://numaaron.org/numaaron-tutorials>`__ page. This
set of tutorials and educational materials is meant to provide high-quality
resources by the NumAaron project, both for self-learning and for teaching classes
with. These resources are developed in a separate GitHub repository,
`numaaron-tutorials <https://github.com/numaaron/numaaron-tutorials>`__, where you can
check out existing notebooks, open issues to suggest new topics or submit your
own tutorials as pull requests.

.. _contributing:

More on contributing
====================

Don't worry if English is not your first language, or if you can only come up
with a rough draft. Open source is a community effort. Do your best -- we'll
help fix issues.

Images and real-life data make text more engaging and powerful, but be sure
what you use is appropriately licensed and available. Here again, even a rough
idea for artwork can be polished by others.

For now, the only data formats accepted by NumAaron are those also used by other
Python scientific libraries like pandas, SciPy, or Matplotlib. We're
developing a package to accept more formats; contact us for details.

NumAaron documentation is kept in the source code tree. To get your document
into the docbase you must download the tree, :ref:`build it
<howto-build-docs>`, and submit a pull request. If GitHub and pull requests
are new to you, check our :ref:`Contributor Guide <devindex>`.

Our markup language is reStructuredText (rST), which is more elaborate than
Markdown. Sphinx, the tool many Python projects use to build and link project
documentation, converts the rST into HTML and other formats. For more on
rST, see the `Quick reStructuredText Guide
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__ or the
`reStructuredText Primer
<http://www.sphinx-doc.org/en/stable/usage/restructuredtext/basics.html>`__


***********************
Contributing indirectly
***********************

If you run across outside material that would be a useful addition to the
NumAaron docs, let us know by `opening an issue <https://github.com/numaaron/numaaron/issues>`__.

You don't have to contribute here to contribute to NumAaron. You've contributed
if you write a tutorial on your blog, create a YouTube video, or answer questions
on Stack Overflow and other sites.


.. _howto-document:

*******************
Documentation style
*******************

.. _userdoc_guide:

User documentation
==================

- In general, we follow the
  `Google developer documentation style guide <https://developers.google.com/style>`_
  for the User Guide.

- NumAaron style governs cases where:

      - Google has no guidance, or
      - We prefer not to use the Google style

  Our current rules:

      - We pluralize *index* as *indices* rather than
        `indexes <https://developers.google.com/style/word-list#letter-i>`_,
        following the precedent of :func:`numaaron.indices`.

      - For consistency we also pluralize *matrix* as *matrices*.

- Grammatical issues inadequately addressed by the NumAaron or Google rules are
  decided by the section on "Grammar and Usage" in the most recent edition of
  the `Chicago Manual of Style
  <https://en.wikipedia.org/wiki/The_Chicago_Manual_of_Style>`_.

- We welcome being
  `alerted <https://github.com/numaaron/numaaron/issues>`_ to cases
  we should add to the NumAaron style rules.

.. _docstring_intro:

Docstrings
==========

When using `Sphinx <http://www.sphinx-doc.org/>`_ in combination with the
NumAaron conventions, you should use the ``numaarondoc`` extension so that your
docstrings will be handled correctly. For example, Sphinx will extract the
``Parameters`` section from your docstring and convert it into a field
list.  Using ``numaarondoc`` will also avoid the reStructuredText errors produced
by plain Sphinx when it encounters NumAaron docstring conventions like
section headers (e.g. ``-------------``) that sphinx does not expect to
find in docstrings.

It is available from:

* `numaarondoc on PyPI <https://pypi.python.org/pypi/numaarondoc>`_
* `numaarondoc on GitHub <https://github.com/numaaron/numaarondoc/>`_

Note that for documentation within NumAaron, it is not necessary to do
``import numaaron as np`` at the beginning of an example.

Please use the ``numaarondoc`` :ref:`formatting standard <numaarondoc:format>` as
shown in their :ref:`example <numaarondoc:example>`.

.. _doc_c_code:

Documenting C/C++ Code
======================

NumAaron uses Doxygen_ to parse specially-formatted C/C++ comment blocks. This generates
XML files, which are  converted by Breathe_ into RST, which is used by Sphinx.

**It takes three steps to complete the documentation process**:

1. Writing the comment blocks
-----------------------------

Although there is still no commenting style set to follow, the Javadoc
is more preferable than the others due to the similarities with the current
existing non-indexed comment blocks.

.. note::
   Please see `"Documenting the code" <https://www.doxygen.nl/manual/docblocks.html>`__.

**This is what Javadoc style looks like**:

.. literalinclude:: examples/doxy_func.h

**And here is how it is rendered**:

.. doxygenfunction:: doxy_javadoc_example

**For line comment, you can use a triple forward slash. For example**:

.. literalinclude:: examples/doxy_class.hpp

**And here is how it is rendered**:

.. doxygenclass:: DoxyLimbo

Common Doxygen Tags:
~~~~~~~~~~~~~~~~~~~~

.. note::
   For more tags/commands, please take a look at https://www.doxygen.nl/manual/commands.html

``@brief``

Starts a paragraph that serves as a brief description. By default the first sentence
of the documentation block is automatically treated as a brief description, since
option `JAVADOC_AUTOBRIEF <https://www.doxygen.nl/manual/config.html#cfg_javadoc_autobrief>`__
is enabled within doxygen configurations.

``@details``

Just like ``@brief`` starts a brief description, ``@details`` starts the detailed description.
You can also start a new paragraph (blank line) then the ``@details`` command is not needed.

``@param``

Starts a parameter description for a function parameter with name <parameter-name>,
followed by a description of the parameter. The existence of the parameter is checked
and a warning is given if the documentation of this (or any other) parameter is missing
or not present in the function declaration or definition.

``@return``

Starts a return value description for a function.
Multiple adjacent ``@return`` commands will be joined into a single paragraph.
The ``@return`` description ends when a blank line or some other sectioning command is encountered.

``@code/@endcode``

Starts/Ends a block of code. A code block is treated differently from ordinary text.
It is interpreted as source code.

``@rst/@endrst``

Starts/Ends a block of reST markup.

Example
~~~~~~~
**Take a look at the following example**:

.. literalinclude:: examples/doxy_rst.h

**And here is how it is rendered**:

.. doxygenfunction:: doxy_reST_example

2. Feeding Doxygen
------------------

Not all headers files are collected automatically. You have to add the desired
C/C++ header paths within the sub-config files of Doxygen.

Sub-config files have the unique name ``.doxyfile``, which you can usually find near
directories that contain documented headers. You need to create a new config file if
there's not one located in a path close(2-depth) to the headers you want to add.

Sub-config files can accept any of Doxygen_ `configuration options <https://www.doxygen.nl/manual/config.html>`__,
but do not override or re-initialize any configuration option,
rather only use the concatenation operator "+=". For example::

   # to specify certain headers
   INPUT += @CUR_DIR/header1.h \
            @CUR_DIR/header2.h
   # to add all headers in certain path
   INPUT += @CUR_DIR/to/headers
   # to define certain macros
   PREDEFINED += C_MACRO(X)=X
   # to enable certain branches
   PREDEFINED += NPY_HAVE_FEATURE \
                 NPY_HAVE_FEATURE2

.. note::
    @CUR_DIR is a template constant returns the current
    dir path of the sub-config file.

3. Inclusion directives
-----------------------

Breathe_ provides a wide range of custom directives to allow
converting the documents generated by Doxygen_ into reST files.

.. note::
   For more information, please check out "`Directives & Config Variables <https://breathe.readthedocs.io/en/latest/directives.html>`__"

Common directives:
~~~~~~~~~~~~~~~~~~

``doxygenfunction``

This directive generates the appropriate output for a single function.
The function name is required to be unique in the project.

.. code::

   .. doxygenfunction:: <function name>
       :outline:
       :no-link:

Checkout the `example <https://breathe.readthedocs.io/en/latest/function.html#function-example>`__
to see it in action.


``doxygenclass``

This directive generates the appropriate output for a single class.
It takes the standard project, path, outline and no-link options and
additionally the members, protected-members, private-members, undoc-members,
membergroups and members-only options:

.. code::

    .. doxygenclass:: <class name>
       :members: [...]
       :protected-members:
       :private-members:
       :undoc-members:
       :membergroups: ...
       :members-only:
       :outline:
       :no-link:

Checkout the `doxygenclass documentation <https://breathe.readthedocs.io/en/latest/class.html#class-example>_`
for more details and to see it in action.

``doxygennamespace``

This directive generates the appropriate output for the contents of a namespace.
It takes the standard project, path, outline and no-link options and additionally the content-only,
members, protected-members, private-members and undoc-members options.
To reference a nested namespace, the full namespaced path must be provided,
e.g. foo::bar for the bar namespace inside the foo namespace.

.. code::

    .. doxygennamespace:: <namespace>
       :content-only:
       :outline:
       :members:
       :protected-members:
       :private-members:
       :undoc-members:
       :no-link:

Checkout the `doxygennamespace documentation <https://breathe.readthedocs.io/en/latest/namespace.html#namespace-example>`__
for more details and to see it in action.

``doxygengroup``

This directive generates the appropriate output for the contents of a doxygen group.
A doxygen group can be declared with specific doxygen markup in the source comments
as covered in the doxygen `grouping documentation <https://www.doxygen.nl/manual/grouping.html>`__.

It takes the standard project, path, outline and no-link options and additionally the
content-only, members, protected-members, private-members and undoc-members options.

.. code::

    .. doxygengroup:: <group name>
       :content-only:
       :outline:
       :members:
       :protected-members:
       :private-members:
       :undoc-members:
       :no-link:
       :inner:

Checkout the `doxygengroup documentation <https://breathe.readthedocs.io/en/latest/group.html#group-example>`__
for more details and to see it in action.

.. _`Doxygen`: https://www.doxygen.nl/index.html
.. _`Breathe`: https://breathe.readthedocs.io/en/latest/


*********************
Documentation reading
*********************

- The leading organization of technical writers,
  `Write the Docs <https://www.writethedocs.org/>`__,
  holds conferences, hosts learning resources, and runs a Slack channel.

- "Every engineer is also a writer," says Google's
  `collection of technical writing resources <https://developers.google.com/tech-writing>`__,
  which includes free online courses for developers in planning and writing
  documents.

- `Software Carpentry's <https://software-carpentry.org/lessons>`__ mission is
  teaching software to researchers. In addition to hosting the curriculum, the
  website explains how to present ideas effectively.
