def add_module(modulename,duration):
        topic_list = []
        topic_size = int(input("Enter number of topics: "))
        for i in range(topic_size):
            topic = input(f"Enter topic name {i} : ")
            topic_list.append(topic)
            moduledata = {
                "Module_Name" : modulename,
                "Duration" : duration,
                "Topic_Name" : topic_list
            }
        