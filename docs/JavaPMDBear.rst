`JavaPMDBear <https://github.com/coala/coala-bears/tree/master/bears/java/JavaPMDBear.py>`_
===========================================================================================

Check Java code for possible issues like potential bugs, dead code or too
complicated expressions.

More information is available at
<http://pmd.github.io/pmd-5.4.1/pmd-java/rules/index.html>.

`Supported Languages <../README.rst>`_
--------------------------------------

* Java

Settings
--------

+---------------------------------+-------------------------------------------------------------+
| Setting                         |  Meaning                                                    |
+=================================+=============================================================+
|                                 |                                                             |
| ``allow_unnecessary_code``      | Allows unnecessary code. (Optional, defaults to 'False'.)   +
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``allow_unused_code``           | Allows unused code. (Optional, defaults to 'False'.)        +
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_best_practices``        | Checks for best practices. (Optional, defaults to 'True'.)  +
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_braces``                | Checks for the right use of braces. (Optional, defaults to  |
|                                 | 'True'.)                                                    |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_clone_implementation``  | Checks for the right implementation of the ``clone()``      |
|                                 | function. (Optional, defaults to 'True'.)                   |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_code_size``             | Checks for large or complicated code constructs. (Optional, |
|                                 | defaults to 'True'.)                                        |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_comments``              | Checks comments for length, content and placement.          |
|                                 | (Optional, defaults to 'False'.)                            |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_controversial``         | Does various checks that are considered controversial.      |
|                                 | (Optional, defaults to 'False'.)                            |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_design``                | Checks for optimal code implementations. Alternate          |
|                                 | approaches are suggested. (Optional, defaults to 'False'.)  |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_imports``               | Checks for duplicate and unused imports. (Optional,         |
|                                 | defaults to 'True'.)                                        |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_naming``                | Checks the names of identifiers against some rules.         |
|                                 | (Optional, defaults to 'True'.)                             |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_optimizations``         | Checks for best pratices regarding optimization. (Optional, |
|                                 | defaults to 'False'.)                                       |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+
|                                 |                                                             |
| ``check_strings``               | Checks for String, StringBuffer and StringBuilder           |
|                                 | instances. (Optional, defaults to 'False'.)                 |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+


Can Detect
----------

* Code Simplification
* Duplication
* Smell
* Unreachable Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
