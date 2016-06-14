**CPDBear**
===========

Checks for similar code that looks as it could be replaced to reduce redundancy.
For more details see: <https://pmd.github.io/pmd-5.4.1/usage/cpd-usage.html>

`Supported Languages <../README.rst>_`:
-----

* Scala
* Python 2
* Go
* JSP
* Octave
* PL/SQL
* Ruby
* Matlab
* C#
* PHP
* Python
* Python 3
* C++
* Objective-C
* Fortran
* Swift
* Java
* JavaScript

Settings
--------

+---------------------------+-------------------------------------------------------------------+
| Setting                   |  Meaning                                                          |
+===========================+===================================================================+
|                           |                                                                   |
| ``ignore_identifiers``    | Ignore constant and variable names when comparing text.           +
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
| ``language``\*            | One of the supported languages of this bear.                      +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_annotations``    | Ignore language annotations when comparing text.                  +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``minimum_tokens``        | The minimum token length which should be reported as a duplicate. +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``ignore_usings``         | Ignore ``using`` directives in C#.                                +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+

\* denotes required param