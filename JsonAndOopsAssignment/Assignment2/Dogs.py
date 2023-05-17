class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}\nAge: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def specific_method1(self):
        print("This is a specific method for Jack Russell Terrier.")

    def specific_method2(self):
        print("This is another specific method for Jack Russell Terrier.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def specific_method1(self):
        print("This is a specific method for Bulldog.")

    def specific_method2(self):
        print("This is another specific method for Bulldog.")


dog = Dog("Max", 3, "Brown")
dog.description()
dog.get_info()

print()

jack_russell = JackRussellTerrier("Leo", 5, "White and Brown")
jack_russell.description()
jack_russell.get_info()
jack_russell.specific_method1()
jack_russell.specific_method2()

print()

bulldog = Bulldog("Shitzu", 4, "White")
bulldog.description()
bulldog.get_info()
bulldog.specific_method1()
bulldog.specific_method2()
