class Admin_panel:
    def __init__(self):
        pass

    def admin_login(self,username,password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self,modulename,duration):
        topic_list = []
        topic_size = int(input("Enter number of topics: "))
        for i in range(topic_size):
            topic = input(f"Enter topic name: {i}")
            topic_list.append(topic)



