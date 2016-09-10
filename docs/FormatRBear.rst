`FormatRBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/r/FormatRBear.py>`_
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
| ``indent_size``              | Number of spaces per indentation level. (Optional,         |
|                              | defaults to '4'.)                                          |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
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
|                              | defaults to '0'.)                                          |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``r_use_arrows``             | Determines whether the assignment operator ``=`` should be |
|                              | replaced by an arrow ``<-`` or not.                        |
|                              | Example: If  ``True``, ``x = 1`` changes to ``x <- 1``.    |
|                              | (Optional, defaults to 'False'.)                           |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+
|                              |                                                            |
| ``tab_width``                | Number of spaces per indentation level. (Optional,         |
|                              | defaults to '4'.)                                          |
|                              |                                                            |
+------------------------------+------------------------------------------------------------+


Dependencies
------------

.. code-block:: bash

    $ R   - e   " i n s t a l l . p a c k a g e s ( " f o r m a t R " ,   r e p o = " h t t p : / / c r a n . r s t u d i o . c o m " ,   d e p e n d e n c i e s = T R U E ) "



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
