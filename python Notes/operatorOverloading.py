#Demo program to use + operator for a class object
# class Book:
# class Book:
#    def __init__(self,pages):
#     self.pages=pages
#     print("Constructor loaded")
 
#     def __add__(self,x):
#         return self.pages+x.pages
# B1=Book(500)
# B2=Book(1000)
# print(B1)
# print(B2)
# print(B1+B2)


#Demo program to use - operator for a class object
class Book:
   def __init__(self,pages):
    self.pages=pages
    print("Constructor called")
    
    def __sub__(self,x):
        print("Magic method called")
        return self.pages-x.pages
 
b1=Book(2000)
b2=Book(200)
print(b1 - b2)