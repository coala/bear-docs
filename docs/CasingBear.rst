`CasingBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/general/CasingBear.py>`_
==============

Checks whether all identifier names (variables, classes, objects) follow a certain naming convention.

`Supported Languages <../README.rst>`_
-----



Settings
--------

+------------------+----------------------------------------------------------+
| Setting          |  Meaning                                                 |
+==================+==========================================================+
|                  |                                                          |
| ``casing``       | "camel" for camelCasing or "snake" for snake_casing or   |
|                  | "pascal" for PascalCasing.                               |
|                  |                                                          |
+------------------+----------------------------------------------------------+
|                  |                                                          |
| ``coalang_dir``  | External directory for the coalang file. (Optional,      |
|                  | defaults to 'None'.)                                     |
|                  |                                                          |
+------------------+----------------------------------------------------------+
|                  |                                                          |
| ``language``     | The language of the file, which is used to determine the |
|                  | keywords to ignore.                                      |
|                  |                                                          |
+------------------+----------------------------------------------------------+
