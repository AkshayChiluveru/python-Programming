def find_pairs(array, target_sum):
    pairs = []
    complements = set()

    for num in array:
        complement = target_sum - num
        if complement in complements:
            pairs.append((num, complement))
        complements.add(num)

    return pairs

array = input("Enter the array of integers: ").split()
array = [int(num) for num in array]

target = int(input("Enter the target sum: "))

result = find_pairs(array, target)
print(f"Pairs with sum {target}:")
for pair in result:
    print(pair)
