import sys
import os
import inspect

from bear_docs_utils import get_bears
from language_generate import language_generate

if __name__ == "__main__":
    bears = get_bears()
    for bear in bears:
        output = "**" + bear.name + "**\n"
        output += "=" * (4 + len(bear.name)) + "\n\n"
        output += bear.get_metadata().desc + "\n\n"
        output += "`Supported Languages <../README.rst>`_" + "\n-----\n\n"
        output += "\n".join(["* " + x for x in sorted(bear.LANGUAGES)])
        output += "\n\n"
        docstring = inspect.getdoc(bear.run)
        if docstring:
            docstring = docstring[docstring.find(":param"):]
            if docstring.find("\n\n") != -1:
                docstring = docstring[:docstring.find("\n\n")]
            if docstring.find(":return") != -1:
                docstring = docstring[:docstring.find(":return")]
        if docstring:
            par = {}
            lmax = -1
            rmax = -1
            first = True
            for param in docstring.split(":param"):
                if first:
                    first = False
                    continue
                res = param.split(":")
                if len(res) > 2:
                    res = res[0], ":".join(res[1:])
                elif len(res) < 2:
                    continue
                key, meaning = res
                bold = "\\*" if key.strip() in bear.get_metadata().non_optional_params else ""
                key = " ``" + key.strip() + "``" + bold + " "
                meaning = meaning.strip()
                if lmax < len(key):
                    lmax = len(key)
                par[key] = []
                for line in meaning.split("\n"):
                    par[key].append(line.strip())
                    if len(line.strip()) > rmax:
                        rmax = len(line.strip())
            lmax = max(lmax, len(" Setting"))
            rmax = max(rmax, len("Meaning"))
            header = False
            for key in sorted(par):
                if not header:
                    output += "Settings\n--------\n\n"
                    output += "+" + "-" * (lmax) + "-+-" + "-" * (1 + rmax) + "+\n"
                    output += "| Setting" + " " * (lmax - len(" Setting")) + " |  Meaning" + " " * (rmax - len("Meaning")) + "|\n"
                    output += "+" + "=" * lmax + "=+=" + "=" * (1 + rmax) + "+\n"
                    header = True
                output += "| " + " " * lmax + "| " + " " * (1 + rmax) + "|\n"
                output += "|" + key + " " + " " * (lmax - len(key)) + "| " + par[key][0] + " " * (1 + rmax - len(par[key][0]))
                if len(par[key]) > 1:
                    output += "|\n"
                else:
                    output += "+\n"
                for text in par[key][1:]:
                    output += "|" + " " * (lmax + 1) + "| " + text + " " * (1 + rmax - len(text)) + "|\n"
                output += "| " + " " * lmax + "| " + " " * (1 + rmax) + "|\n"
                output += "+" + "-" * lmax + "-+-" + "-" * (1 + rmax) + "+\n"
            output += "\n\* denotes required param"

        if len(bear.can_detect):
            output += "\n\nCan Detect\n----------\n\n"
            output += "\n".join(sorted(["* " + x for x in bear.can_detect]))

        if bear.LICENSE:
            output += "\n\nLicense\n-------\n\n"
            output += bear.LICENSE

        if len(bear.AUTHORS):
            output += "\n\nAuthors\n-------\n\n"
            for author, author_email in zip(bear.AUTHORS, bear.AUTHORS_EMAILS):
                output += "* " + author + " (" + author_email + ")\n"

        with open("docs/" + bear.name + ".rst", "w") as bear_file:
            bear_file.write(output)

    language_generate()

    if len(sys.argv) == 1:
        os.system("git add -A && git commit -m 'Docs Update' && git push")
