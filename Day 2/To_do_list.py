import json

def load_tasks(filename):
    """Load tasks from a file if it exists, otherwise return an empty list."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter the task name: ").strip()
    priority = input("Enter the priority (High, Medium, Low): ").strip().capitalize()

    if priority in ["High", "Medium", "Low"]:
        tasks.append({"name": task_name, "priority": priority})
        print(f"Task '{task_name}' added with priority '{priority}'.")
    else:
        print("Invalid priority. Please enter High, Medium, or Low.")

def show_tasks(tasks):
    """Display all tasks sorted by priority."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task['name']} - {task['priority']}")

def complete_task(tasks):
    """Remove a task by marking it as complete."""
    if not tasks:
        print("No tasks to complete.")
        return

    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            completed_task = tasks.pop(task_num - 1)
            print(f"Task '{completed_task['name']}' completed and removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_manager():
    """Main function to manage the To-Do List."""
    filename = "tasks.json"
    tasks = load_tasks(filename)
    print("Welcome to the To-Do List Manager!")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Save and Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks, filename)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the To-Do List Manager
to_do_list_manager()
