import json

# File to store tasks
task_file = "database.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the tasks file. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")

def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            print("1. Mark as Completed\n2. Edit Task Details")
            choice = int(input("Choose an option: "))
            if choice == 1:
                task["status"] = "Completed"
            elif choice == 2:
                task["title"] = input("Enter new title: ")
                task["description"] = input("Enter new description: ")
                task["due_date"] = input("Enter new due date: ")
                task["priority"] = input("Enter new priority: ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) != len(tasks):
        save_tasks(updated_tasks)
        print("Task deleted successfully!")
        return updated_tasks
    print("Task not found.")
    return tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            tasks = delete_task(tasks)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
