def radix_sort(num_list):
    def num_to_bucket(num_list, base, iteration):
        buckets = [[] for x in range(base)]
        for number in num_list:
            ind = number // (base ** iteration) % base
            buckets[ind].append(number)
        return buckets
    def bucket_to_nums(bucket_list):
        return_list = []
        for bucket in bucket_list:
            for num in bucket:
                return_list.append(num)
        return return_list

    base = 10
    max_val = max(num_list)
    iteration = 0
    while max_val >= (base ** iteration):
        num_list = bucket_to_nums(num_to_bucket(num_list, base, iteration))
        iteration += 1
    return num_list
