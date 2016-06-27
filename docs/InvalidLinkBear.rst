**InvalidLinkBear**
===================

Find links in any text file and check if they are valid.
A link is considered valid if the server responds with a 2xx code.
This bear can automatically fix redirects, but ignores redirect URLs that have a huge difference with the original URL.
Warning: This bear will make HEAD requests to all URLs mentioned in your codebase, which can potentially be destructive. As an example, this bear would naively just visit the URL from a line that goes like `do_not_ever_open = 'https://api.acme.inc/delete-all-data'` wiping out all your data.

`Supported Languages <../README.rst>`_
-----

* All

Settings
--------

+-------------------+------------------------------------------------------+
| Setting           |  Meaning                                             |
+===================+======================================================+
|                   |                                                      |
| ``ignore_regex``  | A regex for urls to ignore. (Optional, defaults to   |
|                   | '[.\/]example\.com'.)                                |
|                   |                                                      |
+-------------------+------------------------------------------------------+
|                   |                                                      |
| ``timeout``       | Request timeout period. (Optional, defaults to '2'.) +
|                   |                                                      |
+-------------------+------------------------------------------------------+


Can Detect
----------

* Documentation

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
