# class person:
#     name = "Akshay"
#     Age = 23
#     Occupation = "Employed"
#     networth = 100
#     def info(self):
#         print(f"{self.name} is {self.Occupation}")

# # The self parameter is a reference to the curent instance of the class, and is used to access variables that belongs to the class.
# # It must be provided as the extra parameter inside the method definition.

# a = person()
# # a.name = person.name
# # a.Occupation = person.Occupation
# a.name = "Deepak"
# a.Occupation = "Engineer"

# a.info()



# class student:
#     def __init__(self,name,roll_no,marks,study):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#         self.study = study

#     def student_info(self):
#         print("Name of the student: " ,self.name)
#         print("Student roll number is: " ,self.roll_no)
#         print("Students marks : " ,self.marks)
#         print("class of the student: " ,self.study)

# x = student("Akshay",20,600,16)
# x.student_info()
# x = student("Naveena",22,300,15)
# x.student_info()
# x = student("Deepak",24,500,13)
# x.student_info()



# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#         print("student name: ", self.name)
#         print("rollno: ", self.rollno)
#         print("marks: ", self.marks)
    
# x = Student("Akshay",20,300)
# y = Student("Deepak",22,200)
# z = Student("Akshay",21,100)



# class mobile:
#     def __init__(self,brand,color,ram,rom):
#         self.w = brand
#         self.x = color
#         self.y = ram
#         self.z = rom

#     def view_mobile(self):
#         print("mobile brand is: ", self.w)
#         print("mobile color is: ", self.x)
#         print("mobile ram is: ", self.y)
#         print("mobile rom is: ", self.z)


# x = mobile("onePlus","Olive Green",12,256)
# x.view_mobile()
# print("----------------------------------")
# y = mobile("iphone","Green","12 GB","256 GB")
# y.view_mobile()
# print("----------------------------------")
# z = mobile("Vivo","Black","8 GB","128 GB")
# z.view_mobile()



class Animal: 
 def __init__(self,name,rollno):
   self.name = name
   self.rollno = rollno
   print("Constuctor is executed")
   
 def f1(self):
   
   print(self.name,self.rollno)
   print("f1-Method Exceuted")

x=Animal("akshay","12")
x.f1()
y=Animal("akshay","12")
y.f1()
z=Animal("akshay","12")
z.f1()