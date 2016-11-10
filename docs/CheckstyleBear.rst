`CheckstyleBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/java/CheckstyleBear.py>`_
==================

Check Java code for possible style, semantic and design issues.

For more information, consult
<http://checkstyle.sourceforge.net/checks.html>.

`Supported Languages <../README.rst>`_
-----

* Java

Settings
--------

+-------------------------+------------------------------------------------------------+
| Setting                 |  Meaning                                                   |
+=========================+============================================================+
|                         |                                                            |
| ``checkstyle_configs``  | A file containing configs to use in ``checkstyle``. It can |
|                         | also have the special values:                              |
|                         | - google - Google's Java style. More info at               |
|                         | <http://checkstyle.sourceforge.net/style_configs.html>. -  |
|                         | sun - Sun's Java style. These are the same as the default  |
|                         | Eclipse checks. More info at                               |
|                         | <http://checkstyle.sourceforge.net/style_configs.html>. -  |
|                         | android-check-easy - The easy Android configs provided by  |
|                         | the android-check eclipse plugin. More info at             |
|                         | <https://github.com/noveogroup/android-check>. -           |
|                         | android-check-hard - The hard Android confis provided by   |
|                         | the android-check eclipse plugin. More info at             |
|                         | <https://github.com/noveogroup/android-check>. - geosoft - |
|                         | The Java style followed by GeoSoft. More info at           |
|                         | <http://geosoft.no/development/javastyle.html> (Optional,  |
|                         | defaults to 'google'.)                                     |
|                         |                                                            |
+-------------------------+------------------------------------------------------------+
|                         |                                                            |
| ``indent_size``         | No description given. (Optional, defaults to '2'.)         +
|                         |                                                            |
+-------------------------+------------------------------------------------------------+
|                         |                                                            |
| ``use_spaces``          | No description given. (Optional, defaults to 'True'.)      +
|                         |                                                            |
+-------------------------+------------------------------------------------------------+


Can Detect
----------

* Formatting
* Smell

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
