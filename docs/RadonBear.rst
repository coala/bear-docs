`RadonBear <https://github.com/coala/coala-bears/tree/master/bears/python/RadonBear.py>`_
=========================================================================================

Uses radon to compute complexity of a given file.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+-------------------------+---------------------------------------------------------+
| Setting                 |  Meaning                                                |
+=========================+=========================================================+
|                         |                                                         |
| ``radon_ranks_info``    | The ranks (given by radon) to treat as severity INFO.   |
|                         | (Optional, defaults to '()'.)                           |
|                         |                                                         |
+-------------------------+---------------------------------------------------------+
|                         |                                                         |
| ``radon_ranks_major``   | The ranks (given by radon) to treat as severity MAJOR.  |
|                         | (Optional, defaults to '('E', 'F')'.)                   |
|                         |                                                         |
+-------------------------+---------------------------------------------------------+
|                         |                                                         |
| ``radon_ranks_normal``  | The ranks (given by radon) to treat as severity NORMAL. |
|                         | (Optional, defaults to '('C', 'D')'.)                   |
|                         |                                                         |
+-------------------------+---------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``radon``


Can Detect
----------

* Complexity

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
