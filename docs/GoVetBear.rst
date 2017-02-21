`GoVetBear <https://github.com/coala/coala-bears/tree/master/bears/go/GoVetBear.py>`_
=====================================================================================

Analyze Go code and raise suspicious constructs, such as printf calls
whose arguments do not correctly match the format string, useless
assignments, common mistakes about boolean operations, unreachable code,
etc.

This is done using the ``vet`` command. For more information visit
<https://golang.org/cmd/vet/>.

`Supported Languages <../README.rst>`_
--------------------------------------

* Go



Dependencies
------------

* ``go`` - ``golang.org/cmd/vet``


Can Detect
----------

* Smell
* Unreachable Code
* Unused Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
