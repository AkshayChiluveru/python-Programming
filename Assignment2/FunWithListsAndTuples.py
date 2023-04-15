def sort_tuple_list(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuple_list = sort_tuple_list(tuple_list)
print(sorted_tuple_list)