class Animal:
    legs=4
    @classmethod
    
    def walk(cls,name):
        print(str(name)+" having "+str(Animal.legs)+" legs")
Animal.walk("lion")
dir(Animal)