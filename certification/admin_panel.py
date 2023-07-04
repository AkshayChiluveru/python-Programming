import json
import random

class Admin_panel:
    def __init__(self):
        self.moduledetails = {}

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
            json.dump(self.moduledetails, f)
        return self.moduledetails

d = Admin_panel()
d.add_module("python", "8 weeks")
d.add_module("mySQL", "4 weeks")