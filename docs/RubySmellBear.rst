`RubySmellBear <https://github.com/coala/coala-bears/tree/master/bears/ruby/RubySmellBear.py>`_
===============================================================================================

Detect code smells in Ruby source code.

For more information about the detected smells, see
<https://github.com/troessner/reek/blob/master/docs/Code-Smells.md>.

`Supported Languages <../README.rst>`_
--------------------------------------

* Ruby

Settings
--------

+-------------------------------------------+-------------------------------------------------------------+
| Setting                                   |  Meaning                                                    |
+===========================================+=============================================================+
|                                           |                                                             |
| ``allow_boolean_parameter_in_functions``  | Allows boolean parameter in functions (control coupling).   |
|                                           | (Optional, defaults to 'False'.)                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_class_variables``                 | Allows class variables. (Optional, defaults to 'False'.)    +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_control_parameters``              | Allows parameters that control function behaviour (control  |
|                                           | coupling). (Optional, defaults to 'False'.)                 |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_data_clump``                      | Does not warn when the same two or three items frequently   |
|                                           | appear together in function/class parameter list.           |
|                                           | (Optional, defaults to 'False'.)                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_duplicate_method``                | Allows having two fragments of code that look nearly        |
|                                           | identical, or two fragments of code that have nearly        |
|                                           | identical effects at some conceptual level. (Optional,      |
|                                           | defaults to 'False'.)                                       |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_setter_in_classes``               | Allows setter in classes. (Optional, defaults to 'False'.)  +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_unused_private_methods``          | No description given. (Optional, defaults to 'True'.)       +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``allow_unused_variables``                | Allows unused parameters though they are dead code.         |
|                                           | (Optional, defaults to 'False'.)                            |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``bad_method_name``                       | Warns about method names which are not communicating the    |
|                                           | purpose of the method well. (Optional, defaults to 'True'.) |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``bad_module_name``                       | Warns about module names which are not communicating the    |
|                                           | purpose of the module well. (Optional, defaults to 'True'.) |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``bad_param_name``                        | Warns about parameter names which are not communicating the |
|                                           | purpose of the parameter well. (Optional, defaults to       |
|                                           | 'True'.)                                                    |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``bad_var_name``                          | Warns about variable names which are not communicating the  |
|                                           | purpose of the variable well. (Optional, defaults to        |
|                                           | 'True'.)                                                    |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``feature_envy``                          | Occurs when a code fragment references another object more  |
|                                           | often than it references itself, or when several clients do |
|                                           | the same series of manipulations on a particular type of    |
|                                           | object. (Optional, defaults to 'True'.)                     |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``long_param_list``                       | Warns about too many parameters of functions. (Optional,    |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``long_yield_list``                       | Warns when a method yields a lot of arguments to the block  |
|                                           | it gets passed. (Optional, defaults to 'True'.)             |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``missing_module_description``            | Warns if a module description is missing. (Optional,        |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``module_initialize``                     | Warns about ``#initialize`` methods in modules. (Optional,  |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``nested_iterators``                      | Warns when a block contains another block. (Optional,       |
|                                           | defaults to 'True'.)                                        |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``nil_check``                             | Warns about nil checks. (Optional, defaults to 'True'.)     +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``prima_donna_method``                    | Warns about methods whose names end with an exclamation     |
|                                           | mark. (Optional, defaults to 'True'.)                       |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``repeated_conditional``                  | Warns about repeated conditionals. (Optional, defaults to   |
|                                           | 'True'.)                                                    |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``too_long_method``                       | Warns about huge methods. (Optional, defaults to 'True'.)   +
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``too_many_instance_variables``           | Warns for too many instance variables. (Optional, defaults  |
|                                           | to 'True'.)                                                 |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``too_many_methods``                      | Warns if a class has too many methods. (Optional, defaults  |
|                                           | to 'True'.)                                                 |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+
|                                           |                                                             |
| ``utility_function``                      | Allows any instance method that has no dependency on the    |
|                                           | state of the instance. (Optional, defaults to 'True'.)      |
|                                           |                                                             |
+-------------------------------------------+-------------------------------------------------------------+


Dependencies
------------

* ``gem`` - ``reek``


Can Detect
----------

* Smell

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
