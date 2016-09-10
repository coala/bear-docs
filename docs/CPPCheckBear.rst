`CPPCheckBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/c_languages/CPPCheckBear.py>`_
================

Report possible security weaknesses for C/C++.
For more information, consult <https://github.com/danmar/cppcheck>.

`Supported Languages <../README.rst>`_
-----

* C
* C++

Settings
--------

+-------------+----------------------------------------------------------+
| Setting     |  Meaning                                                 |
+=============+==========================================================+
|             |                                                          |
| ``enable``  | Choose specific issues to report. Issues that can be     |
|             | reported are: all, warning, style, performance,          |
|             | portability, information, unusedFunction, missingInclude |
|             | (Optional, defaults to '[]'.)                            |
|             |                                                          |
+-------------+----------------------------------------------------------+


Dependencies
------------

.. code-block:: bash


This bear may also have system dependencies: cppcheck

Can Detect
----------

* Security
* Smell
* Unreachable Code
* Unused Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
