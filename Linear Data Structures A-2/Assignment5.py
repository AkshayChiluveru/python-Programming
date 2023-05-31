# Find duplicates in an array

def find_duplicates(arr):
    duplicates = set()
    seen = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
