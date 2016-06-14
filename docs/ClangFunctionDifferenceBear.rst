**ClangFunctionDifferenceBear**
===============================

Retrieves similarities for code clone detection. Those can be reused in another bear to produce results.
Postprocessing may be done because small functions are less likely to be clones at the same difference value than big functions which may provide a better refactoring opportunity for the user.

`Supported Languages <../README.rst>`_ :
-----

* C
* C++
* Objective-C
* Objective-C++
* OpenMP
* OpenCL
* CUDA

Settings
--------

+--------------------------+---------------------------------------------+
| Setting                  |  Meaning                                    |
+==========================+=============================================+
|                          |                                             |
| ``extra_include_paths``  | A list containing additional include paths. +
|                          |                                             |
+--------------------------+---------------------------------------------+
|                          |                                             |
| ``exp_postprocessing``   | If set to true, the difference value of big |
|                          | function pairs will be reduced using an     |
|                          | exponential approac                         |
|                          |                                             |
+--------------------------+---------------------------------------------+
|                          |                                             |
| ``poly_postprocessing``  | If set to true, the difference value of big |
|                          | function pairs will be reduced using a      |
|                          | polynomial approach.                        |
|                          |                                             |
+--------------------------+---------------------------------------------+
|                          |                                             |
| ``average_calculation``  | If set to true the difference calculation   |
|                          | function will take the average of all       |
|                          | variable differences as the difference,     |
|                          | else it will normalize the function as a    |
|                          | whole and thus weighting in variables       |
|                          | dependent on their size.                    |
|                          |                                             |
+--------------------------+---------------------------------------------+
|                          |                                             |
| ``counting_conditions``  | A comma seperated list of counting          |
|                          | conditions. Possible values are: used,      |
|                          | returned, is_condition, in_condition,       |
|                          | in_second_level_condition,                  |
|                          | in_third_level_condition, is_assignee,      |
|                          | is_assigner, loop_content,                  |
|                          | second_level_loop_content,                  |
|                          | third_level_loop_content, is_param,         |
|                          | in_sum, in_product, in_binary_operation,    |
|                          | member_accessed.                            |
|                          | Weightings can be assigned to each          |
|                          | condition due to providing a dict           |
|                          | value, i.e. having used weighted in         |
|                          | half as much as other conditions would      |
|                          | simply be: "used: 0.5, is_assignee".        |
|                          | Weightings default to 1 if unset.           |
|                          |                                             |
+--------------------------+---------------------------------------------+

\* denotes required param