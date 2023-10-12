def multiply_list_map(my_list=[], number=0):
    """Returns a list with all values multiplied by a number without using any loops.
    Args:
    my_list: A list.
    number: A number.
    Returns:
    A new list with all values multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))
