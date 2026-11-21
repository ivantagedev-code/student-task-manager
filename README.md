Student Task Manager

A simple command-line app to keep track of your tasks and deadlines. Tasks are saved in a JSON file, so they are still there the next time you run the program.

Features
Add tasks with a title, description and deadline
View tasks in a table, sorted by deadline (pending tasks first, completed ones at the bottom)
Mark tasks as complete
Edit tasks (press Enter to keep a field as it is)
Delete tasks
Filter tasks by pending or completed
Deadline tracking: each pending task shows how many days are left, "Due today", or how many days it is overdue
Saved automatically to tasks.json after every change
Input checks: empty fields and wrong date formats are rejected
Requirements
Python 3.6 or higher
tabulate library

Install the library with:

bash
pip install tabulate

json and datetime come with Python, so there is nothing else to install.

How to Run
Save the code as task_manager.py (or any name you like).
Open a terminal in that folder.
Run:
bash
python task_manager.py
Usage

When you start the program you will see this menu:

=== Student Task Manager ===
1. Add task
2. View tasks
3. Mark complete
4. Edit task
5. Delete task
6. Filter tasks
7. Exit
Choose (1-7):

Type a number and press Enter.

Option	What it does
1	Asks for a title, description and deadline, then adds the task as pending
2	Shows all tasks in a table
3	Shows the tasks, then asks for the number of the task to mark as completed
4	Shows the tasks, then asks which one to edit. Press Enter on any field to leave it unchanged
5	Shows the tasks, then asks which one to delete
6	Shows only pending or completed tasks, whichever you type
7	Exits the program

When it asks for a task number, you can press Enter without typing anything to cancel.

Deadline format: dd-mm-yyyy, for example 25-12-2026.

Example output
╒═══════╤════════╤═══════════════╤════════════════════╤════════════╤═══════════════╕
│   No. │ Done   │ Title         │ Description        │ Deadline   │ Status        │
╞═══════╪════════╪═══════════════╪════════════════════╪════════════╪═══════════════╡
│     1 │ [ X ]  │ Physics lab   │ Finish the record  │ 25-11-2026 │ 4 day(s) left │
├───────┼────────┼───────────────┼────────────────────┼────────────┼───────────────┤
│     2 │ [ ✔ ]  │ Task 3 write  │ Open source task   │ 21-11-2026 │ Done          │
╘═══════╧════════╧═══════════════╧════════════════════╧════════════╧═══════════════╛

The exact table will depend on your tasks and today's date.

How the Data Is Stored

Tasks are kept in tasks.json in the same folder as the program. The file is created the first time you add a task. Each task looks like this:

json
{
 "title": "Physics lab",
 "description": "Finish the record",
 "deadline": "25-11-2026",
 "status": "pending"
}

status is either pending or completed.

If tasks.json is missing, the program starts with an empty list. If the file is damaged, it prints a message and also starts empty.

Project Structure
.
├── task_manager.py   # the program
├── tasks.json        # your saved tasks (created automatically)
└── README.md
Notes
Tasks are numbered in the order shown in the table. The list is re-sorted every time you view it, so check the number before you complete, edit or delete a task.
Editing a task does not change its status. Use option 3 to mark it as completed.
Deleting a task cannot be undone.
Built With
Python
json for saving and loading data
datetime for handling deadlines
tabulate for the table display

