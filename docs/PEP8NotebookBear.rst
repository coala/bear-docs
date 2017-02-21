`PEP8NotebookBear <https://github.com/coala/coala-bears/tree/master/bears/python/PEP8NotebookBear.py>`_
=======================================================================================================

Detects and fixes PEP8 incompliant code in Jupyter Notebooks. This bear will not change functionality of the code in any way.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+------------------------+-------------------------------------------------------------+
| Setting                |  Meaning                                                    |
+========================+=============================================================+
|                        |                                                             |
| ``indent_size``        | Number of spaces per indent level. (Optional, defaults to   |
|                        | '4'.)                                                       |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``local_pep8_config``  | Set to true if autopep8 should use a config file as if run  |
|                        | normally from this directory. (Optional, defaults to        |
|                        | 'False'.)                                                   |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``max_line_length``    | Maximum number of characters for a line. (Optional,         |
|                        | defaults to '79'.)                                          |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``pep_ignore``         | A list of errors/warnings to ignore. (Optional, defaults to |
|                        | '()'.)                                                      |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``pep_select``         | A list of errors/warnings to exclusively apply. (Optional,  |
|                        | defaults to '()'.)                                          |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/83333.png
   :target: https://asciinema.org/a/83333?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``autopep8``
* ``pip`` - ``nbformat``


Can Detect
----------

* Formatting

Can Fix
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
