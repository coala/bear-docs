**WriteGoodLintBear**
=====================

Lints the text files using ``write-good`` for improving proses.

See <https://github.com/btford/write-good> for more information.

`Supported Languages <../README.rst>`_
-----

* Natural Language

Settings
--------

+---------------------------+------------------------------------------------------------+
| Setting                   |  Meaning                                                   |
+===========================+============================================================+
|                           |                                                            |
| ``check_adverbs``         | Checks for adverbs that can weaken the meaning, such as:   |
|                           | ``really``, ``very``, ``extremely``, etc. (Optional,       |
|                           | defaults to 'False'.)                                      |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_ambiguos_words``  | Checks for ``weasel words`` for example ``often``,         |
|                           | ``probably`` (Optional, defaults to 'False'.)              |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_cliche_exists``   | Checks for common cliche phrases in the sentence.          |
|                           | (Optional, defaults to 'False'.)                           |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_extra_words``     | Checks for wordy phrases and unnecessary words. (Optional, |
|                           | defaults to 'False'.)                                      |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_passive_voice``   | Checks for passive voice. (Optional, defaults to 'False'.) +
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_repeated_words``  | Checks for lexical illusions – cases where a word is       |
|                           | repeated. (Optional, defaults to 'False'.)                 |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_so_beginning``    | Checks for ``So`` at the beginning of the sentence.        |
|                           | (Optional, defaults to 'False'.)                           |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+
|                           |                                                            |
| ``check_there_is``        | Checks for ``There is`` or ``There are`` at the beginning  |
|                           | of the sentence. (Optional, defaults to 'False'.)          |
|                           |                                                            |
+---------------------------+------------------------------------------------------------+


Can Detect
----------

* Formatting
* Grammar

License
-------

AGPL-3.0

Authors
-------

* The coala developers (coala-devel@googlegroups.com)
