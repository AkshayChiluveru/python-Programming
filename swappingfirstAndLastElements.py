myList = [12,14,51,63,74,34]

# Approach 1
length = len(myList)
temp = myList[0]
myList[0] = myList[length-1]
myList[length-1] = temp

# Approach 2
myList[0],myList[-1] = myList[-1],myList[0]

print(myList)