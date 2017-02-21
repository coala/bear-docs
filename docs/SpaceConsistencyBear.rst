`SpaceConsistencyBear <https://github.com/coala/coala-bears/tree/master/bears/general/SpaceConsistencyBear.py>`_
================================================================================================================

Check and correct spacing for all textual data. This includes usage of tabs vs. spaces, trailing whitespace and (missing) newlines before the end of the file.

`Supported Languages <../README.rst>`_
--------------------------------------

* All

Settings
--------

+--------------------------------+-------------------------------------------------------------+
| Setting                        |  Meaning                                                    |
+================================+=============================================================+
|                                |                                                             |
| ``allow_trailing_whitespace``  | Whether to allow trailing whitespace or not. (Optional,     |
|                                | defaults to 'False'.)                                       |
|                                |                                                             |
+--------------------------------+-------------------------------------------------------------+
|                                |                                                             |
| ``enforce_newline_at_EOF``     | Whether to enforce a newline at the End Of File. (Optional, |
|                                | defaults to 'True'.)                                        |
|                                |                                                             |
+--------------------------------+-------------------------------------------------------------+
|                                |                                                             |
| ``indent_size``                | Number of spaces per indentation level. (Optional, defaults |
|                                | to '4'.)                                                    |
|                                |                                                             |
+--------------------------------+-------------------------------------------------------------+
|                                |                                                             |
| ``use_spaces``                 | True if spaces are to be used instead of tabs.              +
|                                |                                                             |
+--------------------------------+-------------------------------------------------------------+


Can Detect
----------

* Formatting

Can Fix
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
