`RSTcheckBear <https://github.com/coala/coala-bears/tree/master/bears/rest/RSTcheckBear.py>`_
=============================================================================================

Check syntax of ``reStructuredText`` and code blocks
nested within it.

Check <https://pypi.python.org/pypi/rstcheck> for more information.

`Supported Languages <../README.rst>`_
--------------------------------------

* reStructuredText

Settings
--------

+---------------------------------+-------------------------------------------------------------+
| Setting                         |  Meaning                                                    |
+=================================+=============================================================+
|                                 |                                                             |
| ``code_block_language_ignore``  | Comma seperated list for languages of which code blocks     |
|                                 | should be ignored. Code block of following languages can be |
|                                 | detected: ``bash``, ``c``, ``cpp``, ``json``, ``python``,   |
|                                 | ``rst``. (Optional, defaults to '()'.)                      |
|                                 |                                                             |
+---------------------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/8ntlaqubk2qkrn9mm0dh07rlk?speed=2.png
   :target: https://asciinema.org/a/8ntlaqubk2qkrn9mm0dh07rlk?speed=2?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``rstcheck``


Can Detect
----------

* Formatting
* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
