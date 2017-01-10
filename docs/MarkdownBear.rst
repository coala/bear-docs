`MarkdownBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/markdown/MarkdownBear.py>`_
==========================================================================================================

Check and correct Markdown style violations automatically.

See <https://github.com/wooorm/remark-lint> for details about the tool
below.

`Supported Languages <../README.rst>`_
--------------------------------------

* Markdown

Settings
--------

+-----------------------------+-------------------------------------------------------------+
| Setting                     |  Meaning                                                    |
+=============================+=============================================================+
|                             |                                                             |
| ``bullets``                 | Character to use for bullets in lists. Can be "-", "*" or   |
|                             | "+". (Optional, defaults to '-'.)                           |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``closed_headings``         | Whether to close Atx headings or not. if true, extra #      |
|                             | marks will be required after the heading. eg: `## Heading   |
|                             | ##`. (Optional, defaults to 'False'.)                       |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``codefence``               | Used to find which characters to use for code fences. Can   |
|                             | be "`" or "~". (Optional, defaults to '`'.)                 |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``emphasis``                | Character to wrap strong emphasis by. Can be "_" or "*".    |
|                             | (Optional, defaults to '*'.)                                |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``encode_entities``         | Whether to encode symbols that are not ASCII into special   |
|                             | HTML characters. (Optional, defaults to 'False'.)           |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``fences``                  | Use fences for code blocks. (Optional, defaults to 'True'.) +
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``horizontal_rule_repeat``  | The number of times the horizontal rule character will be   |
|                             | repeated. (Optional, defaults to '3'.)                      |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``horizontal_rule_spaces``  | Whether spaces should be added between horizontal rule      |
|                             | characters. (Optional, defaults to 'False'.)                |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``horizontal_rule``         | No description given. (Optional, defaults to '*'.)          +
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``list_increment``          | Whether an ordered lists numbers should be incremented.     |
|                             | (Optional, defaults to 'True'.)                             |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``list_indent``             | Used to find spacing after bullet in lists. Can be "1",     |
|                             | "tab" or "mixed". - "1" - 1 space after bullet. - "tab" -   |
|                             | Use tab stops to begin a sentence after the bullet. -       |
|                             | "mixed" - Use "1" when the list item is only 1 line, "tab"  |
|                             | if it spans multiple. (Optional, defaults to '1'.)          |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``loose_tables``            | Whether to use pipes for the outermost borders in a table.  |
|                             | (Optional, defaults to 'False'.)                            |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``max_line_length``         | The maximum line length allowed. (Optional, defaults to     |
|                             | '80'.)                                                      |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``setext_headings``         | Whether to use setext headings. A setext heading uses       |
|                             | underlines instead of # marks. (Optional, defaults to       |
|                             | 'False'.)                                                   |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``spaced_tables``           | Whether to add space between pipes in a table. (Optional,   |
|                             | defaults to 'True'.)                                        |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+
|                             |                                                             |
| ``strong``                  | Character to wrap slight emphasis by. Can be "_" or "*".    |
|                             | (Optional, defaults to '*'.)                                |
|                             |                                                             |
+-----------------------------+-------------------------------------------------------------+


Dependencies
------------

* ``npm`` - ``remark-cli``


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
