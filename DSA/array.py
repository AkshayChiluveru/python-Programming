class Array:
    def __init__(self):
        self.array = []

    def insertion_at_beg(self,data):
        self.array.insert(0,data)
        return self.array
        
    def insertion_at_end(self,data):
        self.array.append(data)
        return self.array
    def insertion_at_pos(self,data,pos):
        if pos> len(self.array):
            return self.array 
        self.array.insert(pos,data)
        return self.array
    
    def deletion_at_begin(self): #[]
        if len(self.array)<1:
            return self.array
 
        self.array.pop(0)
        return self.array
 
    def deletion_at_end(self):
        if len(self.array)<1:
            return self.array
        self.array.pop()
        return self.array
 
    def deletion_at_pos(self,pos):
        if len(self.array)<1 or pos>len(self.array):
            return self.array
        self.array.pop(pos)
        return self.array
 
    def traversal(self):
        for i in self.array:
            print(i)    
            

s=Array()
s.insertion_at_beg(10)
s.traversal()
print("*****************************************************************")
s.insertion_at_beg(20)
s.traversal()
print("*****************************************************************")
s.insertion_at_beg(30)
s.traversal()
print("*****************************************************************")
s.insertion_at_pos(50,0)
s.traversal()
print("*****************************************************************")
s.insertion_at_pos(50,4)
s.traversal()
print("*****************************************************************")
s.insertion_at_end(100)
s.traversal()
print("*****************************************************************")
s.deletion_at_begin()
s.traversal()
print("*****************************************************************")
s.deletion_at_end()
s.traversal()
print("*****************************************************************")
s.deletion_at_pos(2)
s.traversal()
