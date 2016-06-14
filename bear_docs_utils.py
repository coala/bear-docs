from coalib.settings.ConfigurationGathering import load_configuration
from coalib.misc.DictUtilities import inverse_dicts
from coalib.collecting.Collectors import (
    collect_all_bears_from_sections, filter_section_bears_by_languages)
from pyprint.NullPrinter import NullPrinter
from coalib.output.printers.LogPrinter import LogPrinter

def get_bears():
    """
    Get a dict of bears with the bear class as key.

    :return:
        A dict with bear classes as key and the list of sections
        as value.
    """
    log_printer = LogPrinter(NullPrinter())
    sections, _ = load_configuration(None, log_printer)
    local_bears, global_bears = collect_all_bears_from_sections(
        sections, log_printer)
    return inverse_dicts(local_bears, global_bears)
