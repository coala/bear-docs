**CPDBear**
===========

Checks for similar code that looks as it could be replaced to reduce redundancy.
For more details see: <https://pmd.github.io/pmd-5.4.1/usage/cpd-usage.html>

`Supported Languages <../README.rst>`_ :
-----

* Python 3
* Swift
* Python
* PHP
* JSP
* Ruby
* JavaScript
* Scala
* C#
* Java
* Python 2
* Octave
* C++
* Fortran
* Go
* Objective-C
* Matlab
* PL/SQL

Settings
--------

+---------------------------+-------------------------------------------------------------------+
| Setting                   |  Meaning                                                          |
+===========================+===================================================================+
|                           |                                                                   |
| ``ignore_usings``         | Ignore ``using`` directives in C#.                                +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_literals``       | Ignore number values and string contents when comparing text.     +
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
| ``language``\*            | One of the supported languages of this bear.                      +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_annotations``    | Ignore language annotations when comparing text.                  +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_identifiers``    | Ignore constant and variable names when comparing text.           +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+

\* denotes required param