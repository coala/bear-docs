from bear_docs_utils import get_bears

if __name__ == '__main__':
    language_can_detect = {}
    language_can_fix = {}
    can_detects = set()
    for bear in get_bears():
        can_detects |= bear.can_detect

        for language in sorted(bear.LANGUAGES):
            if language in language_can_detect:
                language_can_detect[language] |= set(bear.can_detect)
                language_can_fix[language] |= set(bear.CAN_FIX)
            else:
                language_can_detect[language] = set(bear.can_detect)
                language_can_fix[language] = set(bear.CAN_FIX)

    columns = [val for val in sorted(can_detects)]
    file = ["Languages," + ','.join(columns) + '\n']
    for language in sorted(language_can_detect):
        def get_val(val):
            if val in language_can_fix[language]:
                return 'Can fix'

            if val in language_can_detect[language]:
                return 'Can detect'

            return "Unsupported"
        detects = ','.join(get_val(val)
                           for val in sorted(can_detects))
        file.append(language + ',' + detects + '\n')
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
                    return "Can fix"

                return "Can detect"

            return "Unsupported"

        detects = ','.join(ret_number(cat) for cat in categories)
        shortfile.append(language + ',' + detects + '\n')

    with open("simplified_language_support.csv", "w") as filehandle:
        filehandle.writelines(shortfile)
