# In an array, Count Pairs with given sum

def count_pairs_with_sum(arr, target_sum):
    count = 0
    num_freq = {}
    
    for num in arr:
        complement = target_sum - num
        if complement in num_freq:
            count += num_freq[complement]
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    
    return count
