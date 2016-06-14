**CasingBear**
==============

Checks whether all identifier names (variables, classes, objects) follow a certain naming convention.

`Supported Languages <../README.rst>`:
-----



Settings
--------

+-------------------------+---------------------------------------------+
| Setting                 |  Meaning                                    |
+=========================+=============================================+
|                         |                                             |
| ``language``\*          | The language of the file, which is used to  |
|                         | determine the keywords to ignor             |
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``casing``\*            | camelCasing or snake_casing or PascalCasing +
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``file``                | File that needs to be checked in the form   |
|                         | of a list of strings.                       |
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``dependency_results``  | A dict of dependencies with bear name as    |
|                         | key and results as value                    |
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``filename``            | Name of the file that needs to be checked.  +
|                         |                                             |
+-------------------------+---------------------------------------------+

\* denotes required param