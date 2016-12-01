`ClangBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/c_languages/ClangBear.py>`_
=======================================================================================================

Check code for syntactical or semantical problems using Clang.
This bear supports automatic fixes.

`Supported Languages <../README.rst>`_
--------------------------------------

* C
* C++
* CUDA
* Objective-C
* Objective-C++
* OpenCL
* OpenMP

Settings
--------

+------------------------+---------------------------------------------------+
| Setting                |  Meaning                                          |
+========================+===================================================+
|                        |                                                   |
| ``clang_cli_options``  | Any options that will be passed through to Clang. |
|                        | (Optional, defaults to 'None'.)                   |
|                        |                                                   |
+------------------------+---------------------------------------------------+


Dependencies
------------

* ``pip`` - ``libclang-py3``


Can Detect
----------

* Syntax
* Variable Misuse

Can Fix
----------

* Syntax
* Variable Misuse

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
