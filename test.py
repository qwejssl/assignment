tasks = []

def add_task(title, priority):
    task = {"title": title, "priority": priority, "completed": False}
    tasks.append(task)

def list_tasks(): # Missing type hints
    for index, task in enumerate(tasks):
        print(f"#{index+1} - Title: " + task["title"], " Priority: " + str(task["priority"]), " Completed: " + str(task["completed"]))

def complete_task(index):
    tasks[index]["completed"] = True

def main():
    while True:
        print("Task Manager:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            priority = input("Enter task priority: ")
            add_task(title, priority)
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(index)
        else:
            print("Invalid choice.")
