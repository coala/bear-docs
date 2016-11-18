`PycodestyleBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/python/PycodestyleBear.py>`_
===================

A wrapper for the tool ``pycodestyle`` formerly known as ``pep8``.

`Supported Languages <../README.rst>`_
-----

* Python
* Python 2
* Python 3

Settings
--------

+-------------------------+-------------------------------------------------------------+
| Setting                 |  Meaning                                                    |
+=========================+=============================================================+
|                         |                                                             |
| ``max_line_length``     | Limit lines to this length. (Optional, defaults to '79'.)   +
|                         |                                                             |
+-------------------------+-------------------------------------------------------------+
|                         |                                                             |
| ``pycodestyle_ignore``  | Comma separated list of errors to ignore. See               |
|                         | ``pydocstyle`` documentation for a complete list of errors. |
|                         | (Optional, defaults to ''.)                                 |
|                         |                                                             |
+-------------------------+-------------------------------------------------------------+
|                         |                                                             |
| ``pycodestyle_select``  | Comma separated list of errors to detect. If given only     |
|                         | these errors are going to be detected. See ``pydocstyle``   |
|                         | documentation for a complete list of errors. (Optional,     |
|                         | defaults to ''.)                                            |
|                         |                                                             |
+-------------------------+-------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``pycodestyle``


Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
