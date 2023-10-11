def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element in a list with another element.
    Args:
    my_list: A list.
    search: The element to replace in the list.
    replace: The new element.
    Returns:
    A new list with all occurrences of `search` replaced with `replace`.
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
