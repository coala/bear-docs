**ClangComplexityBear**
=======================

Check for all functions if they are too complicated using the cyclomatic complexity metric.
You can read more about this metric at <https://www.wikiwand.com/en/Cyclomatic_complexity>.

`Supported Languages <../README.rst>_`:
-----

* C
* C++
* Objective-C
* Objective-C++
* OpenMP
* OpenCL
* CUDA

Settings
--------

+---------------------+-----------------------------------------------+
| Setting             |  Meaning                                      |
+=====================+===============================================+
|                     |                                               |
| ``max_complexity``  | Maximum cyclomatic complexity that is         |
|                     | considered to be normal. The value of 10 had  |
|                     | received substantial corroborating evidence.  |
|                     | But the general recommendation: "For each     |
|                     | module, either limit cyclomatic complexity to |
|                     | [the agreed-upon limit] or provide a written  |
|                     | explanation of why the limit was exceeded     |
|                     |                                               |
+---------------------+-----------------------------------------------+

\* denotes required param