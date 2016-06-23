**FormatRBear**
===============

Check and correct formatting of R Code using known formatR utility.

`Supported Languages <../README.rst>`_
-----

* R

Settings
--------

+------------------------------+------------------------------------------------------------+
| Setting                      |  Meaning                                                   |
+==============================+============================================================+
|                              |                                                            |
| ``r_braces_on_next_line``    | Determines whether a brace should be placed on the next    |
|                              | line.                                                      |
|                              | Example: If ``True``, ``` if (...) { ``` changes to ``` if |
|                              | (...) { ``` If ``False`` the brace is placed on the same   |
|                              | line. (Optional, defaults to 'False'.)                     |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``r_keep_blank_lines``       | Determines whether blank lines are kept or not. (Optional, |
|                              | defaults to 'True'.)                                       |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``r_keep_comments``          | Determines whether comments are kept or not. (Optional,    |
|                              | defaults to 'True'.)                                       |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``r_max_expression_length``  | Maximum number of characters for an expression.            |
|                              | Example: If ``20`` then ``` 1 + 1 + 1 + 1 + 1 + 1 + 1 ```  |
|                              | changes to ``` 1 + 1 + 1 + 1 + 1 + 1 + 1 ``` (Optional,    |
|                              | defaults to '20'.)                                         |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``r_use_arrows``             | Determines if either the assign operator ``=`` or the      |
|                              | arrow ``<-`` should be used.                               |
|                              | Example: If  ``True``, ``x = 1`` changes to ``x <- 1``.    |
|                              | (Optional, defaults to 'False'.)                           |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``tab_width``                | Number of spaces for indentation. (Optional, defaults to   |
|                              | '4'.)                                                      |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+

\* denotes required param

Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
