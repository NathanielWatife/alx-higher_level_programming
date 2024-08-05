#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key from a dictionary.
    Args:
    a_dictionary: A dictionary.
    key: A string key.
    """
    if key in a_dictionary:
        del a_dictionary[key]
