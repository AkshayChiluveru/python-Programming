class demo():
    def __init__(self,a,b):
        self._a = a
        self._b = b

class demo2(demo):
    def output(self):
        # print(self._a)
        print(self._b)


d = demo2(3,4)
d.output()
