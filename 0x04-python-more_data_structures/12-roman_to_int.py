#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.
    Args:
    roman_string: A string containing a Roman numeral.
    Returns:
    An integer representing the Roman numeral.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    previous_value = None
    for character in roman_string[::-1]:
        current_value = roman_map[character]
    if previous_value is None or current_value >= previous_value:
        result += current_value
    else:
        result -= current_value
        previous_value = current_value
    return result
