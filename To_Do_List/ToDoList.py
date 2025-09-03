import json
import os
from datetime import datetime

FILENAME = "tasks.json"
todo_list = []

# Load Task in tasks.json
def load_task():
    global todo_list
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        todo_list = json.load(f)
        for task in todo_list:
            task.setdefault("priority", "Normal")
            task.setdefault("due_date", "No due date")
            task.setdefault("category", "General")
else:
    todo_list = []  

# Save Task in tasks.json
def save_task():
    with open(FILENAME, "w") as f:
        json.dump(todo_list, f, indent=4)

# Add new Task
def add_task():
    task_name = input("Enter New Task: ")
    priority = input("Enter priority (High/ Medium/ Low): ") or "Normal"
    due_date = input("Enter your due date (YYYY-MM-DD): ") or "No due date"
    category = input("enter category (Work/Personal/Study etc.)") or "General"
    
    task = {
        "task" : task_name,
        "completed" : False,
        "priority" : priority,
        "due_date" : due_date,
        "category" : category
    }

    todo_list.append(task)
    save_task()
    print("Task Added!")
    
# View task list
def view_task():
    print("To Do List Tasks \n")
    if not todo_list:
        print("No any pending tasks")
    else:
        print("Your Tasks")
        for index, task in enumerate(todo_list, start=1):
            task_name = task.get("task", "Unkown task")
            completed = task.get("completed", False)
            priority = task.get("priority", "Normal")
            due_date = task.get("due_date", "No due date")
            category = task.get("category", "General")
            
            status = "Completed" if completed else "Not Completed"
            save_task()
            print(f"{index}: {task_name} - {status} | priority :{priority} | Due: {due_date} | Category: {category}")
    print("\n")
    
# Remove task
def remove_task():
    view_task()
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                save_task()
                print(f"Task Removed: {removed_task['task']}")
            else:
                print("Invalid number")
        except ValueError:
            print("Please Enter a valid task number.")
            
# Mark as completed
def mark_task():
    view_task()
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task you have done: "))
            if 1 <= search_index < len(todo_list):
                todo_list[search_index - 1]['completed'] = True
                save_task()
                print(f"Task {todo_list[search_index]['task']} has been marked as completed!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please Enter valid task number")

#Edit task
def edit_task():
    view_task()
    try:
        task_num = int(input("Enter task number to edit: "))
        if 1 <= task_num <= len(todo_list):
            task = todo_list[task_num-1]
            
            #Let user update each field
            new_name = input(f"Task name [{task['task']}]: ") or task["task"]
            new_priority = input(f"Priority [{task['priority']}]: ") or task["priority"]
            new_due_date = input(f"Due date [{task['due_date']}]: ") or task["due_date"]
            new_category = input(f"Category [{task['category']}]: ") or task["category"]
            
            #update task
            task.update({
                "task": new_name,
                "priority": new_priority,
                "due_date": new_due_date,
                "new_category": new_category
            })
            
            save_task()
            print("Task updated successfully!")
        else:
            print("Invalid Task Number")
    except ValueError:
        print("Enter valid number")
        
#Search Task
def search_task():
    keyword = input("Enter keyword or category to search: ").strip().lower()
    found = [
        task for task in todo_list 
        if keyword in task["task"].lower() or keyword in task["category"].lower()
    ]
    if not found:
        print("Not task found")
    else:
        print("\nSearch Results:")
        for index, task in enumerate(found, start=1):
            status = "completed" if task["completed"] else "Not completed"
            print(f"{index}. {task['task']} - {status} | Priority: {task['priority']} | Due: {task['due_date']} | Category: {task['category']}")

#Sort Task
def sort_task():
    print("Sort by:")
    print("1. Priority")
    print("2. Due Date:")
    choice = input("Enter chocie:")
    
    sorted_list = todo_list.copy()
    
    if choice == "1":
        priority_order = {"High": 1, "Medium": 2, "Low": 3, "Normal": 4}
        sorted_list.sort(key=lambda t: priority_order.get(t["priority"], 4))
    elif choice == "2":
        def parse_date(d):
            try:
                return datetime.strptime(d, "%Y-%m-%d")
            except:
                return datetime.max
        sorted_list.sort(key=lambda t: parse_date(t["due_date"]))
    
    print("\nSorted Task:")
    for index, task in enumerate(sorted_list, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['task']} - {status} | Priority: {task['priority']} | Due: {task['due_date']} | Category: {task['category']}")

# To Do List Menu
def menu():
    load_task()
    while True:
        print("Selection Menu")
        print("1. Add a new task")
        print("2. View all task")
        print("3. Remove a task")
        print("4. Mark as completed")
        print("5. Update a task")
        print("6. Search task")
        print("7. Sort task")
        print("8. Exit")
        
        choice = input("Enter your choice: \n")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_task()
        elif choice == "7":
            sort_task()
        elif choice == "8":
            print("Application exiting")
            break
        else:
            print("Enter Valid Number")

menu() 