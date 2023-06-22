class person:
    name = "Akshay"
    Age = 23
    Occupation = "Employed"
    networth = 100
    def info(self):
        print(f"{self.name} is {self.Occupation}")

# The self parameter is a reference to the curent instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

a = person()
a.name = "Deepak"
a.Occupation = "Engineer"

a.info()
