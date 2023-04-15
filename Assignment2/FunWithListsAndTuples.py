def sort_tuple_list(tuple_list):
    n = len(tuple_list)
    i = 0
    while i < n-1:
        j = i+1
        while j < n:
            if tuple_list[i][-1] > tuple_list[j][-1]:
                tuple_list[i], tuple_list[j] = tuple_list[j], tuple_list[i]
            j += 1
        i += 1
    return tuple_list

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuple_list = sort_tuple_list(tuple_list)
print(sorted_tuple_list)
