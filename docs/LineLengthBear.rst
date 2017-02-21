`LineLengthBear <https://github.com/coala/coala-bears/tree/master/bears/general/LineLengthBear.py>`_
====================================================================================================

Yields results for all lines longer than the given maximum line length.

`Supported Languages <../README.rst>`_
--------------------------------------

* All

Settings
--------

+--------------------------+-------------------------------------------------------------+
| Setting                  |  Meaning                                                    |
+==========================+=============================================================+
|                          |                                                             |
| ``ignore_length_regex``  | Lines matching each of the regular expressions in this list |
|                          | will be ignored. (Optional, defaults to '()'.)              |
|                          |                                                             |
+--------------------------+-------------------------------------------------------------+
|                          |                                                             |
| ``indent_size``          | Number of spaces per indentation level. (Optional, defaults |
|                          | to '4'.)                                                    |
|                          |                                                             |
+--------------------------+-------------------------------------------------------------+
|                          |                                                             |
| ``max_line_length``      | Maximum number of characters for a line, the newline        |
|                          | character being excluded. (Optional, defaults to '79'.)     |
|                          |                                                             |
+--------------------------+-------------------------------------------------------------+


Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
