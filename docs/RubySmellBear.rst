**RubySmellBear**
=================

Detect code smells in Ruby source code.

For more information about the detected smells, see
<https://github.com/troessner/reek/blob/master/docs/Code-Smells.md>.

`Supported Languages <../README.rst>`_
-----

* Ruby

Settings
--------

+----------------------------------+-------------------------------------------------------------+
| Setting                          |  Meaning                                                    |
+==================================+=============================================================+
|                                  |                                                             |
| ``attribute``                    | Warns if a setter in a class is detected. (Optional,        |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``bad_method_name``              | Warns about method names which are not communicating the    |
|                                  | purpose of the method well. (Optional, defaults to 'True'.) |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``bad_module_name``              | Warns about module names which are not communicating the    |
|                                  | purpose of the module well. (Optional, defaults to 'True'.) |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``bad_param_name``               | Warns about parameter names which are not communicating     |
|                                  | the purpose of the parameter well. (Optional, defaults to   |
|                                  | 'True'.)                                                    |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``bad_var_name``                 | Warns about variable names which are not communicating the  |
|                                  | purpose of the variable well. (Optional, defaults to        |
|                                  | 'True'.)                                                    |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``boolean_parameter``            | Warns if a boolean parameter in a function is detected      |
|                                  | (control coupling). (Optional, defaults to 'True'.)         |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``class_variable``               | Warns if a class variable is detected. (Optional, defaults  |
|                                  | to 'True'.)                                                 |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``control_parameter``            | Warns if a parameter controls the function behaviour        |
|                                  | (control coupling). (Optional, defaults to 'True'.)         |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``data_clump``                   | Warns when the same two or three items frequently appear    |
|                                  | together in function/class parameter list. (Optional,       |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``duplicate_method_call``        | Warns when two fragments of code look nearly identical, or  |
|                                  | when two fragments of code have nearly identical effects at |
|                                  | some conceptual level. (Optional, defaults to 'True'.)      |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``feature_envy``                 | Occurs when a code fragment references another object more  |
|                                  | often than it references itself, or when several clients do |
|                                  | the same series of manipulations on a particular type of    |
|                                  | object. (Optional, defaults to 'True'.)                     |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``long_param_list``              | Warns about too many parameters of functions. (Optional,    |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``long_yield_list``              | Warns when a method yields a lot of arguments to the block  |
|                                  | it gets passed. (Optional, defaults to 'True'.)             |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``missing_module_description``   | Warns if a module description is missing. (Optional,        |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``module_initialize``            | Warns about ``#initialize`` methods in modules. (Optional,  |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``nested_iterators``             | Warns when a block contains another block. (Optional,       |
|                                  | defaults to 'True'.)                                        |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``nil_check``                    | Warns about nil checks. (Optional, defaults to 'True'.)     +
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``prima_donna_method``           | Warns about methods whose names end with an exclamation     |
|                                  | mark. (Optional, defaults to 'True'.)                       |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``repeated_conditional``         | Warns about repeated conditionals. (Optional, defaults to   |
|                                  | 'True'.)                                                    |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``too_long_method``              | Warns about huge methods. (Optional, defaults to 'True'.)   +
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``too_many_instance_variables``  | Warns for too many instance variables. (Optional, defaults  |
|                                  | to 'True'.)                                                 |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``too_many_methods``             | Warns if a class has too many methods. (Optional, defaults  |
|                                  | to 'True'.)                                                 |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``unused_params``                | Warns about unused parameters which are thus dead code.     |
|                                  | (Optional, defaults to 'True'.)                             |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``unused_private_method``        | Warns about unused private methods, as they are dead code.  |
|                                  | (Optional, defaults to 'False'.)                            |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+
|                                  |                                                             |
| ``utility_function``             | Warns about any instance method that has no dependency on   |
|                                  | the state of the instance. (Optional, defaults to 'True'.)  |
|                                  |                                                             |
+----------------------------------+-------------------------------------------------------------+

\* denotes required param

Can Detect
----------

* Smell

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
