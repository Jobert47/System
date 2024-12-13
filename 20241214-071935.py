import json

task_file = "database.json"

def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 
    except json.JSONDecodeError:
        print("Error reading the tasks file. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def is_valid_text(input_text):
    return input_text.replace(" ", "").isalpha() and len(input_text.strip()) > 0

def add_task(tasks):
    while True:
        title = input("Enter task title: ")
        if is_valid_text(title):
            break
        print("Title must contain only letters and spaces, and cannot be empty. Please try again.")

    description = input("Enter task description: ")

    while True:
        priority = input("Enter task priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Priority must be one of the following: High, Medium, or Low. Please try again.")

    while True:
        try:
            due_date = input("Enter due date (YYYY-MM-DD): ")
            year, month, day = map(int, due_date.split('-'))

            if (1900 <= year <= 3000) and (1 <= month <= 12) and (1 <= day <= 31): 
                break
            else:
                print("Invalid date. Please enter a date in the format YYYY-MM-DD.")
        except ValueError:
            print("Invalid input. Please enter only numbers.")

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
        print(f"\nID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}")

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
        print("..............")
        print("[1] Add Task\n[2] View Tasks\n[3] Update Task\n[4] Delete Task\n[5] Exit")
        print("..............")
        Select = int(input("Select an option: "))
        if Select == 1:
            add_task(tasks)
        elif Select == 2:
            view_tasks(tasks)
        elif Select == 3:
            update_task(tasks)
        elif Select == 4:
            tasks = delete_task(tasks)
        elif Select == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
    