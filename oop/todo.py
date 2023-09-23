
# Task classes, handles the core information and data on each specific task.
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def set_task_completion(self, completion_state: bool) -> None:
        self.completed = completion_state

    def get_name(self) -> str:
        return self.name
    
    def get_completion(self) -> bool:
        return self.completion

# List class handles displaying tasks, saving them in a location and removing tasks. It leaves functionality for multiple todo lists to be added
class TaskList:
    def __init__(self):
        self.tasks = []

    # Loops through all tasks, used for showing users what they have and prompting edits or deletions, etc.
    def display_all_tasks(self) -> None:
        if  len(self.tasks) == 0:
            return print("--> No todo's available")
        
        for task in self.tasks:
            print(f"Name: {task.get_name()}\nCompleted: {'Y' if task.get_completion() else 'N'}")

    # Displays task information, grabbing it using its object functions
    def display_task(self, task: list) -> None:
        print(f"Name: {task.get_name()}\nCompleted: {'Y' if task.get_completion() else 'N'}")

    # Saves task object into internal list
    def add_task(self, task: list) -> None:
        self.tasks.append(task)

    # Returns a list of all tasks, useful for finding indexes of specific tasks
    def get_all_tasks(self) -> list:
        return self.tasks

    # Simply returns the task object requested, index can be fount by getting all tasks and finding it there.
    def get_task(self, index: int) -> list:
        return self.tasks[index]
    
    # Removes task from list using its index.
    def delete_task(self, index: int) -> list:
        self.tasks.pop(index)
        return self.tasks

def generate_cli_form(questions: list) -> list:
    answers = []
    
    for question in questions:
        answer = input(question + "\n Enter Here -->")
        answers.append(answer)

    return answers    

# TODO: Add CLI interactions, NOTE: do not edit task list directly from function returns. Use for viewing only. Act as if it is immutable

todo_list = TaskList()

# CLI Loop
while True:
    user_command = input("Enter a command:\n[0] View List\n[1] Create a todo\n[2] Edit a todo\n[3] Exit application\nEnter Here --> ")

    if user_command == "0":
        todo_list.display_all_tasks()
    elif user_command == "1":
        print("Create todo form")
    elif user_command == "2":
        print("Edit todo menu")
    elif user_command == "3":
        print("Application closing")
        break