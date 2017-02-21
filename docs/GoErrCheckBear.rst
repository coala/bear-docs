`GoErrCheckBear <https://github.com/coala/coala-bears/tree/master/bears/go/GoErrCheckBear.py>`_
===============================================================================================

Checks the code for all function calls that have unchecked errors.
GoErrCheckBear runs ``errcheck`` over each file to find such functions.

For more information on the analysis visit
<https://github.com/kisielk/errcheck>.

`Supported Languages <../README.rst>`_
--------------------------------------

* Go

Settings
--------

+----------------+-----------------------------------------------------------+
| Setting        |  Meaning                                                  |
+================+===========================================================+
|                |                                                           |
| ``asserts``    | Enables checking for ignored type assertion results.      |
|                | (Optional, defaults to 'False'.)                          |
|                |                                                           |
+----------------+-----------------------------------------------------------+
|                |                                                           |
| ``blank``      | Enables checking for assignments of errors to the blank   |
|                | identifier. (Optional, defaults to 'False'.)              |
|                |                                                           |
+----------------+-----------------------------------------------------------+
|                |                                                           |
| ``ignore``     | Comma-separated list of pairs of the form package:regex.  |
|                | For each package, the regex describes which functions to  |
|                | ignore within that package. The package may be omitted to |
|                | have the regex apply to all packages. (Optional, defaults |
|                | to '[]'.)                                                 |
|                |                                                           |
+----------------+-----------------------------------------------------------+
|                |                                                           |
| ``ignorepkg``  | Takes a comma-separated list of package import paths to   |
|                | ignore. (Optional, defaults to '[]'.)                     |
|                |                                                           |
+----------------+-----------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/46834.png
   :target: https://asciinema.org/a/46834?autoplay=1
   :width: 100%

Dependencies
------------

* ``go`` - ``github.com/kisielk/errcheck``


Can Detect
----------

* Syntax

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
