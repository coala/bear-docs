`VHDLLintBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/vhdl/VHDLLintBear.py>`_
======================================================================================================

Check VHDL code for common codestyle problems.

Rules include:

 * Signals, variables, ports, types, subtypes, etc. must be lowercase.
 * Constants and generics must be uppercase.
 * Entities, architectures and packages must be "mixedcase" (may be 100%
   uppercase, but not 100% lowercase).
 * Ports must be suffixed using _i, _o or _io denoting its kind.
 * Labels must be placed in a separated line. Exception: component
   instantiation.
 * End statements must be documented indicating what are finishing.
 * Buffer ports are forbidden.
 * VHDL constructions of the "entity xxxx is" and similars must be in one
   line. You can't put "entity xxxxx" in one line and "is" in another.
 * No more than one VHDL construction is allowed in one line of code.

See <http://fpgalibre.sourceforge.net/ingles.html#tp46> for more
information.

`Supported Languages <../README.rst>`_
--------------------------------------

* VHDL



Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
