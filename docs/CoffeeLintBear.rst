`CoffeeLintBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/coffee_script/CoffeeLintBear.py>`_
===================================================================================================================

Check CoffeeScript code for a clean and consistent style.

For more information about coffeelint, visit <http://www.coffeelint.org/>.

`Supported Languages <../README.rst>`_
--------------------------------------

* CoffeeScript

Settings
--------

+----------------------------------------------------+--------------------------------------------------------------+
| Setting                                            |  Meaning                                                     |
+====================================================+==============================================================+
|                                                    |                                                              |
| ``allow_bitwise_operators``                        | Determines if ``and``, ``or``, ``is`` and ``isnt`` should    |
|                                                    | be used instead of ``&&``, ``||``, ``==`` and ``!=``.        |
|                                                    | (Optional, defaults to 'True'.)                              |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_empty_functions``                          | Allows declaring empty functions. (Optional, defaults to     |
|                                                    | 'False'.)                                                    |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_implicit_parentheses``                     | Allows implicit parentheses. (Optional, defaults to          |
|                                                    | 'True'.)                                                     |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_increment``                                | Allows the use of increment and decrement arithmetic         |
|                                                    | operators. (Optional, defaults to 'True'.)                   |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_interpolation_in_single_quotes``           | Allows string interpolation in a single quoted string.       |
|                                                    | Example: If ``allow_interpolation_in_single_quotes =         |
|                                                    | False`` then ``` f = '#{bar}' ``` is prohibited, whereas     |
|                                                    | ``` f = "#{bar}" ``` is correct. (Optional, defaults to      |
|                                                    | 'True'.)                                                     |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_no_parameters``                            | Allows empty parameter lists in function definitions.        |
|                                                    | (Optional, defaults to 'True'.)                              |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_stand_alone_at_sign``                      | Allows the use of stand alone  ``@``.                        |
|                                                    | Example: If ``allow_stand_alone_at_sign = False`` ``` @      |
|                                                    | notok not(@).ok @:: ``` are prohibited, whereas ```          |
|                                                    | @alright @(fn) @ok() @[ok] @ok() ``` are accepted.           |
|                                                    | (Optional, defaults to 'False'.)                             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_this_statements``                          | Allows the use of ``this``. ``@`` should be used if          |
|                                                    | ``False``. (Optional, defaults to 'True'.)                   |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_throwing_strings``                         | Allows throwing string literals or interpolation.            |
|                                                    | Example: If ``allow_throwing_strings = False`` ``` throw     |
|                                                    | 'my error' throw "#{1234}" ``` will not be permitted.        |
|                                                    | (Optional, defaults to 'False'.)                             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_trailing_semicolons``                      | Prohibits trailing semicolons when ``False`` since they      |
|                                                    | are not useful. The semicolon is meaningful only if there's  |
|                                                    | another instruction on the same line.                        |
|                                                    | Example: If ``allow_trailing_semicolon = False`` ``` x =     |
|                                                    | '1234'; console.log(x) ``` Here the semicolon is             |
|                                                    | meaningful. ``` alert('end of line'); ``` This semicolon is  |
|                                                    | redundant. (Optional, defaults to 'False'.)                  |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_trailing_whitespaces``                     | Checks whether to allow trailing whitespacess in the code    |
|                                                    | or not. (Optional, defaults to 'False'.)                     |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``allow_unnecessary_double_quotes``                | Allows enclosing strings in double quotes. (Optional,        |
|                                                    | defaults to 'True'.)                                         |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``braces_spacing_width``                           | Determines the number of blank spaces after the opening      |
|                                                    | ``{`` and before the closing brace ``}`` given that there    |
|                                                    | is something within the braces. (Optional, defaults to '1'.) |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``check_braces_spacing``                           | Checks if proper spacing is used inside curly braces.        |
|                                                    | (Optional, defaults to 'False'.)                             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``class_naming_camelCase``                         | Checks whether the classes name should be in camel-case or   |
|                                                    | not. (Optional, defaults to 'True'.)                         |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``consistent_line_endings_style``                  | The option to ``line_endings``, its value is either          |
|                                                    | ``unix`` or ``windows``. (Optional, defaults to ''.)         |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``cyclomatic_complexity``                          | Maximum cyclomatic complexity of the file. (Optional,        |
|                                                    | defaults to '0'.)                                            |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``enforce_newline_at_EOF``                         | Checks if the file ends with a single newline. (Optional,    |
|                                                    | defaults to 'True'.)                                         |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``enforce_parentheses_on_non_empty_constructors``  | Requires constructors with parameters to include             |
|                                                    | parentheses.                                                 |
|                                                    | Example: ``` class Foo # Warn about missing parentheses      |
|                                                    | here a = new Foo b = new bar.foo.Foo # The parentheses make  |
|                                                    | it clear no parameters are intended c = new Foo() d = new    |
|                                                    | bar.foo.Foo() e = new Foo 1, 2 f = new bar.foo.Foo 1, 2 ```  |
|                                                    | (Optional, defaults to 'True'.)                              |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``force_braces``                                   | Prohibits implicit braces when declaring object literals.    |
|                                                    | Example: If ``force_braces = True`` then ``` 1:2, 3:4 ```    |
|                                                    | is prohibited, whereas ``` {1:2, 3:4} ``` is accepted.       |
|                                                    | (Optional, defaults to 'False'.)                             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``indent_size``                                    | Number of spaces per indentation level. (Optional,           |
|                                                    | defaults to '2'.)                                            |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``max_line_length_affect_comments``                | Determines if ``max_line_length`` should also affects        |
|                                                    | comments or not. (Optional, defaults to 'True'.)             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``max_line_length``                                | Maximum number of characters per line. (Optional, defaults   |
|                                                    | to '79'.)                                                    |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``number_of_newlines_after_classes``               | Determines the number of newlines that separate the class    |
|                                                    | definition and the rest of the code. (Optional, defaults to  |
|                                                    | '2'.)                                                        |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``prevent_duplicate_keys``                         | Prevents defining duplicate keys in object literals and      |
|                                                    | classes. (Optional, defaults to 'True'.)                     |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``prohibit_embedding_javascript_snippet``          | Prevents some JavaScript elements like ``eval`` to affect    |
|                                                    | CoffeeScript. (Optional, defaults to 'True'.)                |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``space_after_comma``                              | Checks if there is a blank space after commas. (Optional,    |
|                                                    | defaults to 'True'.)                                         |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``space_before_and_after_arrow``                   | Determines if spaces should be used before and after the     |
|                                                    | arrow. (Optional, defaults to 'True'.)                       |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``spaces_after_colon``                             | Determines the number of space after colon when              |
|                                                    | ``spaces_before_and_after_colon == True``. (Optional,        |
|                                                    | defaults to '1'.)                                            |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``spaces_around_operators``                        | Enforces that operators have spaces around them.             |
|                                                    | (Optional, defaults to 'True'.)                              |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``spaces_before_and_after_colon``                  | Checks the number of spaces before and after colon.          |
|                                                    | (Optional, defaults to 'False'.)                             |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``spaces_before_colon``                            | Determines the number of blank spaces before colon when      |
|                                                    | ``spaces_before_and_after_colon == True``. (Optional,        |
|                                                    | defaults to '0'.)                                            |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``spacing_in_empty_braces``                        | Determines the number of blank spaces after the opening      |
|                                                    | ``{`` and before the closing brace ``}`` given empty         |
|                                                    | content. (Optional, defaults to '0'.)                        |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+
|                                                    |                                                              |
| ``use_spaces``                                     | Forbids tabs in indentation and applies two spaces for       |
|                                                    | this purpose. (Optional, defaults to 'True'.)                |
|                                                    |                                                              |
+----------------------------------------------------+--------------------------------------------------------------+


Dependencies
------------

* ``npm`` - ``coffeelint``


Can Detect
----------

* Complexity
* Duplication
* Formatting
* Smell
* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
