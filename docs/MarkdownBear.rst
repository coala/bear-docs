`MarkdownBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/markdown/MarkdownBear.py>`_
================

Check and correct Markdown style violations automatically.

See <https://github.com/wooorm/remark-lint> for details about the tool
below.

`Supported Languages <../README.rst>`_
-----

* Markdown

Settings
--------

+--------------------------------------+-------------------------------------------------------------+
| Setting                              |  Meaning                                                    |
+======================================+=============================================================+
|                                      |                                                             |
| ``markdown_bullets``                 | Character to use for bullets in lists. Can be "-", "*" or   |
|                                      | "+". (Optional, defaults to '-'.)                           |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_closed_headings``         | Whether to close Atx headings or not. if true, extra #      |
|                                      | marks will be required after the heading. eg: `## Heading   |
|                                      | ##`. (Optional, defaults to 'False'.)                       |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_codefence``               | Used to find which characters to use for code fences. Can   |
|                                      | be "`" or "~". (Optional, defaults to '`'.)                 |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_emphasis``                | Character to wrap strong emphasis by. Can be "_" or "*".    |
|                                      | (Optional, defaults to '*'.)                                |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_encode_entities``         | Whether to encode symbols that are not ASCII into special   |
|                                      | HTML characters. (Optional, defaults to 'False'.)           |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_fences``                  | Use fences for code blocks. (Optional, defaults to 'True'.) +
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_horizontal_rule_repeat``  | The number of times the horizontal rule character will be   |
|                                      | repeated. (Optional, defaults to '3'.)                      |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_horizontal_rule_spaces``  | Whether spaces should be added between horizontal rule      |
|                                      | characters. (Optional, defaults to 'False'.)                |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_horizontal_rule``         | The horizontal rule character. Can be '*', '_' or '-'.      |
|                                      | (Optional, defaults to '*'.)                                |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_list_increment``          | Whether an ordered lists numbers should be incremented.     |
|                                      | (Optional, defaults to 'True'.)                             |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_list_indent``             | Used to find spacing after bullet in lists. Can be "1",     |
|                                      | "tab" or "mixed".                                           |
|                                      | - "1" - 1 space after bullet. - "tab" - Use tab stops to    |
|                                      | begin a sentence after the bullet. - "mixed" - Use "1" when |
|                                      | the list item is only 1 line, "tab" if it spans multiple.   |
|                                      | (Optional, defaults to '1'.)                                |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_loose_tables``            | Whether to use pipes for the outermost borders in a table.  |
|                                      | (Optional, defaults to 'False'.)                            |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_setext_headings``         | Whether to use setext headings. A setext heading uses       |
|                                      | underlines instead of # marks. (Optional, defaults to       |
|                                      | 'False'.)                                                   |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_spaced_tables``           | Whether to add space between pipes in a table. (Optional,   |
|                                      | defaults to 'True'.)                                        |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+
|                                      |                                                             |
| ``markdown_strong``                  | Character to wrap slight emphasis by. Can be "_" or "*".    |
|                                      | (Optional, defaults to '*'.)                                |
|                                      |                                                             |
+--------------------------------------+-------------------------------------------------------------+


Dependencies
------------

.. code-block:: bash

    $ npm install remark@3



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
