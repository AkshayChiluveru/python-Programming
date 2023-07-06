import json
import random

class Admin_panel:
    Student_list = []
    def __init__(self):
        self.moduledetails = {}
        self.trainer_details = {}
        self.batch_details = {}
        self.student_details = {}

    def admin_login(self,username,password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self,modulename,duration):
        topic_list = []
        key = random.randint(1,100)
        topic_size = int(input("Enter number of topics that you want to add: "))
        for i in range(topic_size+1):
            topic = input(f"Enter topic name {i}: ")
            topic_list.append(topic)
        moduledata = {
            "Module_Name" : modulename,
            "Duration" : duration,                
            "Topic_Name" : topic_list
            }
        self.moduledetails[key] = moduledata
        with open("certification/add_module.json", "w") as f:
            json.dump(self.moduledetails, f,indent =2)
        return self.moduledetails

# d = Admin_panel()
# d.add_module("python", "8 weeks")
# d.add_module("mySQL", "4 weeks")

    def addTrainer(self):
        trainer_id = random.randint(1,100)
        student_size = int(input("Enter the number of students you want to add: "))
        for i in range(1,student_size+1):
            print(f"Enter the details of the student {i}: ")
            name = input("enter the name: ")
            gender = input("Enter the gender: ")
            mobile = int(input("Enter the mobile: "))
            experience = input("enter the Experience: ")
            qualification = input("Enter the Qualification: ")
            email_id = input("Enter the email id: ")
            password = input("Enter the pass word")
            trainer_data = {
                "trainer_id": trainer_id,
                "name" : name,
                "gender": gender,
                "mobile": mobile,
                "experience": experience,
                "qualification": qualification,
                "email_id": email_id,
                "password": password
            }
        self.trainer_details[trainer_id] = trainer_data
        with open("certification/add_trainer.json", "w") as f:
            json.dump(self.trainer_details, f,indent = 2)
        return self.trainer_details
    

# d = Admin_panel()
# d.add_module("python", "8 weeks")
# d.add_module("mySQL", "4 weeks")
# d.addTrainer()


    def add_batch(self,module,trainer,student):
        key = random.randint(1,100)
        batch_data = {
            "module" : module,
            "trainer" : trainer,
            "student" : student
        }
        self.batch_details[key] = batch_data
        with open("certification/add_batch.json", "w") as f:
            json.dump(self.batch_details, f,indent = 2)
        return self.batch_details
    

# d = Admin_panel()
# d.add_module("python", "8 weeks")
# d.add_module("mySQL", "4 weeks")
# d.addTrainer()
# d.add_batch("DSA","Akshay","Student")


    def add_student(self):
        key = random.randint(1,100)
        student_size = int(input("Enter the number of students you want to add: "))
        for i in range(1,student_size+1):
            print(f"Enter the details of the student {i}: ")
            name = input("Enter the name of the student: ")
            gender = input("Enter the gender of the student: ")
            mobile = input("Enter the mobile number: ")
            qualification = input("Enter the Qualification: ")
            email_id = input("Enter the email id: ")
            password = input("Enter the password: ")
            student_data = {
                "name" : name,
                "gender": gender,
                "mobile": mobile,
                "qualification": qualification,
                "email_id": email_id,
                "password": password
            }

            Admin_panel.Student_list.append(student_data) 
        self.student_details[key] = Admin_panel.Student_list
        with open("certification/add_student.json", "w") as f:
            json.dump(self.student_details,f,indent = 2)
            
        return self.student_details


    def remove_module(self):
        with open("certification/add_module.json", "r") as f:
            content1 = json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f"module_id :{k} data :{v}")
        module_key = input("Enter the id to remove from the module: ")
        del content1[module_key]
        print("module is successfully deleted:")
        print(content1)
        with open("certification/add_module.json", "w") as f:
            json.dump(content1, f,indent = 2)


    def update_module(self):
        with open("certification/add_trainer.json", "r") as f:
            content1 = json.load(f)
        for  k,v in content1.items():
            print(f"trainer_id :{k} data :{v}")
        trainer_id = input("Enter the trainer id that you want to update: ")
        trainer_edit = input("Enter which field you want to update: ")
        trainer_update_value =  input("Enter the updated value: ")
        content1[trainer_id][trainer_edit] = trainer_update_value 
        for  k,v in content1.items():
            print(f"trainer_id :{k} data :{v}")
        with open("certification/add_trainer.json", "w") as f:
            json.dump(content1, f,indent=2)


    def read_student(self):
        with open("certification/add_student.json", "r") as f:
            content = json.load(f)
        
        for k,v in content.items():
            print(f"Student_id :{k} student Data :{v}")
            print("\n")
        return content
    
    def read_trainer(self):
        with open("certification/add_trainer.json", "r") as f:
            content = json.load(f)
        
        for k,v in content.items():
            print(f"trainer_id :{k} Trainer Data :{v}")
            print("\n")
        return content
    
    def read_batch(self):
        with open("certification/add_batch.json", "r") as f:
            content = json.load(f)
        
        for k,v in content.items():
            print(f"batch_id :{k} Batch Data :{v}")
            print("\n")
        return content


    def read_module(self):
        with open("certification/add_module.json", "r") as f:
            content = json.load(f)
        
        for k,v in content.items():
            print(f"Module_id :{k} Module Data :{v}")
            print("\n")
        return content


d = Admin_panel()
# d.read_batch()
# d.read_trainer()
# d.read_student()
# d.update_module()
# d.remove_module()

# print("First batch is: ",d.add_batch("python","deepak","akshay"))
# print("second batch is: ",d.add_batch("MySql","naveena", "naina"))
# print("-"*40)
# print("First batch is: ",d.add_module("python","8 weeks"))
# print("second batch is: ",d.add_module("mySql","4 weeks"))
# print("-"*40)
# print("first batch: ",d.add_student())
# print("second batch: ",d.add_student())
# print("-"*40)
# print(d.addTrainer())
# print(d.addTrainer())

