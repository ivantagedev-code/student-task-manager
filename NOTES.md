# Design Choices & AI Usage

## Design Choices

**JSON instead of CSV.** Each task is a dictionary with a title, description, deadline and status. JSON stores this structure directly.

**Tabulate for display.** I learned `tabulate` from a CS50P problem set where we read its documentation. A table makes deadlines and statuses much easier to scan than plain printed lines.

**Saving after every change.** Tasks are loaded into a list at startup, and `tasks.json` is rewritten after every add, edit, complete or delete, so nothing is lost if the program closes unexpectedly.

**Input validation.** Empty fields are rejected, dates must follow `dd-mm-yyyy` (checked with `datetime.strptime`), and task numbers must exist in the list. Pressing Enter cancels an action. If `tasks.json` is missing or corrupted, the program starts with an empty list instead of crashing.


## AI Usage

I wrote and manually tested the code myself, using what I learned in CS50P. When I needed help understanding specific functions or modules, I checked Google and the official documentation first, and asked Claude when something was still unclear. I also used Claude to help write the README and this notes file.