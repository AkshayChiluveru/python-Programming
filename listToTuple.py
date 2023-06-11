# How can I make a tuple out of a list?
# We can transform a list into a tuple using the Python tuple() method. Since a tuple is immutable, we can't update the list after it has been converted to a tuple.

# Code

month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'] 
print(type(month)) 
converting_list = tuple(month)  
print(converting_list)  
print(type(converting_list))  