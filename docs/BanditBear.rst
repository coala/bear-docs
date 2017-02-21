`BanditBear <https://github.com/coala/coala-bears/tree/master/bears/python/BanditBear.py>`_
===========================================================================================

Performs security analysis on Python source code, utilizing the ``ast``
module from the Python standard library.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+---------------------------+------------------------------------------------------------+
| Setting                   |  Meaning                                                   |
+===========================+============================================================+
|                           |                                                            |
| ``bandit_skipped_tests``  | The IDs of the tests ``bandit`` shall not perform. You can |
|                           | get information about the available builtin codes at       |
|                           | https://github.com/openstack/bandit#usage. (Optional,      |
|                           | defaults to '('B105', 'B106', 'B107', 'B404', 'B603',      |
|                           | 'B606', 'B607')'.)                                         |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``bandit``


Can Detect
----------

* Security

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
