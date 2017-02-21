`AnnotationBear <https://github.com/coala/coala-bears/tree/master/bears/general/AnnotationBear.py>`_
====================================================================================================

Finds out all the positions of strings and comments in a file. The Bear searches for valid comments and strings and yields their ranges as SourceRange objects in HiddenResults.

`Supported Languages <../README.rst>`_
--------------------------------------



Settings
--------

+------------------+------------------------------------------------------------+
| Setting          |  Meaning                                                   |
+==================+============================================================+
|                  |                                                            |
| ``coalang_dir``  | External directory for coalang file. :return: One          |
|                  | HiddenResult containing a dictionary with keys being       |
|                  | 'strings' or 'comments' and values being a tuple of        |
|                  | SourceRanges pointing to the strings and a tuple of        |
|                  | SourceRanges pointing to all comments respectively. The    |
|                  | ranges do include string quotes or the comment starting    |
|                  | separator but not anything before (e.g. when using         |
|                  | ``u"string"``, the ``u`` will not be in the source range). |
|                  | (Optional, defaults to 'None'.)                            |
|                  |                                                            |
+------------------+------------------------------------------------------------+
|                  |                                                            |
| ``language``     | The programming language of the source code.               +
|                  |                                                            |
+------------------+------------------------------------------------------------+


License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
