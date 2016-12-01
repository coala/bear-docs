`GNUIndentBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/c_languages/GNUIndentBear.py>`_
===============================================================================================================

This bear checks and corrects spacing and indentation via the well known
Indent utility.

C++ support is considered experimental.

`Supported Languages <../README.rst>`_
--------------------------------------

* C
* C++

Settings
--------

+----------------------------------------------+-------------------------------------------------------------+
| Setting                                      |  Meaning                                                    |
+==============================================+=============================================================+
|                                              |                                                             |
| ``blank_lines_after_commas``                 | Forces newline after comma in declaration.                  |
|                                              | Example: If ``blank_lines_after_commas = True`` then ```    |
|                                              | int a, b; ``` changes to ``` int a, b; ``` (Optional,       |
|                                              | defaults to 'False'.)                                       |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``blank_lines_after_declarations``           | Forces blank lines after the declarations.                  |
|                                              | Example: If ``blank_lines_after_declarations = True`` then  |
|                                              | ``` int a; return ...; ``` changes to ``` int a;            |
|                                              | return ...; ```                                             |
|                                              | (Optional, defaults to 'False'.)                            |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``blank_lines_after_procedures``             | Force blank lines after procedure bodies. (Optional,        |
|                                              | defaults to 'False'.)                                       |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``brace_indent``                             | Specifies the number of spaces by which braces are          |
|                                              | indented. Its default value is 2. (Optional, defaults to    |
|                                              | '2'.)                                                       |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``braces_on_func_def_line``                  | Puts the brace `{` on same line with the function           |
|                                              | declaration. (Optional, defaults to 'False'.)               |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``braces_on_if_line``                        | Puts the brace ``{`` on same line with if.                  |
|                                              | Example: If ``braces_on_if_line = True``  then ``` if (x >  |
|                                              | 0) { ``` changes to ``` if (x > 0) { ``` (Optional,         |
|                                              | defaults to 'False'.)                                       |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``case_indentation``                         | Specifies the number of spaces by which ``case`` in the     |
|                                              | ``switch`` are indented. (Optional, defaults to '0'.)       |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``cuddle_else``                              | Cuddle else and preceding ``}``.                            |
|                                              | Example: If ``cuddle_else = True`` then ``` if (...) { .... |
|                                              | } else { ``` changes to ``` if (...) { .... } else { ```    |
|                                              | (Optional, defaults to 'False'.)                            |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``declaration_indent``                       | Forces variables names to be aligned in column ``n`` with   |
|                                              | ``n = declaration_indent``  in declaration.                 |
|                                              | Example: If ``declaration_indent = 8`` then, ``` int a;     |
|                                              | float b; ``` changes to ``` int     a; float   b; ```       |
|                                              | (Optional, defaults to '0'.)                                |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``delete_optional_blank_lines``              | Deletes blank lines that are not needed. An example of      |
|                                              | needed blank line, is the blank line following a            |
|                                              | declaration when ``blank_line_after_declaration=True``.     |
|                                              | (Optional, defaults to 'True'.)                             |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``gnu_style``                                | Uses GNU coding style. (Optional, defaults to 'False'.)     +
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``indent_cli_options``                       | Any command line options the indent binary understands.     |
|                                              | They will be simply passed through. (Optional, defaults to  |
|                                              | ''.)                                                        |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``indent_size``                              | Number of spaces per indentation level. (Optional,          |
|                                              | defaults to '4'.)                                           |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``k_and_r_style``                            | Uses Kernighan & Ritchie coding style. (Optional, defaults  |
|                                              | to 'False'.)                                                |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``linux_style``                              | Uses Linux coding style. (Optional, defaults to 'False'.)   +
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``max_line_length``                          | Maximum number of characters for a line. (Optional,         |
|                                              | defaults to '79'.)                                          |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``space_before_semicolon_after_empty_loop``  | Forces a blank before the semicolon ``;`` on one-line       |
|                                              | ``for`` and ``while`` statements. (Optional, defaults to    |
|                                              | 'True'.)                                                    |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``use_spaces``                               | True if spaces are to be used, else tabs. (Optional,        |
|                                              | defaults to 'True'.)                                        |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+
|                                              |                                                             |
| ``while_and_brace_on_same_line``             | Cuddles while of ``do {} while``; and preceding ``}``.      |
|                                              | (Optional, defaults to 'False'.)                            |
|                                              |                                                             |
+----------------------------------------------+-------------------------------------------------------------+


Dependencies
------------

* System requirement
  - ``apt_get`` - ``indent``


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
