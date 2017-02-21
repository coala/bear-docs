`Jinja2Bear <https://github.com/coala/coala-bears/tree/master/bears/jinja2/Jinja2Bear.py>`_
===========================================================================================

Check `Jinja2 templates <http://jinja.pocoo.org>`_ for syntax, formatting and documentation issues. The following aspects are being looked at:
* Variable spacing: Variable tags should be padded with one space on each side, like this: ``{{ var_name }}``. This can be set to any number of spaces via the setting ``variable_spacing``. Malformatted variable tags are detected and fixes suggested. * Control spacing: Like variable spacing, but for control blocks, i.e. ``if`` and ``for`` constructs. Looks at both start and end block. * Control labels: It is good practice to label the end of an ``if`` or ``for`` construct with a comment equal to the content of the start, like so::
{% for x in y %} do something {% endfor %}{# for x in y %}
Mising or differing labels are detected and fixes suggested. Constructs with start and end on the same line are being ignored. * unbalanced blocks: Each opening tag for a ``for`` or ``if`` construct must be closed by a corresponding end tag. An unbalanced number of opening and closing tags is invalid syntax and will be reported with MAJOR severity by the bear.

`Supported Languages <../README.rst>`_
--------------------------------------

* Jinja2

Settings
--------

+-----------------------+-------------------------------------------------------------+
| Setting               |  Meaning                                                    |
+=======================+=============================================================+
|                       |                                                             |
| ``control_spacing``   | The number of spaces a control block should be spaced with. |
|                       | Default is 1. (Optional, defaults to '1'.)                  |
|                       |                                                             |
+-----------------------+-------------------------------------------------------------+
|                       |                                                             |
| ``variable_spacing``  | The number of spaces a variable block should be spaced      |
|                       | with. Default is 1. (Optional, defaults to '1'.)            |
|                       |                                                             |
+-----------------------+-------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/azi6u1gcxutoxn0l7xpu4pljp.png
   :target: https://asciinema.org/a/azi6u1gcxutoxn0l7xpu4pljp?autoplay=1
   :width: 100%

Can Detect
----------

* Documentation
* Formatting
* Syntax

Can Fix
----------

* Documentation
* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
