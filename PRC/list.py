class CheckList:
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self, task_name, task_description="NO DISCRIPTION PROVIDED"):
        self.task_name = task_name
        self.task_description = task_description
        self.tasks.update({self.task_name:self.task_description})

    def show_list(self):
        keys = self.tasks.keys()
        for i in keys:
            print("{} : {}".format(i, self.tasks.get(i)))    
        #stripped_values = self.tasks.get(stripped_keys)

