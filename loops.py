#loops
#for loop
#while loop
# for [variable_name] in [iterable datatype]:
# 	statements
# iterable datatypes: strings list tuple set

# l = [11,12,13,14,15]
# sum = 0
# for value in l:
# 	sum = sum + value
# print(sum)

#range(5) 0 1 2 3 4
#range(10,100) 10,11,12,13,14,......,99
#range(10,100,5) 10,15,20,25,30, ....,95
# sum = 0
# for value in range(1,6):
# 	sum = sum + value
# print(sum)


# continue break enumerate 

# for value in range(1,11):
# 	print(value)

l = [10,20,30,40,50,60]
key = 50

for index,value in enumerate(l):
	if value == key:
		print("element found at index:" ,index)
		break
	else:
	    continue
else:
    print("element not found")	


