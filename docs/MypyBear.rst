`MypyBear <https://github.com/coala/coala-bears/tree/master/bears/python/MypyBear.py>`_
=======================================================================================

Type-checks your Python files!

Checks optional static typing using the mypy tool.
See <http://mypy.readthedocs.io/en/latest/basics.html> for info on how to
add static typing.

`Supported Languages <../README.rst>`_
--------------------------------------

* Python
* Python 2
* Python 3

Settings
--------

+------------------------------------+-------------------------------------------------------------------+
| Setting                            |  Meaning                                                          |
+====================================+===================================================================+
|                                    |                                                                   |
| ``allow_untyped_calls``            | Allow calling functions without type annotations from typed       |
|                                    | functions. (Optional, defaults to 'True'.)                        |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+
|                                    |                                                                   |
| ``allow_untyped_functions``        | Allow defining functions without type annotations or with         |
|                                    | incomplete type annotations. (Optional, defaults to 'True'.)      |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+
|                                    |                                                                   |
| ``check_untyped_function_bodies``  | Do not check the interior of functions without type               |
|                                    | annotations. (Optional, defaults to 'False'.)                     |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+
|                                    |                                                                   |
| ``language``                       | Set to ``Python`` or ``Python 3`` to check Python 3.x             |
|                                    | source. Use ``Python 2`` for Python 2.x. (Optional,               |
|                                    | defaults to 'Python 3'.)                                          |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+
|                                    |                                                                   |
| ``python_version``                 | Set the specific Python version, e.g. ``3.5``. (Optional,         |
|                                    | defaults to 'None'.)                                              |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+
|                                    |                                                                   |
| ``strict_optional``                | Enable experimental strict checks related to Optional             |
|                                    | types. See                                                        |
|                                    | <http://mypy-lang.blogspot.com.es/2016/07/mypy-043-released.html> |
|                                    | for an explanation. (Optional, defaults to 'False'.)              |
|                                    |                                                                   |
+------------------------------------+-------------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/90736.png
   :target: https://asciinema.org/a/90736?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``mypy-lang``


License
-------

AGPL-3.0

Authors
-------

* Petr Viktorin (encukou@gmail.com)
