import json
from tabulate import tabulate

# A function to write tasks to a json file
def tasks_to_json(tasks, filename):
    # validate that tasks is a list
    if not isinstance(tasks, list):
        raise ValueError("Tasks must be a list")
    for task in tasks:
        # Ensure all task are string or dictionary
        if not isinstance(task, (dict)):
            raise ValueError(f"{task} must be a dictionary")
    try:
        with open(filename, "w", encoding = "utf-8") as file:
            # dump() converts tasks list into file in json format
            # dumps() converts tasks list to json but return as a string instead of a file
            json.dump(tasks, file, indent = 1)
    except OSError as e:
        # e is used to print the exact error message
        print(f"Error writting to file: {e}")

# A function to load everything in json file to our tasks list
def load_tasks(filename):
    try:
        with open(filename, "r") as f:
        # load() --> Read from a file on your computer.
            return(json.load(f))
    except FileNotFoundError:
        return []
tasks = load_tasks("tasks.json")

# To get right input
def correct_input(prompt):
    while True:
        reply = input(prompt).strip()
        if reply != "":
            return reply
        print("This can't be empty")

# to add task to the list tasks
def add_tasks():
    task = {} 
    task['title']= correct_input("Title: ")
    task['description'] = correct_input("Description: ")
    task['deadline'] = correct_input("Deadline: ")   
    task['status'] = "pending"
    tasks.append(task)
    print("Task added succesfully!")

# Display result as a table
def print_table(task_list):
    table_data = []
    
    for number, task in enumerate(task_list, start=1):
        mark = "[ ✔ ]" if task['status'] == "completed" else "[ X ]"
        
        # Build a simple list for each row
        table_data.append([
            number, 
            mark, 
            task['title'], 
            task['description'], 
            task['deadline'], 
            task['status']
        ])
        
    # Print the entire table at once
    headers = ["No.", "Done", "Title", "Description", "Deadline", "Status"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# A function to view the tasks
def view_tasks():
    if len(tasks) == 0:
            print("No tasks yet!")
            return
    print_table(tasks)

# A function to get the task number    
def task_number():
    if len(tasks) == 0:
        return None
    while True:
        text = input("Task number (Press Enter to cancel): ")
        if text == "":
            return None
        try:
            number = int(text)
        except ValueError:
            print("Please type a number")
            continue
        else:
            if number < 1 or number > len(tasks):
                print("No task with that number")
                continue
        return number - 1

# A function to complete a task
def complete_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    tasks[position]["status"] = "completed"
    tasks_to_json(tasks, "tasks.json")
    print(f"{tasks[position]['title']} completed!")

# A function to delete a task
def delete_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    removed = tasks.pop(position)
    tasks_to_json(tasks, "tasks.json")
    print(f"{removed['title']} deleted!")

# A function to edit a task
def edit_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    task = tasks[position]
    print("If you don't wanna edit, just click enter")
    title = input("Tilte: ").strip()
    if title != "":
        task['title'] = title
    description = input("Description: ").strip()
    if description != "":
            task['description'] = description
    deadline= input("Deadline: ").strip()
    if deadline != "":
            task['deadline'] = deadline
    tasks_to_json(tasks, "tasks.json")
    print(f"Task {position + 1} updated!")

# To dispaly based on condition
def filter_task():
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    while True:
        status = input("Pending OR Completed: ").strip().lower()
        if status != "pending" and status != "completed":
            print("Please type pending or completed")
            continue
        else:
            break
    matches = []
    for task in tasks:
        if task['status'] == status:
            matches.append(task)
    if not matches:
        print("No task found")
        return
    print_table(matches)

# Taking user input on what to do
while True:
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark complete")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Filter tasks")
    print("7. Exit")
    choose = input("Choose (1-7): ")
    if choose == "1":
        add_tasks()
        tasks_to_json(tasks, "tasks.json")

    elif choose == "2":
        view_tasks()

    elif choose == "3":
        complete_task()

    elif choose == "4":
        edit_task()

    elif choose == "5":
        delete_task()

    elif choose == "6":
        filter_task()

    elif choose == "7":
        break

    else:
        print("Invalid choice, try again!")
