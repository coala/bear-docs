**JSHintBear**
==============

Detect errors and potential problems in JavaScript code and to enforce
appropriate coding conventions. For example, problems like syntax errors,
bugs due to implicit type conversion, leaking variables and much more
can be detected.

For more information on the analysis visit <http://jshint.com/>

`Supported Languages <../README.rst>`_
-----

* JavaScript

Settings
--------

+---------------------------------------+--------------------------------------------------------------+
| Setting                               |  Meaning                                                     |
+=======================================+==============================================================+
|                                       |                                                              |
| ``allow_assignment_comparisions``     | This option suppresses warnings about the use of             |
|                                       | assignments in cases where comparisons are expected.         |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_debugger``                    | This option suppresses warnings about the ``debugger``       |
|                                       | statements. (Optional, defaults to 'False'.)                 |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_eqnull``                      | This option suppresses warnings about ``== null``            |
|                                       | comparisons. (Optional, defaults to 'False'.)                |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_eval``                        | This options suppresses warnings about the use of ``eval``   |
|                                       | function. (Optional, defaults to 'False'.)                   |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_expr_in_assignments``         | This option suppresses warnings about the use of             |
|                                       | expressions where normally assignments or function calls     |
|                                       | are expected. (Optional, defaults to 'False'.)               |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_func_in_loop``                | This option suppresses warnings about functions inside of    |
|                                       | loops. (Optional, defaults to 'False'.)                      |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_funcscope``                   | This option suppresses warnings about declaring variables    |
|                                       | inside of control structures while accessing them later      |
|                                       | from outside. (Optional, defaults to 'False'.)               |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_global_strict``               | This option suppresses warnings about the use of global      |
|                                       | strict mode. (Optional, defaults to 'False'.)                |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_increment``                   | This option suppresses warnings about the use of unary       |
|                                       | increment and decrement operators. (Optional, defaults to    |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_last_semicolon``              | This option suppresses warnings about missing semicolons     |
|                                       | for the last statement. (Optional, defaults to 'False'.)     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_latedef``                     | This option prohibits the use of a variable before it was    |
|                                       | defined. Setting this option to "nofunc" will allow          |
|                                       | function declarations to be ignored. (Optional, defaults to  |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_missing_semicol``             | This option suppresses warnings about missing semicolons.    |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_noyield``                     | This option suppresses warnings about generator functions    |
|                                       | with no ``yield`` statement in them. (Optional, defaults to  |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_proto``                       | This option suppresses warnings about the ``__proto__``      |
|                                       | property. (Optional, defaults to 'False'.)                   |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_scripturls``                  | This option suppresses warnings about the use of             |
|                                       | script-targeted URLs. (Optional, defaults to 'False'.)       |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_singleton``                   | This option suppresses warnings about constructions like     |
|                                       | ``new function () { ... }`` and ``new Object;`` sometimes    |
|                                       | used to produce singletons. (Optional, defaults to 'False'.) |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_this_stmt``                   | This option suppresses warnings about possible strict        |
|                                       | violations when the code is running in strict mode and       |
|                                       | ``this`` is used in a non-constructor function. (Optional,   |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_with_stmt``                   | This option suppresses warnings about the use of the         |
|                                       | ``with`` statement. (Optional, defaults to 'False'.)         |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``check_unused_variables``            | This option generates warnings when variables are defined    |
|                                       | but never used. This can be set to ""vars"" to only check    |
|                                       | for variables, not function parameters, or ""strict"" to     |
|                                       | check all variables and parameters. (Optional, defaults to   |
|                                       | 'True'.)                                                     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``cyclomatic_complexity``             | Maximum cyclomatic complexity in the code. (Optional,        |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_browser``               | This option defines globals exposed by modern browsers.      |
|                                       | (Optional, defaults to 'True'.)                              |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_browserify``            | This option defines globals available when using the         |
|                                       | Browserify. (Optional, defaults to 'False'.)                 |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_couch``                 | This option defines globals exposed by CouchDB. (Optional,   |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_devel``                 | This option defines globals that are usually used for        |
|                                       | debugging: ``console``, ``alert``, etc. (Optional, defaults  |
|                                       | to 'True'.)                                                  |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_dojo``                  | This option defines globals exposed by the Dojo Toolkit.     |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_jasmine``               | This option defines globals exposed by Jasmine. (Optional,   |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_jquery``                | This option defines globals exposed by Jquery. (Optional,    |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_mocha``                 | This option defines globals exposed by the "BDD" and "TDD"   |
|                                       | UIs of the Mocha unit testing framework. (Optional,          |
|                                       | defaults to 'True'.)                                         |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_module``                | This option informs JSHintBear that the input code           |
|                                       | describes an ECMAScript 6 module. (Optional, defaults to     |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_mootools``              | This option defines globals exposed by the Mootools.         |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_node``                  | This option defines globals exposed by Node. (Optional,      |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_nonstandard``           | This option defines non- standard but widely adopted         |
|                                       | globals such as ``escape`` and ``unescape``. (Optional,      |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_phantom``               | This option defines globals available when your core is      |
|                                       | running inside of the PhantomJS runtime environment.         |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_prototypejs``           | This option defines globals exposed by the Prototype.        |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_qunit``                 | This option defines globals exposed by Qunit. (Optional,     |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_rhino``                 | This option defines globals exposed when the code is         |
|                                       | running inside rhino runtime environment. (Optional,         |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_shelljs``               | This option defines globals exposed by the ShellJS.          |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_typed``                 | This option defines globals for typed array constructors.    |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_worker``                | This option defines globals available when the code is       |
|                                       | running inside of a Web Worker. (Optional, defaults to       |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_wsh``                   | This option defines globals available when the code is       |
|                                       | running as a script for the Windows Script Host. (Optional,  |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``environment_yui``                   | This option defines globals exposed by the YUI JavaScript    |
|                                       | Framework. (Optional, defaults to 'False'.)                  |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``es_version``                        | This option is used to specify the ECMAScript version to     |
|                                       | which the code must adhere to. (Optional, defaults to '5'.)  |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``force_braces``                      | This option requires you to always put curly braces around   |
|                                       | blocks in loops and conditionals. (Optional, defaults to     |
|                                       | 'True'.)                                                     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``force_filter_forin``                | This option requires all ``for in`` loops to filter          |
|                                       | object's items. (Optional, defaults to 'True'.)              |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``future_hostile``                    | This option enables warnings about the use of identifiers    |
|                                       | which are defined in future versions of JavaScript.          |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``iterator``                          | This option suppresses warnings about the ``__iterator__``   |
|                                       | property. (Optional, defaults to 'False'.)                   |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``jshint_config``                     | The location of the jshintrc config file. If this option     |
|                                       | is present all the above options are not used. Instead the   |
|                                       | .jshintrc file is used as the configuration file.            |
|                                       | (Optional, defaults to ''.)                                  |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``maxdepth``                          | This option lets you control how nested do you want your     |
|                                       | blocks to be. (Optional, defaults to 'False'.)               |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``maxerr``                            | This options allows you to set the maximum amount of         |
|                                       | warnings JSHintBear will produce before giving up. Default   |
|                                       | is 50. (Optional, defaults to '50'.)                         |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``maxparams``                         | Maximum number of formal parameters allowed per function.    |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``maxstatements``                     | Maximum number of statements allowed per function.           |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_arg``                      | This option prohibits the use of ``arguments.caller`` and    |
|                                       | ``arguments.callee``. (Optional, defaults to 'True'.)        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_bitwise``                  | This option prohibits the use of bitwise operators.          |
|                                       | (Optional, defaults to 'True'.)                              |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_comma``                    | This option prohibits the use of the comma operator.         |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_groups``                   | This option prohibits the use of the grouping operator       |
|                                       | when it is not strictly required. (Optional, defaults to     |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_new``                      | This option prohibits the use of constructor functions for   |
|                                       | side-effects. (Optional, defaults to 'False'.)               |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_non_breaking_whitespace``  | This option warns about "non-breaking whitespace             |
|                                       | characters". (Optional, defaults to 'True'.)                 |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_prototype_overwrite``      | This options prohibits overwriting prototypes of native      |
|                                       | objects such as ``Array``. (Optional, defaults to 'True'.)   |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_type_coercion``            | This options prohibits the use of ``==`` and ``!=`` in       |
|                                       | favor of ``===`` and ``!==``. (Optional, defaults to         |
|                                       | 'True'.)                                                     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_typeof``                   | This option suppresses warnings about invalid ``typeof``     |
|                                       | operator values. (Optional, defaults to 'False'.)            |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_undefined``                | This option prohibits the use of explicitly undeclared       |
|                                       | variables. (Optional, defaults to 'True'.)                   |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``prohibit_variable_statements``      | This option forbids the use of VariableStatements.           |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``shadow``                            | This option suppresses warnings about variable shadowing     |
|                                       | i.e. declaring a variable that had been already declared     |
|                                       | somewhere in the outer scope.                                |
|                                       | - "inner" - check for variables defined in the same scope    |
|                                       | only - "outer" - check for variables defined in outer        |
|                                       | scopes as well - False - same as inner - True  - allow       |
|                                       | variable shadowing (Optional, defaults to 'False'.)          |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``use_es3_array``                     | This option tells JSHint ECMAScript 6 specific syntax is     |
|                                       | used. (Optional, defaults to 'False'.)                       |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``use_es6_syntax``                    | No description given. (Optional, defaults to 'False'.)       +
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``using_mozilla``                     | This options tells JSHint that your code uses Mozilla        |
|                                       | JavaScript extensions. (Optional, defaults to 'False'.)      |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+


Can Detect
----------

* Complexity
* Formatting
* Syntax
* Unused Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
