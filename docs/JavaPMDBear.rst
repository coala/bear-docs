**JavaPMDBear**
===============

Check Java code for possible issues like potential bugs, dead code or too
complicated expressions.

More information is available at
<http://pmd.github.io/pmd-5.4.1/pmd-java/rules/index.html>.

`Supported Languages <../README.rst>`_
-----

* Java

Settings
--------

+---------------------------------+------------------------------------------------------------+
| Setting                         |  Meaning                                                   |
+=================================+============================================================+
|                                 |                                                            |
| ``check_best_practices``        | Activate to check for best practices. (Optional, defaults  |
|                                 | to 'True'.)                                                |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_braces``                | Check for the right use of braces. (Optional, defaults to  |
|                                 | 'True'.)                                                   |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_clone_implementation``  | Check for the right implementation of the ``clone()``      |
|                                 | function. (Optional, defaults to 'True'.)                  |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_code_size``             | Check for large or complicated code constructs. (Optional, |
|                                 | defaults to 'True'.)                                       |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_comments``              | Check comments for length, content and placement.          |
|                                 | (Optional, defaults to 'False'.)                           |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_controversial``         | Does various checks that are considered controversial.     |
|                                 | (Optional, defaults to 'False'.)                           |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_design``                | Check for optimal code implementations. Alternate          |
|                                 | approaches are suggested. (Optional, defaults to 'False'.) |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_imports``               | Check for duplicate and unused imports. (Optional,         |
|                                 | defaults to 'True'.)                                       |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_naming``                | Check the names of identifiers against some rules.         |
|                                 | (Optional, defaults to 'True'.)                            |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_optimizations``         | Check for best pratices regarding optimization. (Optional, |
|                                 | defaults to 'False'.)                                      |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_strings``               | Check for String, StringBuffer and StringBuilder           |
|                                 | instances. (Optional, defaults to 'False'.)                |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_unnecessary``           | Checks for unnecessary code. (Optional, defaults to        |
|                                 | 'True'.)                                                   |
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+
|                                 |                                                            |
| ``check_unused``                | Check for unused code. (Optional, defaults to 'True'.)     +
|                                 |                                                            |
+---------------------------------+------------------------------------------------------------+


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
