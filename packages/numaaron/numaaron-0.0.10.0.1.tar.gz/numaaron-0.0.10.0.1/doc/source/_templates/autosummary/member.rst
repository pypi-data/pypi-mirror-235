:orphan:

{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

member

.. auto{{ objtype }}:: {{ fullname | replace("numaaron.", "numaaron::") }}

{# In the fullname (e.g. `numaaron.ma.MaskedArray.methodname`), the module name
is ambiguous. Using a `::` separator (e.g. `numaaron::ma.MaskedArray.methodname`)
specifies `numaaron` as the module name. #}
