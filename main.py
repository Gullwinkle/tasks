class Task:
    def __init__(self, description, date, is_done=False):
        self.description = description
        self.date = date
        self.is_done = is_done

class Tasks(list):
    def __init__(self):
        super().__init__()

    def add_task(self, task):
        self.append(task)

    def task_done(self, task):
        self[self.index(task)].is_done = True

    def show_tasks(self):
        for task in self:
            if not task.is_done:
                print(task.description)

tasks = Tasks()
task1 = Task('Написать код', '08.01.2025')
task2 = Task('Сделать коммит', '08.01.2025')
task3 = Task('Push to github', '08.01.2025')
tasks.add_task(task1)
tasks.add_task(task2)
tasks.add_task(task3)
tasks.show_tasks()
tasks.task_done(task1)
tasks.task_done(task2)
tasks.show_tasks()