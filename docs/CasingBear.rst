**CasingBear**
==============

Checks whether all identifier names (variables, classes, objects) follow a certain naming convention.

Supported Languages:
-----



Settings
--------

+-------------------------+---------------------------------------------+
| Setting                 |  Meaning                                    |
+=========================+=============================================+
|                         |                                             |
| ``casing``\*            | camelCasing or snake_casing or PascalCasing +
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``filename``            | Name of the file that needs to be checked.  +
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``file``                | File that needs to be checked in the form   |
|                         | of a list of strings.                       |
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``language``\*          | The language of the file, which is used to  |
|                         | determine the keywords to ignor             |
|                         |                                             |
+-------------------------+---------------------------------------------+
|                         |                                             |
| ``dependency_results``  | A dict of dependencies with bear name as    |
|                         | key and results as value                    |
|                         |                                             |
+-------------------------+---------------------------------------------+

\* denotes required param