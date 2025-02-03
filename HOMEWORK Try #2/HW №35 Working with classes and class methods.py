class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append({"name": name, "complete": False})
        print(f"Задача '{name}' добавлена.")

    def complete_task(self, name):

        if self.tasks:

            for i in self.tasks:

                if i["name"] == name:
                    i["complete"] = True
                    print(f"Задача '{name}' выполнена")
                    break

            else:
                print(f"Задача '{name}' не найдена")

        else:
            print("Задачи отсутствуют.")

    def remove_task(self, name):

        if self.tasks:

            for i in self.tasks:

                if i["name"] == name:
                    self.tasks.remove(i)
                    print(f"Задача '{name}' удалена")
                    break

            else:
                print(f"Задача '{name}' не найдена")

        else:
            print("Задачи отсутствуют.")

    def list_tasks(self):

        if not self.tasks:
            print("Задач нет.")

        else:
            print("Список задач:")

        for i in self.tasks:
            sign = "✔" if i["complete"] else "❌"
            print(f"{sign} {i["name"]}")


my_todo_list = ToDoList()

my_todo_list.add_task("Добавить")
my_todo_list.add_task("Выполнить")
my_todo_list.add_task("Удалить")
my_todo_list.list_tasks()
my_todo_list.complete_task("Добавить")
my_todo_list.complete_task("Выполнить")
my_todo_list.list_tasks()
my_todo_list.remove_task("Добавить")
my_todo_list.list_tasks()