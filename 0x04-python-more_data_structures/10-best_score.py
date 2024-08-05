#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.
    Args:
    a_dictionary: A dictionary.
    Returns:
    A key with the biggest integer value, or None if the dictionary is empty.
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_key = None
    best_score = None
    for key in a_dictionary:
        score = a_dictionary[key]
    if best_score is None or score > best_score:
        best_key = key
        best_score = score
    return best_key
