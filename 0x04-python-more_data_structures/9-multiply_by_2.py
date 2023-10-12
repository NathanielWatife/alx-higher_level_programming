def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2.
    Args:
    a_dictionary: A dictionary.
     Returns:
    A new dictionary with all values multiplied by 2.
    """
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
