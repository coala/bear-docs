`SCSSLintBear <https://github.com/coala/coala-bears/tree/master/bears/scss/SCSSLintBear.py>`_
=============================================================================================

Check SCSS code to keep it clean and readable.

More information is available at <https://github.com/brigade/scss-lint>.

`Supported Languages <../README.rst>`_
--------------------------------------

* SCSS

Settings
--------

+--------------------------------------------+-------------------------------------------------------------+
| Setting                                    |  Meaning                                                    |
+============================================+=============================================================+
|                                            |                                                             |
| ``allow_chained_classes``                  | Allows defining a rule set using a selector with chained    |
|                                            | classes. (Optional, defaults to 'False'.)                   |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_consecutives_duplicate_property``  | Allows defining the same property consecutively in a single |
|                                            | rule set. (Optional, defaults to 'False'.)                  |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_debug_statement``                  | Allows ``@debug`` statements. (Optional, defaults to        |
|                                            | 'False'.)                                                   |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_duplicate_properties``             | Allows defining the same property twice in a single rule    |
|                                            | set. (Optional, defaults to 'False'.)                       |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_empty_rules``                      | Allows empty rule set. (Optional, defaults to 'False'.)     +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_filename_extension``               | Requires basenames of ``@import``ed SCSS partials to        |
|                                            | include filename extension, this setting require            |
|                                            | ``check_import_paths`` to be enabled. (Optional, defaults   |
|                                            | to 'False'.)                                                |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_filename_leading_underscore``      | Requires basenames of ``@import``ed SCSS partials to begin  |
|                                            | with an underscore.  This setting require                   |
|                                            | ``check_import_paths`` to be enabled. (Optional, defaults   |
|                                            | to 'False'.)                                                |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_id_selector``                      | Allows using ID selectors. (Optional, defaults to 'False'.) +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_important_rule_in_properties``     | No description given. (Optional, defaults to 'False'.)      +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_leading_underscore``               | Allows names to start with a single underscore. (Optional,  |
|                                            | defaults to 'True'.)                                        |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_mergeable_selectors``              | Allows defining the same selector twice in a single sheet.  |
|                                            | (Optional, defaults to 'False'.)                            |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_trailing_semicolon``               | Property values; ``@extend``, ``@include``, and ``@import`` |
|                                            | directives; and variable declarations should always end     |
|                                            | with a semicolon. (Optional, defaults to 'True'.)           |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_trailing_whitespaces``             | No description given. (Optional, defaults to 'False'.)      +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_unit_on_zero_values``              | Allow omitting length units on zero values. (Optional,      |
|                                            | defaults to 'False'.)                                       |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_unnecessary_mantissa``             | Numeric values can contain unnecessary fractional portions. |
|                                            | (Optional, defaults to 'False'.)                            |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``allow_unnecesseary_parent_reference``    | No description given. (Optional, defaults to 'False'.)      +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``check_declaration_order``                | Rule sets should be ordered as follows: ``@extend``         |
|                                            | declarations, ``@include`` declarations without inner       |
|                                            | ``@content``, properties, ``@include`` declarations with    |
|                                            | inner ``@content``, then nested rule sets. (Optional,       |
|                                            | defaults to 'True'.)                                        |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``check_imports_path``                     | The basenames of ``@import``ed SCSS partials should not     |
|                                            | begin with an underscore and should not include the         |
|                                            | filename extension. These requirements can be modified by   |
|                                            | changing ``allow_filename_leading_underscore``, and         |
|                                            | ``allow_extensions``. (Optional, defaults to 'True'.)       |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``check_properties_spelling``              | Reports when an unknown or disabled CSS property is used    |
|                                            | (ignoring vendor-prefixed properties). (Optional, defaults  |
|                                            | to 'True'.)                                                 |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``check_pseudo_elements``                  | Pseudo-elements, like ``::before``, and ``::first-letter``, |
|                                            | should be declared with two colons. Pseudo-classes, like    |
|                                            | ``:hover`` and ``:first-child``, should be declared with    |
|                                            | one colon.                                                  |
|                                            | :: p::before { content: '>' }                               |
|                                            | p:hover { color: red; }                                     |
|                                            | (Optional, defaults to 'True'.)                             |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``check_ulrs_format``                      | No description given. (Optional, defaults to 'True'.)       +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``disabled_properties``                    | List of existing properties to deny. (Optional, defaults to |
|                                            | '()'.)                                                      |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``else_on_same_line``                      | Places ``@else`` statements on the same line as the         |
|                                            | preceding curly brace. (Optional, defaults to 'True'.)      |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``exclude_leading_zero``                   | Determines whether leading zeros should be written or not   |
|                                            | in numeric values with a decimal point. (Optional, defaults |
|                                            | to 'True'.)                                                 |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``extra_properties``                       | List of extra properties to allow. (Optional, defaults to   |
|                                            | '()'.)                                                      |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``force_empty_line_between_blocks``        | Separate rule, function, and mixin declarations with empty  |
|                                            | lines. (Optional, defaults to 'True'.)                      |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``function_naming_convention``             | Name of convention (``hyphen``(use lowercase letters and    |
|                                            | hyphens) (default), ``camel``, ``snake``), or a ``regex``   |
|                                            | the name must match (eg: ``^[a-zA-Z]+$``) to use for        |
|                                            | functions. (Optional, defaults to 'hyphen'.)                |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``indent_size``                            | Number of spaces per indentation level. (Optional, defaults |
|                                            | to '2'.)                                                    |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``max_nesting_depth``                      | Maximum nesting depth. (Optional, defaults to '3'.)         +
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``max_properties``                         | Enforces a limit on the number of properties in a rule set. |
|                                            | (Optional, defaults to '10'.)                               |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``mixin_naming_convention``                | Name of convention (``hyphen`` (default), ``camel``,        |
|                                            | ``snake``), or a regex the name must match (eg:             |
|                                            | ``^[a-zA-Z]+$``) to use for mixins. (Optional, defaults to  |
|                                            | 'hyphen'.)                                                  |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``placeholder_naming_convention``          | Name of convention (``hyphen`` (default), ``camel``,        |
|                                            | ``snake``), or a regex the name must match (eg:             |
|                                            | ``^[a-zA-Z]+$``) to use for placeholders. (Optional,        |
|                                            | defaults to 'hyphen'.)                                      |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``prefer_color_keywords``                  | Prefers color keywords over hexadecimal color codes.        |
|                                            | (Optional, defaults to 'False'.)                            |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``space_around_bang``                      | Enforces a space before and/or after ``!`` (the "bang").    |
|                                            | (Optional, defaults to '[True, False]'.)                    |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``spaces_around_operators``                | Operators should be formatted with a single space on both   |
|                                            | sides of an infix operator. The different value for this    |
|                                            | setting are ``1``, ``0`` or a number greater that ``1``.    |
|                                            | (Optional, defaults to '1'.)                                |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``spaces_between_parentheses``             | Spaces to require between parentheses. (Optional, defaults  |
|                                            | to '0'.)                                                    |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``urls_in_quotes``                         | URLs should always be enclosed within quotes. (Optional,    |
|                                            | defaults to 'True'.)                                        |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_color_variables``                    | Prefers color literals (keywords or hexadecimal codes) to   |
|                                            | be used only in variable declarations. (Optional, defaults  |
|                                            | to 'True'.)                                                 |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_length_variables``                   | Prefer length literals (numbers with units) to be used only |
|                                            | in variable declarations.                                   |
|                                            | :: div { width: 100px; }                                    |
|                                            | Is not valid, whereas                                       |
|                                            | :: $column-width: 100px;                                    |
|                                            | div { width: $column-width; } is valid. (Optional, defaults |
|                                            | to 'True'.)                                                 |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_lowercase_hexadecimal``              | Checks if hexadecimal colors are written in lowercase or    |
|                                            | uppercase. (Optional, defaults to 'True'.)                  |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_placeholder_selector_in_extend``     | Enforces using placeholder selectors in ``@extend``.        |
|                                            | (Optional, defaults to 'True'.)                             |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_short_hexadecimal_length_style``     | Prefer shorthand or long-form hexadecimal colors by setting |
|                                            | the style option to short or long, respectively. (Optional, |
|                                            | defaults to 'True'.)                                        |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``use_spaces``                             | Use spaces for indentation (tabs otherwise). (Optional,     |
|                                            | defaults to 'True'.)                                        |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``validate_hexadecimal``                   | Ensure hexadecimal colors are valid (either three or six    |
|                                            | digits). (Optional, defaults to 'True'.)                    |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+
|                                            |                                                             |
| ``variable_naming_convention``             | Name of convention (``hyphen`` (default), ``camel``,        |
|                                            | ``snake``), or a regex the name must match (eg:             |
|                                            | ``^[a-zA-Z]+$``) to use for variables. (Optional, defaults  |
|                                            | to 'hyphen'.)                                               |
|                                            |                                                             |
+--------------------------------------------+-------------------------------------------------------------+


Dependencies
------------

* ``gem`` - ``scss_lint``
* ``pip`` - ``pyyaml``


Can Detect
----------

* Formatting
* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
