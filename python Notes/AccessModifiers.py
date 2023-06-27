class modifier:
    x = 10
    __y = 20
    _z =30

    def m1(self):
        print(modifier.x)
        print(modifier.__y)
        print(modifier._z)

a = modifier()
# a.m1()
# a.x
a._z 
