`FormatRBear <https://github.com/coala/coala-bears/tree/master/bears/r/FormatRBear.py>`_
========================================================================================

Check and correct formatting of R Code using known formatR utility.

`Supported Languages <../README.rst>`_
--------------------------------------

* R

Settings
--------

+------------------------------+-------------------------------------------------------------+
| Setting                      |  Meaning                                                    |
+==============================+=============================================================+
|                              |                                                             |
| ``indent_size``              | Number of spaces per indentation level. (Optional, defaults |
|                              | to '4'.)                                                    |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+
|                              |                                                             |
| ``r_braces_on_next_line``    | Determines whether a brace should be placed on the next     |
|                              | line.                                                       |
|                              | Example: If ``True``, ``` if (...) { ``` changes to ``` if  |
|                              | (...) { ``` If ``False`` the brace is placed on the same    |
|                              | line. (Optional, defaults to 'False'.)                      |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+
|                              |                                                             |
| ``r_keep_blank_lines``       | Determines whether blank lines are kept or not. (Optional,  |
|                              | defaults to 'True'.)                                        |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+
|                              |                                                             |
| ``r_keep_comments``          | Determines whether comments are kept or not. (Optional,     |
|                              | defaults to 'True'.)                                        |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+
|                              |                                                             |
| ``r_max_expression_length``  | Maximum number of characters for an expression.             |
|                              | Example: If ``20`` then ``` 1 + 1 + 1 + 1 + 1 + 1 + 1 ```   |
|                              | changes to ``` 1 + 1 + 1 + 1 + 1 + 1 + 1 ``` (Optional,     |
|                              | defaults to '0'.)                                           |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+
|                              |                                                             |
| ``r_use_arrows``             | Determines whether the assignment operator ``=`` should be  |
|                              | replaced by an arrow ``<-`` or not.                         |
|                              | Example: If  ``True``, ``x = 1`` changes to ``x <- 1``.     |
|                              | (Optional, defaults to 'False'.)                            |
|                              |                                                             |
+------------------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/0y0oxtak18v492jdyfqwpw1n4.png
   :target: https://asciinema.org/a/0y0oxtak18v492jdyfqwpw1n4?autoplay=1
   :width: 100%

Dependencies
------------

* ``R`` - ``formatR``


Can Detect
----------

* Formatting

Can Fix
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
