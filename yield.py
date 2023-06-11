# What does the Python keyword imply?
# In Python, we can use the <yield> keyword to convert any Python function into a Python generator. Yields function similarly to a conventional return keyword. However, it will always return a generator object. A function can also use the <yield> keyword multiple times.

# Code

def creating_gen(index):  
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
    yield months[index]  
    yield months[index+2]  
next_month = creating_gen(3)  
print(next(next_month), next(next_month))  