def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

input_arr = input("Enter the elements of the array: ").split()
array = [int(num) for num in input_arr]

reverse_array(array)

print("Reversed Array:", array)
