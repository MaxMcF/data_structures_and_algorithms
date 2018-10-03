def quick_sort(input_list):
    if len(input_list) < 2:
        return input_list
    pivot = len(input_list) - 1
    wall = 0
    current = 0
    while current < pivot:
        while input_list[pivot] > input_list[wall]:
            wall += 1
            current += 1
        if input_list[current] < input_list[pivot]:
            input_list[current], input_list[wall] = input_list[wall], input_list[current]
            wall += 1
        current += 1
    import pdb; pdb.set_trace()
    input_list[pivot], input_list[wall] = input_list[wall], input_list[pivot]
    left = quick_sort(input_list[0:wall])
    right = quick_sort(input_list[wall+1:pivot])
    return left + right


result = quick_sort([32,123,43,3,2,5,7,8,9,0,4355,65,1231,98,900,2123,432,4554554])
