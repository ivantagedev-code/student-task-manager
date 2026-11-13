import json
from tabulate import tabulate
from datetime import datetime

filename = "tasks.json"
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
        print(f"✘ Could not save tasks: {e}")

# A function to load everything in json file to our tasks list
def load_tasks(filename):
    try:
        with open(filename, "r") as f:
        # load() --> Read from a file on your computer.
            return(json.load(f))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("ℹ Saved file is damaged. Starting with an empty list.")
        return []
tasks = load_tasks(filename)

# To get deadline as a date
def deadline_date():
    while True:
        deadline = input("Deadline (dd-mm-yyyy): ").strip()
        try:
            if len(deadline) != 10:
                raise ValueError
            # strptime turns the text into a date
            datetime.strptime(deadline, "%d-%m-%Y")
            return deadline
        except ValueError:
            print("✘ Use dd-mm-yyyy")

# To sort according to the deadline
def sort(task):
    due = datetime.strptime(task['deadline'], "%d-%m-%Y")
    return (task['status'] == "completed", due)

# To get right input
def correct_input(prompt):
    while True:
        reply = input(prompt).strip()
        if reply != "":
            return reply
        print("✘ This field can't be empty")

# to add task to the list tasks
def add_tasks():
    task = {} 
    task['title']= correct_input("Title: ")
    task['description'] = correct_input("Description: ")
    task['deadline'] = deadline_date()  
    task['status'] = "pending"
    tasks.append(task)
    tasks_to_json(tasks, filename)
    print("✔ Task added successfully!")

# To get today's date for comparison
today = datetime.today().date()

# Display result as a table
def print_table(task_list):
    table_data = []
    today = datetime.today().date()

    for number, task in enumerate(task_list, start=1):
        due = datetime.strptime(task['deadline'], "%d-%m-%Y").date()
        mark = "[ ✔ ]" if task['status'] == "completed" else "[ X ]"

        days_left = (due - today).days

        if task['status'] == "completed":
            status_text = "Done"
        elif days_left < 0:
            status_text = f"⚠ OVERDUE by {-days_left} day(s)"
        elif days_left == 0:
            status_text = "Due today"
        else:
            status_text = f"{days_left} day(s) left"

        table_data.append([
            number,
            mark,
            task['title'],
            task['description'],
            task['deadline'],
            status_text
        ])

    headers = ["No.", "Done", "Title", "Description", "Deadline", "Status"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# A function to view the tasks
def view_tasks():
    if len(tasks) == 0:
            print("ℹ No tasks yet. Choose 1 to add one.")
            return
    # tasks.sort() will call sort on every task and reorders the list.
    # sorted() is not used as it would make a copy and break the numbering.
    tasks.sort(key=sort)
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
            print("✘ Please type a number")
            continue
        else:
            if number < 1 or number > len(tasks):
                print("✘ No task with that number")
                continue
        return number - 1

# A function to complete a task
def complete_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    tasks[position]["status"] = "completed"
    tasks_to_json(tasks, filename)
    print(f"{tasks[position]['title']} completed!")

# A function to delete a task
def delete_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    removed = tasks.pop(position)
    tasks_to_json(tasks, filename)
    print(f"{removed['title']} deleted!")

# A function to edit a task
def edit_task():
    view_tasks()
    position = task_number()
    if position is None:
        return
    task = tasks[position]
    print("ℹ Press Enter to keep a field unchanged")
    title = input("Title: ").strip()
    if title != "":
        task['title'] = title
    description = input("Description: ").strip()
    if description != "":
            task['description'] = description
    deadline= input("Deadline (dd-mm-yyyy): ").strip()
    if deadline != "":
        try:
            datetime.strptime(deadline, "%d-%m-%Y")
            task['deadline'] = deadline
        except ValueError:
            print("✘ Invalid date, keeping old deadline")

    tasks_to_json(tasks, filename)
    print(f"✔ Task {position + 1} updated")

# To display based on condition
def filter_task():
    if len(tasks) == 0:
        print("ℹ No tasks yet. Choose 1 to add one.")
        return
    tasks.sort(key=sort)
    while True:
        status = input("Pending OR Completed: ").strip().lower()
        if status != "pending" and status != "completed":
            print("✘ Please type pending or completed")
            continue
        else:
            break
    matches = []
    for task in tasks:
        if task['status'] == status:
            matches.append(task)
    if not matches:
        print("ℹ No matching tasks found")
        return
    print_table(matches)

def main():
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
            print("✘ Invalid choice. Please choose 1 to 7")

if __name__ == "__main__":
    main()