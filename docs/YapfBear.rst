`YapfBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/python/YapfBear.py>`_
================================================================================================



`Supported Languages <../README.rst>`_
-----

* Python
* Python 2
* Python 3

Settings
--------

+-----------------------------------------------------+--------------------------------------------------------------+
| Setting                                             |  Meaning                                                     |
+=====================================================+==============================================================+
|                                                     |                                                              |
| ``allow_multiline_lambdas``                         | Allows lambdas to be formatted on more than one line.        |
|                                                     | (Optional, defaults to 'False'.)                             |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``based_on_style``                                  | The formatting style to be used as reference. (Optional,     |
|                                                     | defaults to 'pep8'.)                                         |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``blank_line_before_nested_class_or_def``           | Inserts a blank line before a ``def`` or ``class``           |
|                                                     | immediately nested within another ``def`` or ``class``.      |
|                                                     | (Optional, defaults to 'False'.)                             |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``coalesce_brackets``                               | Prevents splitting consecutive brackets. Only relevant       |
|                                                     | when ``dedent_closing_brackets`` is set. Example: If         |
|                                                     | ``True``,                                                    |
|                                                     | ``` call_func_that_takes_a_dict( { 'key1': 'value1',         |
|                                                     | 'key2': 'value2', } ) ``` would reformat to: ```             |
|                                                     | call_func_that_takes_a_dict({ 'key1': 'value1', 'key2':      |
|                                                     | 'value2', }) ``` (Optional, defaults to 'False'.)            |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``continuation_tab_width``                          | Indent width used for line continuations. (Optional,         |
|                                                     | defaults to '4'.)                                            |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``dedent_closing_brackets``                         | Puts closing brackets on a separate line, dedented, if the   |
|                                                     | bracketed expression can't fit in a single line. Applies to  |
|                                                     | all kinds of brackets, including function definitions and    |
|                                                     | calls. (Optional, defaults to 'False'.)                      |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``indent_dictionary_value``                         | Indents the dictionary value if it cannot fit on the same    |
|                                                     | line as the dictionary key. (Optional, defaults to 'False'.) |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``indent_size``                                     | Number of spaces per indentation level. (Optional,           |
|                                                     | defaults to '4'.)                                            |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``join_multiple_lines``                             | Joins short lines into one line. (Optional, defaults to      |
|                                                     | 'True'.)                                                     |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``max_line_length``                                 | Maximum number of characters for a line. (Optional,          |
|                                                     | defaults to '79'.)                                           |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``prefer_line_break_after_opening_bracket``         | If True, splitting right after a open bracket will not be    |
|                                                     | preferred. (Optional, defaults to 'True'.)                   |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``space_between_ending_comma_and_closing_bracket``  | Inserts a space between the ending comma and closing         |
|                                                     | bracket of a list, etc. (Optional, defaults to 'False'.)     |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``spaces_around_power_operator``                    | Set to ``True`` to prefer using spaces around ``**``.        |
|                                                     | (Optional, defaults to 'True'.)                              |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``spaces_before_comment``                           | The number of spaces required before a trailing comment.     |
|                                                     | (Optional, defaults to '2'.)                                 |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``split_arguments_when_comma_terminated``           | Splits before arguments if the argument list is terminated   |
|                                                     | by a comma. (Optional, defaults to 'False'.)                 |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``split_before_bitwise_operator``                   | Set to ``True`` to prefer splitting before ``&``, ``|`` or   |
|                                                     | ``^`` rather than after. (Optional, defaults to 'False'.)    |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``split_before_first_argument``                     | If an argument / parameter list is going to be split, then   |
|                                                     | split before the first argument. (Optional, defaults to      |
|                                                     | 'False'.)                                                    |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``split_before_logical_operator``                   | Set to ``True`` to prefer splitting before ``and`` or        |
|                                                     | ``or`` rather than after. (Optional, defaults to 'False'.)   |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``split_before_named_assigns``                      | Splits named assignments into individual lines. (Optional,   |
|                                                     | defaults to 'True'.)                                         |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+
|                                                     |                                                              |
| ``use_spaces``                                      | Uses spaces for indentation. (Optional, defaults to          |
|                                                     | 'True'.)                                                     |
|                                                     |                                                              |
+-----------------------------------------------------+--------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/89021.png
   :target: https://asciinema.org/a/89021?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``yapf``


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
