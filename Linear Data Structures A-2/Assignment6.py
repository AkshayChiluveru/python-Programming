# Find the Kth largest and Kth smallest number in an array

def find_kth_largest_smallest(arr, k):
    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k-1]
    
    return kth_largest, kth_smallest
