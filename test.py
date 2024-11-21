"""
Task Manager Application

This script provides functionality to add, list, and complete tasks.
Users can interact with the application through a menu-based interface.
"""

from typing import List, Dict

tasks: List[Dict] = []

def add_task(title: str, priority: int) -> None:
    """Adds a task to the list."""
    task = {"title": title, "priority": priority, "completed": False}
    tasks.append(task)

def list_tasks() -> None:
    """Lists all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks):
        print(
            f"#{index+1} - Title: {task['title']}, "
            f"Priority: {task['priority']}, Completed: {task['completed']}"
        )

def complete_task(index: int) -> None:
    """Marks a task as completed."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task #{index+1} marked as complete.")
    else:
        print("Invalid task number.")

def main() -> None:
    """Main function to run the task manager."""
    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            title = input("Enter task title: ")
            try:
                priority = int(input("Enter task priority (1-5): "))
                if 1 <= priority <= 5:
                    add_task(title, priority)
                else:
                    print("Priority must be between 1 and 5.")
            except ValueError:
                print("Priority must be a number.")
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == 4:
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
