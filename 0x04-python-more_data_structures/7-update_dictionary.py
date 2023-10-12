def update_dictionary(a_dictionary, key, value):
    """Replaces or adds a key/value pair in a dictionary.
    Args:
    a_dictionary: A dictionary.
    key: A string key.
    value: Any value.
    """

    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
