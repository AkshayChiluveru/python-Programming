class linkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

a = linkedList(10)
b = linkedList(20)
c = linkedList(30)
d = linkedList(40)
e = linkedList(50)

print("step 1: creating a node")
print(a.data,a.next)
print(b.data,b.next)
print(c.data,c.next)
print(d.data,d.next)
print(e.data,e.next)
print("*"*100)
print("step 2: connections to nodes")
a.next = b
print(a.data,a.next)
print(b)
b.next = c
print(b.data,b.next)
print(c)
c.next = d
print(c.data,c.next)
print(d)
d.next = e
print(d.data,d.next)
print(e)
print(e.data,e.next)