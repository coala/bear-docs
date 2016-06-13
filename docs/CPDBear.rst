**CPDBear**
===========

Checks for similar code that looks as it could be replaced to reduce redundancy.
For more details see: <https://pmd.github.io/pmd-5.4.1/usage/cpd-usage.html>

Supported Languages:
-----

* C++
* C#
* Objective C
* Java
* JavaScript
* Fortran
* Go
* JSP
* Python 2
* Python 3
* Python
* Ruby
* PHP
* Scala

Settings
--------

+---------------------------+-------------------------------------------------------------------+
| Setting                   |  Meaning                                                          |
+===========================+===================================================================+
|                           |                                                                   |
| ``language``\*            | One of "cpp", "cs", "js", "f", "go", "jsp", "m", "php", "py",     |
|                           | "rb", "scala", "java" (i.e. the file ending of your language).    |
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_annotations``    | Ignore language annotations when comparing text.                  +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_literals``       | Ignore number values and string contents when comparing text.     +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_usings``         | Ignore ``using`` directives in C#.                                +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``skip_duplicate_files``  | Ignore multiple copies of files of the same name and length in    |
|                           | ompariso                                                          |
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``minimum_tokens``        | The minimum token length which should be reported as a duplicate. +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_identifiers``    | Ignore constant and variable names when comparing text.           +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+

\* denotes required param