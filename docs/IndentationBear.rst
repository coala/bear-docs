**IndentationBear**
===================

It is a generic indent bear, which looks for a start and end indent specifier, example: ``{ : }`` where "{" is the start indent specifier and "}" is the end indent specifier. If the end-specifier is not given, this bear looks for unindents within the code to correctly figure out indentation.
It does not however support hanging indents or absolute indents of any sort, also indents based on keywords are not supported yet. for example:
if(something) does not get indented
undergoes no change.

`Supported Languages <../README.rst>`_
-----



Settings
--------

+-------------------------+-----------------------------------------------------------------+
| Setting                 |  Meaning                                                        |
+=========================+=================================================================+
|                         |                                                                 |
| ``coalang_dir``         | Full path of external directory containing the coalang          |
|                         | file for language.                                              |
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``dependency_results``  | Results given by the AnnotationBear.                            +
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``file``                | File that needs to be checked in the form of a list of strings. +
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``filename``            | Name of the file that needs to be checked.                      +
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``language``\*          | Language to be used for indentation.                            +
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``tab_width``           | No. of spaces to insert for indentation.                        |
|                         | Only Applicable if use_spaces is False.                         |
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+
|                         |                                                                 |
| ``use_spaces``          | Insert spaces instead of tabs for indentation.                  +
|                         |                                                                 |
+-------------------------+-----------------------------------------------------------------+

\* denotes required param