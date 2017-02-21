`InvalidLinkBear <https://github.com/coala/coala-bears/tree/master/bears/general/InvalidLinkBear.py>`_
======================================================================================================

Find links in any text file and check if they are valid.
A link is considered valid if the server responds with a 2xx code.
This bear can automatically fix redirects, but ignores redirect URLs that have a huge difference with the original URL.
Warning: This bear will make HEAD requests to all URLs mentioned in your codebase, which can potentially be destructive. As an example, this bear would naively just visit the URL from a line that goes like `do_not_ever_open = 'https://api.acme.inc/delete-all-data'` wiping out all your data.

`Supported Languages <../README.rst>`_
--------------------------------------

* All

Settings
--------

+------------------------+-------------------------------------------------------------+
| Setting                |  Meaning                                                    |
+========================+=============================================================+
|                        |                                                             |
| ``follow_redirects``   | Set to true to autocorrect redirects. (Optional, defaults   |
|                        | to 'False'.)                                                |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``link_ignore_list``   | Comma separated url globs to ignore (Optional, defaults to  |
|                        | ''.)                                                        |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``link_ignore_regex``  | A regex for urls to ignore. (Optional, defaults to          |
|                        | '([.\/]example\.com|\{|\$)'.)                               |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+
|                        |                                                             |
| ``network_timeout``    | A dict mapping URLs and timeout to be used for that URL.    |
|                        | All the URLs that have the same host as that of URLs        |
|                        | provided will be passed that timeout. It can also contain a |
|                        | wildcard timeout entry with key '*'. The timeout of all the |
|                        | websites not in the dict will be the value of the key '*'.  |
|                        | (Optional, defaults to '{}'.)                               |
|                        |                                                             |
+------------------------+-------------------------------------------------------------+


Dependencies
------------

* ``pip`` - ``requests``


Can Detect
----------

* Documentation

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
