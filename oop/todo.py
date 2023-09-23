
# Task classes, handles the core information and data on each specific task.
class Task:
    def __init__(self, name: str):
        self.name = name
        self.completed = False

    def set_task_completion(self, completion_state: bool) -> None:
        self.completed = completion_state

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def get_completion(self) -> bool:
        return self.completed

# List class handles displaying tasks, saving them in a location and removing tasks. It leaves functionality for multiple todo lists to be added
# NOTE: do not edit task list directly from function returns. Use for viewing only. Act as if it is immutable
class TaskList:
    def __init__(self):
        self.tasks = []

    # Loops through all tasks, used for showing users what they have and prompting edits or deletions, etc.
    def display_all_tasks(self) -> None:
        if  len(self.tasks) == 0:
            return print("--> No todo's available")
        
        # Divider to clean up CLI for end user
        print("_______________________")
        for index, task in enumerate(self.tasks):
            print(f"[{index}]\nTodo: {task.get_name()}\nCompleted: {'Yes' if task.get_completion() else 'No'}\n_______")
    
    # Displays task information, grabbing it using its object functions
    def display_task(self, task) -> None:
        print(f"Todo: {task.get_name()}\nCompleted: {'Yes' if task.get_completion() else 'No'}")

    # Saves task object into internal list
    def add_task(self, task) -> None:
        self.tasks.append(task)

    # Returns a list of all tasks, useful for finding indexes of specific tasks
    def get_all_tasks(self) -> list[Task]:
        return self.tasks

    # Simply returns the task object requested, index can be fount by getting all tasks and finding it there.
    def get_task(self, index: int) -> list:
        return self.tasks[index]
    
    # Removes task from list using its index.
    def delete_task(self, index: int) -> list:
        self.tasks.pop(index)
        return self.tasks

# Generates forms and returns answers in a list, answers should be accessed via index. Useful for building tasks or editing tasks etc.
def generate_cli_form(questions: list) -> list:
    answers = []
    
    for question in questions:
        answer = input(question + "\n--> ")
        answers.append(answer)

    return answers    

# Creating primary task list
todo_list = TaskList()

# CLI Loop
while True:
    user_command = input("Enter a command:\n[0] View List\n[1] Create a todo\n[2] Edit a todo\n[3] Exit application\n--> ")

    if user_command == "0":
        todo_list.display_all_tasks()
    elif user_command == "1":
        # Pull name from a cli form, generate a new task object and insert into current task list, notify user it has been created
        task_form_answers = generate_cli_form(["Name of todo:"])
        new_task = Task(task_form_answers[0])
        todo_list.add_task(new_task)
        print(">> New todo task created")

    elif user_command == "2":
        # Display tasks, validate user picked task. Ask to change choice or task name and then submit those changes
        todo_list.display_all_tasks()        
        task_index = input("Choose a task number to edit\n--> ")
        
        # Guard clause to validate task is a valid task object
        if not task_index.isdigit() or int(task_index) > len(todo_list.get_all_tasks()) - 1:
            print("Error: Did not choose a valid number or chose a number bigger that doesn't correlate to a task")
            continue
            
        # Getting the edit choice and getting new values
        edit_choice = input("Would you like to edit [0] name or [1] completion value?\n--> ")
        
        # Guard clause to validate if option is a valid option
        if not edit_choice.isdigit() or int(edit_choice) > 1 or int(edit_choice) < 0:
            print("Error: Picked an option out of range or command is not recognized")
            continue
        
        # Get task from the array
        task_currently_editing = todo_list.get_all_tasks()[int(task_index)]

        if edit_choice == "0":
            # Fetch new task name, and set the object name to it
            new_name = input("Enter new name value\n--> ")
            task_currently_editing.set_name(new_name)
            print(">> Task name successfully set to: " + new_name)

        elif edit_choice == "1":
            # Set state to true or false or exit out of the current CLI loop if wrong information is given
            new_completion_state = input("Is the task completed (Y) or (N)")
            
            if new_completion_state == "Y":
                task_currently_editing.set_task_completion(True)
            elif new_completion_state == "N":
                task_currently_editing.set_task_completion(False)
            else:
                print("Error: Command not recognized")
                continue

    elif user_command == "3":
        print("Application closing")
        break