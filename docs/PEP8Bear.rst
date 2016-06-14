**PEP8Bear**
============

Detects and fixes PEP8 incompliant code. This bear will not change functionality of the code in any way.

Supported Languages:
-----

* Python
* Python 2
* Python 3

Settings
--------

+------------------------+---------------------------------------------+
| Setting                |  Meaning                                    |
+========================+=============================================+
|                        |                                             |
| ``pep_select``         | A list of errors/warnings to exclusively    |
|                        | apply.                                      |
|                        |                                             |
+------------------------+---------------------------------------------+
|                        |                                             |
| ``local_pep8_config``  | Set to true if autopep8 should use a config |
|                        | file as if run normally from this director  |
|                        |                                             |
+------------------------+---------------------------------------------+
|                        |                                             |
| ``pep_ignore``         | A list of errors/warnings to ignore.        +
|                        |                                             |
+------------------------+---------------------------------------------+
|                        |                                             |
| ``max_line_length``    | Maximum number of characters for a line.    +
|                        |                                             |
+------------------------+---------------------------------------------+
|                        |                                             |
| ``tab_width``          | Number of spaces per indent level.          +
|                        |                                             |
+------------------------+---------------------------------------------+

\* denotes required param