`YAMLLintBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/yml/YAMLLintBear.py>`_
=====================================================================================================

Check yaml code for errors and possible problems.

You can read more about capabilities at
<http://yamllint.readthedocs.org/en/latest/rules.html>.

`Supported Languages <../README.rst>`_
--------------------------------------

* YAML

Settings
--------

+----------------------+-------------------------------------------------------------+
| Setting              |  Meaning                                                    |
+======================+=============================================================+
|                      |                                                             |
| ``document_start``   | Use this rule to require or forbid the use of document      |
|                      | start marker (---). (Optional, defaults to 'False'.)        |
|                      |                                                             |
+----------------------+-------------------------------------------------------------+
|                      |                                                             |
| ``yamllint_config``  | Path to a custom configuration file. (Optional, defaults to |
|                      | ''.)                                                        |
|                      |                                                             |
+----------------------+-------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``yamllint``


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
