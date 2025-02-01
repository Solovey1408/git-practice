class ToDoList:


    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})
        print(f"Задача '{task}' добавлена.")


    def complete_task(self, task):

        for i in self.tasks:

            if i["task"] == task:
                i["complete"] = True
                print(f"Задача '{task}' выполнена")
                break
            else:
                print(f"Задача '{task}' не найдена")


    def remove_task(self, task):

        for i in self.tasks:

            if i["task"] == task:
                self.tasks.remove(i)
                print(f"Задача '{task}' удалена")
                break
            else:
                print(f"Задача '{task}' не найдена")


    def list_tasks(self):
         if not self.tasks:
             print("Задач нет.")
         else:
             print("Список задач:")
             for i in self.tasks:
                 sign = "✔" if i["complete"] else "❌"
                 print(f"{sign} {i}")


my_todo_list = ToDoList()


my_todo_list.add_task("Добавить")
my_todo_list.add_task("Выполнить")
my_todo_list.add_task("Удалить")
my_todo_list.list_tasks()
my_todo_list.complete_task("Добавить")
my_todo_list.list_tasks()
my_todo_list.remove_task("Добавить")
my_todo_list.list_tasks()