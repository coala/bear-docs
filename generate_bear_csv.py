from itertools import chain

from bear_docs_utils import get_bears

if __name__ == '__main__':
    language_can_detect = {}
    language_can_fix = {}
    can_detects = set()
    can_fixes = set()
    for bear in get_bears():
        can_detects |= bear.can_detect
        can_fixes |= bear.CAN_FIX

        for language in sorted(bear.LANGUAGES):
            if language in language_can_detect:
                language_can_detect[language] |= set(bear.can_detect)
                language_can_fix[language] |= set(bear.CAN_FIX)
            else:
                language_can_detect[language] = set(bear.can_detect)
                language_can_fix[language] = set(bear.CAN_FIX)

    columns = [val for val in chain(sorted(can_detects),
                                    sorted("FIX "+fix for fix in can_fixes))]
    file = ["Languages," + ','.join(columns) + '\n']
    for language in sorted(language_can_detect):
        detects = ','.join('1' if val in language_can_detect[language] else '0'
                           for val in sorted(can_detects))
        fixes = ','.join('1' if val in language_can_fix[language] else '0'
                         for val in sorted(can_fixes))
        file.append(language + ',' + detects + ',' + fixes + '\n')
    with open("language_support.csv", "w") as filehandle:
        filehandle.writelines(file)

    mapping = {'Code Duplication': 'Redundancy',
               'Commented Code': 'Redundancy',
               'Complexity': 'Complexity',
               'Documentation': 'Formatting',
               'Duplication': 'Redundancy',
               'Formatting': 'Formatting',
               'Grammar': 'Semantic',
               'Missing import': 'Redundancy',
               'Security': 'Semantic',
               'Simplification': 'Complexity',
               'Smell': 'Semantic',
               'Spelling': 'Syntax',
               'Syntax': 'Syntax',
               'Undefined Element': 'Semantic',
               'Unreachable Code': 'Redundancy',
               'Unused Code': 'Redundancy',
               'Unused code': 'Redundancy',
               'Variable Misuse': 'Semantic'}
    categories = list(sorted({val for val in mapping.values()}))
    shortfile = ['Languages,' + ','.join(categories) + '\n']
    for language in sorted(language_can_detect):
        def ret_number(cat):
            if any(cat == mapping[original_cat]
                   for original_cat in language_can_detect[language]):
                if any(cat == mapping[original_cat]
                       for original_cat in language_can_fix[language]):
                    return "2"

                return "1"

            return "0"

        detects = ','.join(ret_number(cat) for cat in categories)
        shortfile.append(language + ',' + detects + '\n')

    with open("simplified_language_support.csv", "w") as filehandle:
        filehandle.writelines(shortfile)
