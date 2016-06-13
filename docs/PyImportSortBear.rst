**PyImportSortBear**
====================

Raise issues related to sorting imports, segregating imports into various sections, and also adding comments on top of each import section based on the configurations provided.
You can read more about ``isort`` at <https://isort.readthedocs.org/en/latest/>.

Supported Languages:
-----

* Python
* Python 3
* Python 2

Settings
--------

+----------------------------------------+---------------------------------------------------------------------+
| Setting                                |  Meaning                                                            |
+========================================+=====================================================================+
|                                        |                                                                     |
| ``import_heading_localfolder``         | A comment to consistently place directly above imports that         |
|                                        | start with '.'.                                                     |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``known_third_party_imports``          | A list of imports that will be forced to display within the         |
|                                        | third party category of imports.                                    |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``balanced_wrapping_in_imports``       | If set to true - for each multi-line import statement isort will    |
|                                        | dynamically change the import length to the one that produces       |
|                                        | the most balanced grid, while staying below the maximum import      |
|                                        | length defined.                                                     |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``tab_width``                          | Number of spaces per indent level.                                  +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``force_sort_within_import_sections``  | If set, imports will be sorted within there section independent     |
|                                        | to the import_type.                                                 |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``lines_after_imports``                | Forces a certain number of lines after the imports and before the   |
|                                        | first line of functional code. By default this is set to -1 which   |
|                                        | uses 2 lines if the first line of code is a class or function and   |
|                                        | 1 line if it's anything else.                                       |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``from_first_in_import``               | If set, imports using "from" will be displayed above normal         |
|                                        | (straight) imports.                                                 |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``imports_forced_to_top``              | Forces a list of imports to the top of their respective section.    |
|                                        | This works well for handling the unfortunate cases of import        |
|                                        | dependencies that occur in many projects.                           |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``known_first_party_imports``          | A list of imports that will be forced to display within the         |
|                                        | standard library category of imports.                               |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``import_wrap_length``                 | An integer that represents the longest line-length you want when    |
|                                        | wrapping. If not set will default to line_length.                   |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``known_standard_library_imports``     | A list of imports that will be forced to display within the         |
|                                        | first party category of imports.                                    |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``forced_separate_imports``            | A list of modules that you want to appear in their own separate     |
|                                        | section.                                                            |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``use_parentheses_in_import``          | True if parenthesis are to be used in import statements.            +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``combine_star_imports``               | If set to true - ensures that if a star import is present,          |
|                                        | nothing else is imported from that namespace.                       |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``force_grid_wrap_imports``            | Force "from" imports to be grid wrapped regardless of line length.  +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``combine_as_imports``                 | If set to true - isort will combine as imports on the same line     |
|                                        | within for import statements.                                       |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``import_heading_stdlib``              | A comment to consistently place directly above imports from         |
|                                        | the standard library.                                               |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``import_heading_firstparty``          | A comment to consistently place directly above imports from         |
|                                        | the current project.                                                |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``include_trailing_comma_in_import``   | If set, will automatically add a trailing comma to the end of       |
|                                        | "from" imports. Example: ``from abc import (a, b, c,)``             |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``use_spaces``                         | True if spaces are to be used instead of tabs.                      +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``import_heading_future``              | A comment to consistently place directly above future imports.      +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``order_imports_by_type``              | If set to true - isort will create separate sections within "from"  |
|                                        | imports for CONSTANTS, Classes, and modules/functions.              |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``force_single_line_imports``          | If set to true - instead of wrapping multi-line from style imports, |
|                                        | each import will be forced to display on its own line.              |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``sort_imports_by_length``             | Set to true to sort imports by length instead of alphabetically.    +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``import_heading_thirdparty``          | A comment to consistently place directly above thirdparty imports.  +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``max_line_length``                    | Maximum number of characters for a lin                              +
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``force_alphabetical_sort_in_import``  | If set, forces all imports to be sorted as a single section,        |
|                                        | instead of within other groups (such as straight vs from).          |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``default_import_section``             | The default section to place imports in, if their section can       |
|                                        | not be automatically determined.                                    |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+
|                                        |                                                                     |
| ``isort_multi_line_output``            | An integer that represents how you want imports to be displayed     |
|                                        | by ``isort`` if they're long enough to span multiple lines.         |
|                                        | This value is passed to isort as the ``multi_line_output`` setting. |
|                                        | Possible values are (0-grid, 1-vertical, 2-hanging, 3-vert-hanging, |
|                                        | 4-vert-grid, 5-vert-grid-grouped)                                   |
|                                        | A full definition of all possible modes can be found at             |
|                                        | <https://github.com/timothycrosley/isort#multi-line-output-modes>.  |
|                                        |                                                                     |
+----------------------------------------+---------------------------------------------------------------------+

\* denotes required param