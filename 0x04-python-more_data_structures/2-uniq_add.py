#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.
    Args:
    my_list: A list of integers.
    Returns:
    The sum of all unique integers in the list. 
    """
    unique_set = set()
    for element in my_list:
        unique_set.add(element)
    sum = 0
    for element in unique_set:
        sum += element
    return sum
