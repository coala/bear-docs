`TailorBear <https://github.com/coala/coala-bears/tree/master/bears/swift/TailorBear.py>`_
==========================================================================================

Analyze Swift code and check for code style related
warning messages.

For more information on the analysis visit <https://tailor.sh/>

`Supported Languages <../README.rst>`_
--------------------------------------

* Swift

Settings
--------

+--------------------------+------------------------------------------------------------+
| Setting                  |  Meaning                                                   |
+==========================+============================================================+
|                          |                                                            |
| ``max_class_length``     | maximum number of lines in a Class <0-999>. (Optional,     |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_closure_length``   | maximum number of lines in a Closure <0-999>. (Optional,   |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_file_length``      | maximum number of lines in a File <0-999>. (Optional,      |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_function_length``  | maximum number of lines in a Function <0-999>. (Optional,  |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_line_length``      | maximum number of characters in a Line <0-999>. (Optional, |
|                          | defaults to '79'.)                                         |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_name_length``      | maximum length of Identifier name <0-999>. (Optional,      |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``max_struct_length``    | maximum number od lines in a Struct <0-999>. (Optional,    |
|                          | defaults to '0'.)                                          |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``min_name_length``      | minimum number of characters in Identifier name <1-999>.   |
|                          | (Optional, defaults to '1'.)                               |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+
|                          |                                                            |
| ``tailor_config``        | path to Tailor configuration file. (Optional, defaults to  |
|                          | ''.)                                                       |
|                          |                                                            |
+--------------------------+------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/45666.png
   :target: https://asciinema.org/a/45666?autoplay=1
   :width: 100%

Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
