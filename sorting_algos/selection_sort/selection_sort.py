def selection_sort(input_list):
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

