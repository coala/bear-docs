`VerilogLintBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/verilog/VerilogLintBear.py>`_
===============================================================================================================

Analyze Verilog code using ``verilator`` and checks for all lint
related and code style related warning messages. It supports the
synthesis subset of Verilog, plus initial statements, proper
blocking/non-blocking assignments, functions, tasks.

It also warns about unused code when a specified signal is never sinked,
and unoptimized code due to some construct, with which the
optimization of the specified signal or block is disabled.

This is done using the ``--lint-only`` command. For more information visit
<http://www.veripool.org/projects/verilator/wiki/Manual-verilator>.

`Supported Languages <../README.rst>`_
-----

* Verilog



Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/45275.png
   :target: https://asciinema.org/a/45275?autoplay=1
   :width: 100%

Dependencies
------------

* System requirement
  - ``apt_get`` - ``verilator``


Can Detect
----------

* Code Simplification
* Formatting
* Syntax
* Unused Code

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
