#  A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors.
# Constructor is involved automatically when an object of a class is created.

# Syntax of a Python Constructor
# def __init__(self):
    #  initializations;
#  init is one of the reserved functions in python. In Object oriented programming it is known as a constructor. we can also create constructor by defining the function name with same class name.

class person:
    def __init__(self,name,occ): # constructor
        self.name = name 
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Akshay", "developer")
b = person("Deepak", "Block chain developer")
a.info()
b.info()