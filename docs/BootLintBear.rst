`BootLintBear <https://github.com/coala/coala-bears/tree/master/bears/hypertext/BootLintBear.py>`_
==================================================================================================

Raise several common HTML mistakes in html files that are using
Bootstrap in a fairly "vanilla" way. Vanilla Bootstrap's components/widgets
require their parts of the DOM to conform to certain structures that is
checked. Also, raises issues about certain <meta> tags, HTML5 doctype
declaration, etc. to use bootstrap properly.

For more about the analysis, check Bootlint
<https://github.com/twbs/bootlint#bootlint>.

`Supported Languages <../README.rst>`_
--------------------------------------

* HTML

Settings
--------

+----------------------+-----------------------------------------------------------+
| Setting              |  Meaning                                                  |
+======================+===========================================================+
|                      |                                                           |
| ``bootlint_ignore``  | List of checkers to ignore. (Optional, defaults to '[]'.) +
|                      |                                                           |
+----------------------+-----------------------------------------------------------+


Dependencies
------------

* ``npm`` - ``bootlint``


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
