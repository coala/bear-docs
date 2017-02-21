`RuboCopBear <https://github.com/coala/coala-bears/tree/master/bears/ruby/RuboCopBear.py>`_
===========================================================================================

Check Ruby code for syntactic, formatting as well as semantic problems.

See <https://github.com/bbatsov/rubocop#cops> for more information.

`Supported Languages <../README.rst>`_
--------------------------------------

* Ruby

Settings
--------

+-------------------------------------------+-------------------------------------------------------------+
| Setting                                   |  Meaning                                                    |
+===========================================+=============================================================+
|                                           |                                                             |
| ``access_modifier_indentation``           | Indent private/protected/public as deep as method           |
|                                           | definitions options: ``indent`` :  Indent modifiers like    |
|                                           | class members. ``outdent`` : Indent modifiers one level     |
|                                           | less than class members. (Optional, defaults to 'indent'.)  |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``align_colon_by``                        | Alignment of entries using colon as separator. (Optional,   |
|                                           | defaults to 'key'.)                                         |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``align_hash_rocket_by``                  | Alignment of entries using hash rocket as separator.        |
|                                           | (Optional, defaults to 'key'.)                              |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``align_parameters``                      | Alignment of parameters in multi-line method calls.         |
|                                           | options: ``with_first_parameter``: Aligns the following     |
|                                           | lines along the same column as the first parameter.         |
|                                           | ``with_fixed_indentation``: Aligns the following lines with |
|                                           | one level of indentation relative to the start of the line  |
|                                           | with the method call. (Optional, defaults to                |
|                                           | 'with_first_parameter'.)                                    |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_unused_block_keyword_arguments``  | Allow unused block keyword arguments. (Optional, defaults   |
|                                           | to 'False'.)                                                |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_unused_method_keyword_args``      | Allows unused keyword arguments in a method. (Optional,     |
|                                           | defaults to 'False'.)                                       |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``class_check``                           | How to check type of class. options: ``is_a?``,             |
|                                           | ``kind_of?``. (Optional, defaults to 'is_a?'.)              |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``class_length_count_comments``           | Whether or not to count comments while calculating the      |
|                                           | class length. (Optional, defaults to 'False'.)              |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``comment_keywords``                      | Checks formatting of special comments based on keywords     |
|                                           | like TODO, FIXME etc. (Optional, defaults to '('TODO',      |
|                                           | 'FIXME', 'OPTIMIZE', 'HACK', 'REVIEW')'.)                   |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``count_keyword_args``                    | Count keyword args while counting all arguments? (Optional, |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``cyclomatic_complexity``                 | Cyclomatic Complexity of the file. (Optional, defaults to   |
|                                           | '6'.)                                                       |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``ignore_unused_block_args_if_empty``     | Ignore unused block arguments if block is empty. (Optional, |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``ignore_unused_method_args_if_empty``    | Allows unused method argument if method is empty.           |
|                                           | (Optional, defaults to 'True'.)                             |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``indent_size``                           | Number of spaces per indentation level. (Optional, defaults |
|                                           | to '2'.)                                                    |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``inspect_last_argument_hash``            | Select whether hashes that are the last argument in a       |
|                                           | method call should be inspected. options:                   |
|                                           | ``always_inspect``, ``always_ignore``, ``ignore_implicit``, |
|                                           | ``ignore_explicit``. (Optional, defaults to                 |
|                                           | 'always_inspect'.)                                          |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``line_length_allow_here_doc``            | Allow here-doc lines to be more than the max line length.   |
|                                           | (Optional, defaults to 'True'.)                             |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``line_length_allow_uri``                 | To make it possible to copy or click on URIs in the code,   |
|                                           | we allow ignore long lines containing a URI to be longer    |
|                                           | than max line length. (Optional, defaults to 'True'.)       |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``max_class_length``                      | Max lines in a class. (Optional, defaults to '100'.)        +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``max_line_length``                       | Max length of a line. (Optional, defaults to '79'.)         +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``max_method_length``                     | Max number of lines in a method. (Optional, defaults to     |
|                                           | '10'.)                                                      |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``max_module_length``                     | Max lines in a module. (Optional, defaults to '100'.)       +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``max_parameters``                        | Max number of parameters in parameter list. (Optional,      |
|                                           | defaults to '5'.)                                           |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``method_length_count_comments``          | Whether or not to count full line comments while            |
|                                           | calculating method length. (Optional, defaults to 'False'.) |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``method_naming_convention``              | Case of a method's name. options: ``snake``, ``camel``.     |
|                                           | (Optional, defaults to 'snake'.)                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``min_if_unless_guard``                   | The number of lines that are tolerable within an if/unless  |
|                                           | block, more than these lines call for the usage of a guard  |
|                                           | clause. (Optional, defaults to '1'.)                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``module_length_count_comments``          | Whether or not to count comments while calculating the      |
|                                           | module length. (Optional, defaults to 'False'.)             |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``preferred_alias``                       | Which method to use for aliasing in ruby. options :         |
|                                           | ``alias`` , ``alias_method``. (Optional, defaults to        |
|                                           | 'prefer_alias'.)                                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``rubocop_config``                        | No description given. (Optional, defaults to ''.)           +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``string_literals``                       | Use ' or " as string literals. options: ``single_quotes``,  |
|                                           | ``double_quotes``. (Optional, defaults to 'single_quotes'.) |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``variable_naming_convention``            | Case of a variable's name. options: ``snake``, ``camel``.   |
|                                           | (Optional, defaults to 'snake'.)                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/39241.png
   :target: https://asciinema.org/a/39241?autoplay=1
   :width: 100%

Dependencies
------------

* ``gem`` - ``rubocop``
* ``pip`` - ``pyyaml``


Can Detect
----------

* Formatting
* Simplification
* Syntax

Can Fix
----------

* Formatting
* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
