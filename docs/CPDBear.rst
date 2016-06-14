**CPDBear**
===========

Checks for similar code that looks as it could be replaced to reduce redundancy.
For more details see: <https://pmd.github.io/pmd-5.4.1/usage/cpd-usage.html>

`Supported Languages <../README.rst>`:
-----

* PL/SQL
* JavaScript
* JSP
* Matlab
* C#
* Objective-C
* Ruby
* Python
* C++
* PHP
* Go
* Octave
* Scala
* Java
* Fortran
* Python 3
* Python 2
* Swift

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
| ``language``\*            | One of the supported languages of this bear.                      +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``skip_duplicate_files``  | Ignore multiple copies of files of the same name and length in    |
|                           | ompariso                                                          |
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
| ``ignore_identifiers``    | Ignore constant and variable names when comparing text.           +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+
|                           |                                                                   |
| ``minimum_tokens``        | The minimum token length which should be reported as a duplicate. +
|                           |                                                                   |
+---------------------------+-------------------------------------------------------------------+

\* denotes required param