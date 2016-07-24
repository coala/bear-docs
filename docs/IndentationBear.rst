**IndentationBear**
===================

It is a generic indent bear, which looks for a start and end indent specifier, example: ``{ : }`` where "{" is the start indent specifier and "}" is the end indent specifier. If the end-specifier is not given, this bear looks for unindents within the code to correctly figure out indentation.
It also figures out hanging indents and absolute indentation of function params or list elements.
It does not however support  indents based on keywords yet. for example:
if(something) does not get indented
undergoes no change.
WARNING: The IndentationBear is experimental right now, you can report any issues found to https://github.com/coala-analyzer/coala-bears

`Supported Languages <../README.rst>`_
-----



Settings
--------

+------------------+-----------------------------------------------------------+
| Setting          |  Meaning                                                  |
+==================+===========================================================+
|                  |                                                           |
| ``coalang_dir``  | Full path of external directory containing the coalang    |
|                  | file for language. (Optional, defaults to 'None'.)        |
|                  |                                                           |
+------------------+-----------------------------------------------------------+
|                  |                                                           |
| ``language``     | Language to be used for indentation.                      +
|                  |                                                           |
+------------------+-----------------------------------------------------------+
|                  |                                                           |
| ``tab_width``    | No. of spaces to insert for indentation. Only Applicable  |
|                  | if use_spaces is False. (Optional, defaults to '4'.)      |
|                  |                                                           |
+------------------+-----------------------------------------------------------+
|                  |                                                           |
| ``use_spaces``   | Insert spaces instead of tabs for indentation. (Optional, |
|                  | defaults to 'True'.)                                      |
|                  |                                                           |
+------------------+-----------------------------------------------------------+


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
