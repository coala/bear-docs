`CPDBear <https://github.com/coala/coala-bears/tree/master/bears/general/CPDBear.py>`_
======================================================================================

Checks for similar code that looks as it could be replaced to reduce redundancy.
For more details see: <https://pmd.github.io/pmd-5.4.1/usage/cpd-usage.html>

`Supported Languages <../README.rst>`_
--------------------------------------

* C#
* C++
* Fortran
* Go
* JSP
* Java
* JavaScript
* Matlab
* Objective-C
* Octave
* PHP
* PL/SQL
* Python
* Python 2
* Python 3
* Ruby
* Scala
* Swift

Settings
--------

+---------------------------+-------------------------------------------------------------+
| Setting                   |  Meaning                                                    |
+===========================+=============================================================+
|                           |                                                             |
| ``ignore_annotations``    | Ignore language annotations when comparing text. (Optional, |
|                           | defaults to 'False'.)                                       |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``ignore_identifiers``    | Ignore constant and variable names when comparing text.     |
|                           | (Optional, defaults to 'True'.)                             |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``ignore_literals``       | Ignore number values and string contents when comparing     |
|                           | text. (Optional, defaults to 'False'.)                      |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``ignore_usings``         | Ignore ``using`` directives in C#. (Optional, defaults to   |
|                           | 'False'.)                                                   |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``language``              | One of the supported languages of this bear.                +
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``minimum_tokens``        | The minimum token length which should be reported as a      |
|                           | duplicate. (Optional, defaults to '20'.)                    |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+
|                           |                                                             |
| ``skip_duplicate_files``  | Ignore multiple copies of files of the same name and length |
|                           | in comparison. (Optional, defaults to 'True'.)              |
|                           |                                                             |
+---------------------------+-------------------------------------------------------------+


Can Detect
----------

* Duplication

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
