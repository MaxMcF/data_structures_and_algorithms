import math


def binary_search(array, value):
    """
    This runs the binary search function

    Parameters:
    array (list): This is an ordered list that is passed in
    value (int): This is a value that is being checked against the given list

    Returns:
    int: the index of the found number in the list, or -1 if the number was not found

    """
    mid = len(array) // 2
    for index in range(len(array)):
        if value == array[index]:
            return index
        elif value < array[index]:
            mid = mid//2
        else:
            mid = mid + (mid//2)
    return -1

