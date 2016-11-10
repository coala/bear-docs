import os
import inspect

from bear_docs_utils import get_bears

def language_generate():
    lang_dict = {}
    for bear in get_bears():
        for language in bear.LANGUAGES:
            if language in lang_dict:
                lang_dict[language].append(bear.name)
            else:
                lang_dict[language] = [bear.name]

    with open("README.rst", "w") as lang_file:
        lang_file.write("**Note**: The ``master`` branch contains docs for the latest "
                        "stable version. If you want to view the docs for the "
                        "latest development version, see the ``pre`` branch.\n\n")
        lang_file.write("**Supported Languages ({})**\n-----------------------\n\n"
                        ".. contents::\n"
                        "    :local:\n"
                        "    :depth: 1\n"
                        "    :backlinks: none\n\n".format(len(lang_dict)))
        for language in sorted(lang_dict):
            lang_file.write(language + "\n" + "=" * len(language) + "\n")
            for bear in sorted(lang_dict[language]):
                lang_file.write("* `" + bear + " <docs/" + bear + ".rst>`_\n")
            lang_file.write("\n")
