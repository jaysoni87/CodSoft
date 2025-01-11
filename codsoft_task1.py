import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully!')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
            return

        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated successfully!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted successfully!')
        else:
            print("Invalid task number!")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number!")


def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the updated task: ")
                to_do_list.update_task(task_number, new_task)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "4":
            to_do_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                to_do_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "5":
            to_do_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as complete: "))
                to_do_list.mark_complete(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "6":
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
