**PEP8Bear**
============

Detects and fixes PEP8 incompliant code. This bear will not change functionality of the code in any way.

`Supported Languages <../README.rst>`_
-----

* Python
* Python 2
* Python 3

Settings
--------

+------------------------+----------------------------------------------+
| Setting                |  Meaning                                     |
+========================+==============================================+
|                        |                                              |
| ``local_pep8_config``  | Set to true if autopep8 should use a config  |
|                        | file as if run normally from this directory. |
|                        |                                              |
+------------------------+----------------------------------------------+
|                        |                                              |
| ``max_line_length``    | Maximum number of characters for a line.     +
|                        |                                              |
+------------------------+----------------------------------------------+
|                        |                                              |
| ``pep_ignore``         | A list of errors/warnings to ignore.         +
|                        |                                              |
+------------------------+----------------------------------------------+
|                        |                                              |
| ``pep_select``         | A list of errors/warnings to exclusively     |
|                        | apply.                                       |
|                        |                                              |
+------------------------+----------------------------------------------+
|                        |                                              |
| ``tab_width``          | Number of spaces per indent level.           +
|                        |                                              |
+------------------------+----------------------------------------------+

\* denotes required param

Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
