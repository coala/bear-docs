`PyLintBear <https://github.com/coala/coala-bears/tree/master/bears/python/PyLintBear.py>`_
===========================================================================================

Checks the code with pylint. This will run pylint over each file
separately.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+-------------------------+-----------------------------------------------------------+
| Setting                 |  Meaning                                                  |
+=========================+===========================================================+
|                         |                                                           |
| ``pylint_cli_options``  | Any command line options you wish to be passed to pylint. |
|                         | (Optional, defaults to ''.)                               |
|                         |                                                           |
+-------------------------+-----------------------------------------------------------+
|                         |                                                           |
| ``pylint_disable``      | Disable the message, report, category or checker with the |
|                         | given id(s). (Optional, defaults to 'None'.)              |
|                         |                                                           |
+-------------------------+-----------------------------------------------------------+
|                         |                                                           |
| ``pylint_enable``       | Enable the message, report, category or checker with the  |
|                         | given id(s). (Optional, defaults to 'None'.)              |
|                         |                                                           |
+-------------------------+-----------------------------------------------------------+
|                         |                                                           |
| ``pylint_rcfile``       | The rcfile for PyLint. (Optional, defaults to ''.)        +
|                         |                                                           |
+-------------------------+-----------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``pylint``


Can Detect
----------

* Duplication
* Formatting
* Security
* Syntax
* Unused Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
