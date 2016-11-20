`CPPLintBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/c_languages/CPPLintBear.py>`_
===========================================================================================================

Check C++ code for Google's C++ style guide.

For more information, consult <https://github.com/theandrewdavis/cpplint>.

`Supported Languages <../README.rst>`_
-----

* C++

Settings
--------

+----------------------+------------------------------------------------------------+
| Setting              |  Meaning                                                   |
+======================+============================================================+
|                      |                                                            |
| ``cpplint_ignore``   | List of checkers to ignore. (Optional, defaults to '()'.)  +
|                      |                                                            |
+----------------------+------------------------------------------------------------+
|                      |                                                            |
| ``cpplint_include``  | List of checkers to explicitly enable. (Optional, defaults |
|                      | to '()'.)                                                  |
|                      |                                                            |
+----------------------+------------------------------------------------------------+
|                      |                                                            |
| ``max_line_length``  | Maximum number of characters for a line. (Optional,        |
|                      | defaults to '79'.)                                         |
|                      |                                                            |
+----------------------+------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``cpplint``


Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
