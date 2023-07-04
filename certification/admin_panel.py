import json
import random

class Admin_panel:
    def __init__(self):
        self.moduledetails = {}
        self.trainer_details = {}

    def admin_login(self,username,password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self,modulename,duration):
        topic_list = []
        key = random.randint(1,100)
        topic_size = int(input("Enter number of topics: "))
        for i in range(topic_size):
            topic = input(f"Enter topic name {i}: ")
            topic_list.append(topic)
        moduledata = {
            "Module_Name" : modulename,
            "Duration" : duration,                "Topic_Name" : topic_list
            }
        self.moduledetails[key] = moduledata
        with open("certification/add_module.json", "w") as f:
            json.dump(self.moduledetails, f,indent = 2)
        return self.moduledetails

# d = Admin_panel()
# d.add_module("python", "8 weeks")
# d.add_module("mySQL", "4 weeks")

    def addTrainer(self):
        trainer_id = random.randint(1,100)
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
    

d = Admin_panel()
d.add_module("python", "8 weeks")
d.add_module("mySQL", "4 weeks")
d.addTrainer()