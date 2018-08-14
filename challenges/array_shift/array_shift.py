import math

def insert_shift_array(array, value):
    if len(array)%2 != 0:
        oddOrEven = 1
    else:
        oddOrEven = 0
    half_length = ((len(array))//2) + oddOrEven
    return array[:half_length] + [value] + array[half_length:]

