#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.
    Args:
    set_1: A set.
    set_2: A set.
    Returns:
    A set containing the common elements in `set_1` and `set_2`.
    """
    common_set = set()
    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set
