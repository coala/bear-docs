`LicenseCheckBear <https://github.com/coala/coala-bears/tree/master/bears/upload/LicenseCheckBear/coalaLicenseCheckBear/LicenseCheckBear.py>`_
==============================================================================================================================================

Attempts to check the given file for a license, by searching the start
of the file for text belonging to various licenses.

For Ubuntu/Debian users, the ``licensecheck_lines`` option has to be used
in accordance with the ``licensecheck_tail`` option.

`Supported Languages <../README.rst>`_
--------------------------------------

* All

Settings
--------

+-------------------------+-------------------------------------------------------------+
| Setting                 |  Meaning                                                    |
+=========================+=============================================================+
|                         |                                                             |
| ``licensecheck_lines``  | Specify how many lines of the file header should be parsed  |
|                         | for license information. Set to 0 to parse the whole file   |
|                         | (and ignore ``licensecheck_tail``). (Optional, defaults to  |
|                         | '60'.)                                                      |
|                         |                                                             |
+-------------------------+-------------------------------------------------------------+
|                         |                                                             |
| ``licensecheck_tail``   | Specify how many bytes to parse at end of file. Set to 0 to |
|                         | disable parsing from end of file. (Optional, defaults to    |
|                         | '5000'.)                                                    |
|                         |                                                             |
+-------------------------+-------------------------------------------------------------+


Dependencies
------------

* System requirement
  - ``dnf`` - ``licensecheck``  - ``apt_get`` - ``devscripts``


Can Detect
----------

* License

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
