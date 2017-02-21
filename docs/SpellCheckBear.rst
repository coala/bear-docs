`SpellCheckBear <https://github.com/coala/coala-bears/tree/master/bears/natural_language/SpellCheckBear.py>`_
=============================================================================================================

Lints files to check for incorrect spellings using ``scspell``.

scspell is a spell checker for source code.
When applied to a code written in most popular programming languages
while using most typical naming conventions, this algorithm will
usually catch many errors without an annoying false positive rate.

In an effort to catch more spelling errors, scspell is able to
check each file against a set of dictionary words selected
specifically for that file.

See <https://pypi.python.org/pypi/scspell3k> for more information.

`Supported Languages <../README.rst>`_
--------------------------------------

* Natural Language



Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/87753.png
   :target: https://asciinema.org/a/87753?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``scspell3k``


Can Detect
----------

* Spelling

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
