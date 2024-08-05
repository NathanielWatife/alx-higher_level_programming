def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    Args:
    set_1: A set.
    set_2: A set.
    Returns:
    A set containing all elements present in only one set.
    """
    return (set_1 ^ set_2)
