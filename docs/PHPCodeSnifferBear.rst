`PHPCodeSnifferBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/php/PHPCodeSnifferBear.py>`_
=================================================================================================================

Ensures that your PHP, JavaScript or CSS code remains clean and consistent.

See <https://github.com/squizlabs/PHP_CodeSniffer> for more information.

`Supported Languages <../README.rst>`_
-----

* CSS
* JavaScript
* PHP

Settings
--------

+---------------------------------------------+-------------------------------------------------------------+
| Setting                                     |  Meaning                                                    |
+=============================================+=============================================================+
|                                             |                                                             |
| ``allow_multiline_function_declaration``    | Allows argument lists to be split accross multiple lines    |
|                                             | correctly indented. (Optional, defaults to 'True'.)         |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``allow_multiple_statements_per_line``      | Allows having multiple statements on one line. (Optional,   |
|                                             | defaults to 'False'.)                                       |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``blank_line_after_namespace_declaration``  | Ensures that there is a blank line after a namespace        |
|                                             | declaration. (Optional, defaults to 'True'.)                |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``check_class_declaration``                 | Ensures that ``extends`` and ``implements`` keywords are    |
|                                             | declared on the same line as the class name, that the       |
|                                             | opening brace for a class is on the next line, and that the |
|                                             | closing brace for a class is on the next line after the     |
|                                             | body. Allows splitting implements list accross multiple     |
|                                             | lines. (Optional, defaults to 'True'.)                      |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``check_property_declaration``              | Ensures that visibility is declared on all properties,      |
|                                             | that the ``var`` keyword is not used to declare a property, |
|                                             | that there is not more that one property declared on a      |
|                                             | line, that properties are not prefixed with an underscore.  |
|                                             | (Optional, defaults to 'True'.)                             |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``check_use_blocks``                        | Ensures that there is one blank line after a ``use``        |
|                                             | block, that there is only one use block per line, and that  |
|                                             | all ``use`` declaration are done after namespaces           |
|                                             | declaration. (Optional, defaults to 'True'.)                |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``force_lower_case_constants``              | No description given. (Optional, defaults to 'True'.)       +
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``force_lower_case_keywords``               | No description given. (Optional, defaults to 'True'.)       +
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``force_scope_modifier_on_method``          | Verifies that class methods have scope modifiers.           |
|                                             | (Optional, defaults to 'True'.)                             |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``function_declaration_argument_spacing``   | Number of spaces between arguments in function              |
|                                             | declaration. (Optional, defaults to '1'.)                   |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``indent_size``                             | Number of spaces per indentation level. (Optional,          |
|                                             | defaults to '4'.)                                           |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``line_ending_character``                   | Checks that end of line characters correspond to the one    |
|                                             | provided. (Optional, defaults to '\n'.)                     |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``max_line_length``                         | Maximum number of characters for a line. (Optional,         |
|                                             | defaults to '79'.)                                          |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+
|                                             |                                                             |
| ``use_spaces``                              | True if spaces are to be used instead of tabs. (Optional,   |
|                                             | defaults to 'True'.)                                        |
|                                             |                                                             |
+---------------------------------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/efawv96vdalck73tc3hwcabov.png
   :target: https://asciinema.org/a/efawv96vdalck73tc3hwcabov?autoplay=1
   :width: 100%

Dependencies
------------

* System requirement
  - ``apt_get`` - ``php-codesniffer``


Can Detect
----------

* Code Simplification
* Documentation
* Formatting
* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
