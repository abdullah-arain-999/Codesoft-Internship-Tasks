print()
print(('---------------------------------------'))
print(('           TO-DO-LIST-MANAGER          '))
print(('---------------------------------------'))

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = 'Done' if self.completed else 'Not Done'
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            print(f"Task {index} updated.")
        else:
            print("Task index out of range.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Task index out of range.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].description}' marked as complete.")
        else:
            print("Task index out of range.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Complete Task")
        print("5. List Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task index to update: "))
            description = input("Enter new task description: ")
            todo_list.update_task(index, description)
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            index = int(input("Enter task index to complete: "))
            todo_list.complete_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
