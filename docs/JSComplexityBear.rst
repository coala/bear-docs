`JSComplexityBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/js/JSComplexityBear.py>`_
====================

Calculates cyclomatic complexity using ``cr``, the command line utility
provided by the NodeJS module ``complexity-report``.

`Supported Languages <../README.rst>`_
-----

* JavaScript

Settings
--------

+-------------------+------------------------------------------------------+
| Setting           |  Meaning                                             |
+===================+======================================================+
|                   |                                                      |
| ``cc_threshold``  | Threshold value for cyclomatic complexity (Optional, |
|                   | defaults to '10'.)                                   |
|                   |                                                      |
+-------------------+------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/39250.png
   :target: https://asciinema.org/a/39250?autoplay=1
   :width: 100%

Dependencies
------------

.. code-block:: bash

    $ npm install complexity-report@2.0.0-alpha



Can Detect
----------

* Complexity

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
