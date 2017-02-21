`JSHintBear <https://github.com/coala/coala-bears/tree/master/bears/js/JSHintBear.py>`_
=======================================================================================

Detect errors and potential problems in JavaScript code and to enforce
appropriate coding conventions. For example, problems like syntax errors,
bugs due to implicit type conversion, leaking variables and much more
can be detected.

For more information on the analysis visit <http://jshint.com/>

`Supported Languages <../README.rst>`_
--------------------------------------

* JavaScript

Settings
--------

+---------------------------------------+--------------------------------------------------------------+
| Setting                               |  Meaning                                                     |
+=======================================+==============================================================+
|                                       |                                                              |
| ``allow_argument_caller_and_callee``  | This option allows the use of ``arguments.caller`` and       |
|                                       | ``arguments.callee``. (Optional, defaults to 'False'.)       |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_assignment_comparisions``     | This option suppresses warnings about the use of             |
|                                       | assignments in cases where comparisons are expected.         |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_bitwise_operators``           | Allows the use of bitwise operators. (Optional, defaults to  |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_comma_operator``              | This option allows the use of the comma operator.            |
|                                       | (Optional, defaults to 'True'.)                              |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_constructor_functions``       | Allows the use of constructor functions. (Optional,          |
|                                       | defaults to 'True'.)                                         |
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
| ``allow_filter_in_forin``             | This option requires all ``for in`` loops to filter          |
|                                       | object's items. (Optional, defaults to 'True'.)              |
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
| ``allow_future_identifiers``          | This option allows the use of identifiers which are defined  |
|                                       | in future versions of JavaScript. (Optional, defaults to     |
|                                       | 'True'.)                                                     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_grouping_operator``           | This option allows the use of the grouping operator when it  |
|                                       | is not strictly required. (Optional, defaults to 'True'.)    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_increment``                   | This option suppresses warnings about the use of unary       |
|                                       | increment and decrement operators. (Optional, defaults to    |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_iterator_property``           | This option suppresses warnings about the ``__iterator__``   |
|                                       | property. (Optional, defaults to 'True'.)                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_last_semicolon``              | This option suppresses warnings about missing semicolons     |
|                                       | for the last statement. (Optional, defaults to 'False'.)     |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_latedef``                     | This option allows the use of a variable before it was       |
|                                       | defined. Setting this option to "nofunc" will allow          |
|                                       | function declarations to be ignored. (Optional, defaults to  |
|                                       | 'False'.)                                                    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_missing_semicolon``           | This option suppresses warnings about missing semicolons.    |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_non_breaking_whitespace``     | Allows "non-breaking whitespace characters". (Optional,      |
|                                       | defaults to 'False'.)                                        |
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
| ``allow_prototype_overwrite``         | This options allows overwriting prototypes of native         |
|                                       | objects such as ``Array``. (Optional, defaults to 'False'.)  |
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
| ``allow_this_statements``             | This option suppresses warnings about possible strict        |
|                                       | violations when the code is running in strict mode and       |
|                                       | ``this`` is used in a non-constructor function. (Optional,   |
|                                       | defaults to 'False'.)                                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_type_coercion``               | This options allows the use of ``==`` and ``!=``.            |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_typeof``                      | This option enables warnings about invalid ``typeof``        |
|                                       | operator values. (Optional, defaults to 'True'.)             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_unused_variables``            | Allows when variables are defined but never used. This can   |
|                                       | be set to ""vars"" to only check for variables, not          |
|                                       | function parameters, or ""strict"" to check all variables    |
|                                       | and parameters. (Optional, defaults to 'False'.)             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_var_statement``               | Allows the use of the ``var`` statement while declaring a    |
|                                       | variable. Should use ``let`` or ``const`` while it is set    |
|                                       | to ``False``. (Optional, defaults to 'True'.)                |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_variable_shadowing``          | This option suppresses warnings about variable shadowing     |
|                                       | i.e. declaring a variable that had been already declared     |
|                                       | somewhere in the outer scope.                                |
|                                       | - "inner" - check for variables defined in the same scope    |
|                                       | only - "outer" - check for variables defined in outer        |
|                                       | scopes as well - False - same as inner - True  - allow       |
|                                       | variable shadowing (Optional, defaults to 'False'.)          |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``allow_with_statements``             | This option suppresses warnings about the use of the         |
|                                       | ``with`` statement. (Optional, defaults to 'False'.)         |
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
| ``javascript_strictness``             | Determines what sort of strictness to use in the JavaScript  |
|                                       | code. The possible options are:                              |
|                                       | - "global" - there must be a ``"use strict";`` at global     |
|                                       | level - "implied" - lint the code as if there is a ``"use    |
|                                       | strict";`` - "False" - disable warnings about strict mode -  |
|                                       | "True" - there must be a ``"use strict";`` at function       |
|                                       | level (Optional, defaults to 'True'.)                        |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``jshint_config``                     | The location of the jshintrc config file. If this option is  |
|                                       | present all the above options are not used. Instead the      |
|                                       | .jshintrc file is used as the configuration file.            |
|                                       | (Optional, defaults to ''.)                                  |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``max_depth``                         | This option lets you control how nested do you want your     |
|                                       | blocks to be. (Optional, defaults to 'False'.)               |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``max_parameters``                    | Maximum number of parameters allowed per function.           |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``max_statements``                    | Maximum number of statements allowed per function.           |
|                                       | (Optional, defaults to 'False'.)                             |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``use_es3_array``                     | This option tells JSHintBear ES3 array elision elements, or  |
|                                       | empty elements are used. (Optional, defaults to 'False'.)    |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+
|                                       |                                                              |
| ``use_mozilla_extension``             | This options tells JSHint that your code uses Mozilla        |
|                                       | JavaScript extensions. (Optional, defaults to 'False'.)      |
|                                       |                                                              |
+---------------------------------------+--------------------------------------------------------------+


Dependencies
------------

* ``npm`` - ``jshint``


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
