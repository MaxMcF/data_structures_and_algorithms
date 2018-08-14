import math

# This function takes in an array and a value, finds the middle index of the array, and inserts
# the value into that index. This is done without using built in methods.
def insert_shift_array(array, value):
    if len(array)%2 != 0:
        oddOrEven = 1
    else:
        oddOrEven = 0
    half_length = ((len(array))//2) + oddOrEven
    return array[:half_length] + [value] + array[half_length:]

