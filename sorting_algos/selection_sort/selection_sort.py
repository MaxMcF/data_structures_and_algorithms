def selection_sort(input_list):
    '''This function takes in a string and sorts it using a selection sort.
    The list gets iterated through and finds the lowest value. This value gets put into
    the first index. The list is then iterated through again, finding the next lowest value,
    and that value gets put into the second index. This continues until the list is sorted.

    ARGS:
        Input List
    OUTPUT:
        Sorted List
    '''
    if type(input_list) is not list:
        raise TypeError('Input must be a list')
    for i in range(len(input_list)):
        lowest = input_list[i]
        index_low = i
        for k in range(i, len(input_list)):
            if input_list[k] < lowest:
                lowest = input_list[k]
                index_low = k
        temp = input_list[i]
        input_list[i] = lowest
        input_list[index_low] = temp
    return input_list

