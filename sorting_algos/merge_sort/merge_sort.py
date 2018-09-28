def merge_sort(input_list):
    '''This function takes in a string and sorts it using a merge sort.

    ARGS:
        Input List
    OUTPUT:
        Sorted List
    '''
    if type(input_list) is not list:
        raise TypeError('Input must be a list')
    if len(input_list) < 2:
        return input_list
    half = len(input_list)//2
    left = merge_sort(input_list[:half])
    right = merge_sort(input_list[half:])
    return merge(left, right)

def merge(array_1, array_2):
    merged = []
    counter_one, counter_two = 0, 0

    while counter_one < (len(array_1)) and counter_two < (len(array_2)):
        if array_1[counter_one] < array_2[counter_two]:
            merged.append(array_1[counter_one])
            counter_one += 1
        else:
            merged.append(array_2[counter_two])
            counter_two += 1

    if counter_one > (len(array_1) - 1):
        merged.extend(array_2[counter_two:])
        return merged
    else:
        merged.extend(array_1[counter_one:])
        return merged

