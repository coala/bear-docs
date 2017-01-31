`GitCommitBear <https://github.com/coala-analyzer/coala-bears/tree/master/bears/vcs/git/GitCommitBear.py>`_
===========================================================================================================

Check for matching issue related references and URLs.

`Supported Languages <../README.rst>`_
--------------------------------------

* Git

Settings
--------

+------------------------------------+---------------------------------------------------------------------------------------+
| Setting                            |  Meaning                                                                              |
+====================================+=======================================================================================+
|                                    |                                                                                       |
| ``allow_empty_commit_message``     | Whether empty commit messages are allowed or not.                                     |
|                                    | (Optional, defaults to 'False'.)                                                      |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_close_issue_full_url``      | Checks the presence of issue close reference with a full                              |
|                                    | URL related to some issue. Works along with                                           |
|                                    | ``body_close_issue``. (Optional, defaults to 'False'.)                                |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_close_issue_on_last_line``  | When enabled, checks for issue close reference presence on                            |
|                                    | the last line of the commit body. Works along with                                    |
|                                    | ``body_close_issue``. (Optional, defaults to 'False'.)                                |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_close_issue``               | GitHub and GitLab support auto closing issues with commit                             |
|                                    | messages. When enabled, this checks for matching keywords                             |
|                                    | in the commit body by retrieving host information from git                            |
|                                    | configuration. By default, if none of                                                 |
|                                    | ``body_close_issue_full_url`` and                                                     |
|                                    | ``body_close_issue_on_last_line`` are enabled, this checks                            |
|                                    | for presence of short references like ``closes #213``.                                |
|                                    | Otherwise behaves according to other chosen flags. More on                            |
|                                    | keywords follows.                                                                     |
|                                    | [GitHub](https://help.github.com/articles/closing-issues-via-commit-messages/)        |
|                                    | [GitLab](https://docs.gitlab.com/ce/user/project/issues/automatic_issue_closing.html) |
|                                    | (Optional, defaults to 'False'.)                                                      |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_enforce_issue_reference``   | Whether to enforce presence of issue reference in the body                            |
|                                    | of commit message. (Optional, defaults to 'False'.)                                   |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_line_length``               | The maximum line-length of the body. The newline character                            |
|                                    | at each line end does not count to the length. (Optional,                             |
|                                    | defaults to '72'.)                                                                    |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``body_regex``                     | If provided, checks the presence of regex in the commit                               |
|                                    | body. (Optional, defaults to 'None'.)                                                 |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``force_body``                     | Whether a body shall exist or not. (Optional, defaults to                             |
|                                    | 'False'.)                                                                             |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``ignore_length_regex``            | Lines matching each of the regular expressions in this list                           |
|                                    | will be ignored. (Optional, defaults to '()'.)                                        |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``shortlog_imperative_check``      | No description given. (Optional, defaults to 'True'.)                                 +
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``shortlog_length``                | The maximum length of the shortlog. The newline character                             |
|                                    | at end does not count to the length. (Optional, defaults to                           |
|                                    | '50'.)                                                                                |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``shortlog_regex``                 | No description given. (Optional, defaults to ''.)                                     +
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``shortlog_trailing_period``       | Whether a dot shall be enforced at end end or not (or                                 |
|                                    | ``None`` for "don't care"). (Optional, defaults to 'None'.)                           |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+
|                                    |                                                                                       |
| ``shortlog_wip_check``             | Whether a "WIP" in the shortlog text should yield a result                            |
|                                    | or not. (Optional, defaults to 'True'.)                                               |
|                                    |                                                                                       |
+------------------------------------+---------------------------------------------------------------------------------------+


Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/e146c9739ojhr8396wedsvf0d.png
   :target: https://asciinema.org/a/e146c9739ojhr8396wedsvf0d?autoplay=1
   :width: 100%

Dependencies
------------

* ``pip`` - ``nltk``


Can Detect
----------

* Formatting

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
