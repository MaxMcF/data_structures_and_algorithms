def insertion_sort(input_list):
    '''This function takes in a string and sorts it using a insertion sort.

    ARGS:
        Input List
    OUTPUT:
        Sorted List
    '''
    if type(input_list) is not list:
        raise TypeError('Input must be a list')
    for i in range(1, len(input_list)):
        current = input_list[i]
        curr_index = i
        while current < input_list[curr_index-1] and curr_index > 0:
            input_list[curr_index], input_list[curr_index-1] = input_list[curr_index-1], input_list[curr_index]
            curr_index -= 1

    return input_list

