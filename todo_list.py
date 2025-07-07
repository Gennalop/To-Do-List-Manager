class Task:
    def __init__(self, description, priority, due_date, status="pending"):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Description: {self.description}, Priority: {self.priority}, Due Date: {self.due_date}, Status: {self.status}"

def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    new_task = Task(description, priority, due_date)
    tasks.append(new_task)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def mark_completed(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        task_index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index].status = "completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def clean_tasks(tasks):
    list_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            task_num += 1
            print(f"Task '{task_num}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def clean_completed_tasks(tasks):
    initial_count = len(tasks)
    tasks[:] = [task for task in tasks if task.status == "pending"]
    if len(tasks) < initial_count:
        print("Completed tasks cleaned from the list.")
    else:
        print("No completed tasks to clean.") 

def clean_list(tasks):
    num = len(tasks)
    if num == 0:
        print("No tasks in the list.")
    else: 
        tasks.clear()
        print(f"{num} tasks deleted.")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Delete Completed Tasks")
        print("6. Delete All Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            clean_tasks(tasks)
        elif choice == "5":
            clean_completed_tasks(tasks)
        elif choice == "6":
            clean_list(tasks)
        elif choice == "7":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()