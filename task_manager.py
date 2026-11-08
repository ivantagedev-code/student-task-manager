import json

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
            print(f"Task written to {filename}")

    except OSError as e:
        # e is used to print the exact error message
        print(f"Error writting to file: {e}")

def load_tasks(filename):
    try:
        with open(filename, "r") as f:
            return(json.load(f))
    except FileNotFoundError:
        return []

tasks = load_tasks("tasks.json")


def add_tasks():
    task = {}
    task['title']= input("Title: ")
    task['description'] = input("Description: ")
    task['deadline'] = input("Deadline: ")
    task['status'] = "pending"
    tasks.append(task)

add_tasks()
tasks_to_json(tasks, "tasks.json")


# enumerate --> providing both the index and the element together
for number, task in enumerate(tasks, start = 1):
    print(f"{number} . {task['title']} | {task['description']} | {task['deadline']} | {task['status']}")