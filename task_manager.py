tasks = [
    {"title": "Record Submission",
     "description": "Record submission on Monday",
     "status": "pending",
     "deadline": "Monday"},
    {"title": "Exam",
     "description": "Exam on Friday",
     "status": "pending",
     "deadline": "Friday"}
]

for number, task in enumerate(tasks, start = 1):
    print(f"{number} . {task["title"]} | {task["description"]} | {task["status"]} | {task["deadline"]}")