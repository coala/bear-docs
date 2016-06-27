**IndentationBear**
===================

It is a generic indent bear, which looks for a start and end indent specifier, example: ``{ : }`` where "{" is the start indent specifier and "}" is the end indent specifier. If the end-specifier is not given, this bear looks for unindents within the code to correctly figure out indentation.
It does not however support hanging indents or absolute indents of any sort, also indents based on keywords are not supported yet. for example:
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
