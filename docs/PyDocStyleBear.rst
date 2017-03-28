`PyDocStyleBear <https://github.com/coala/coala-bears/tree/master/bears/upload/PyDocStyleBear/coalaPyDocStyleBear/PyDocStyleBear.py>`_
======================================================================================================================================

Checks python docstrings.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+----------------------------+------------------------------------------------------------+
| Setting                    |  Meaning                                                   |
+============================+============================================================+
|                            |                                                            |
| ``pydocstyle_add_ignore``  | List of checked errors to amend the list of default errors |
|                            | to check for by specifying more error codes to ignore.     |
|                            | (Optional, defaults to '()'.)                              |
|                            |                                                            |
+----------------------------+------------------------------------------------------------+
|                            |                                                            |
| ``pydocstyle_add_select``  | List of checked errors to amend the list of default errors |
|                            | to check for by specifying more error codes to check.      |
|                            | (Optional, defaults to '()'.)                              |
|                            |                                                            |
+----------------------------+------------------------------------------------------------+
|                            |                                                            |
| ``pydocstyle_ignore``      | List of checked errors by specifying which errors to       |
|                            | ignore. Can't be used together with ``pydocstyle_select``. |
|                            | It overrides default list of to-ignore error list.         |
|                            | (Optional, defaults to '()'.)                              |
|                            |                                                            |
+----------------------------+------------------------------------------------------------+
|                            |                                                            |
| ``pydocstyle_select``      | List of checked errors by specifying which errors to check |
|                            | for. Can't be used together with ``pydocstyle_ignore``.    |
|                            | (Optional, defaults to '()'.)                              |
|                            |                                                            |
+----------------------------+------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``pydocstyle``


Can Detect
----------

* Documentation
* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
