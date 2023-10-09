from datetime import datetime, timedelta
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements

    task["lastActivity"] = datetime.now().strftime('%m/%d/%y %H:%M:%S')     # Last activity update with current time.
    task["name"] = name                                                     # Name attribute update.
    task["description"] = description                                       # Description attribute update.
    try:
        task["due"] = str_to_datetime(due).strftime('%m/%d/%y %H:%M:%S')    # Due date update.
    except ValueError:
        print("\n*** Failed to add task due to Invalid date format ***\n")  # Throws Invalid date format exception.
        return
    if '' in task.values():                                                 # Checks for any empty values in the task.
        print("\n*** Failed to add task due to missing values in the input.***") # Task will not be added if any missing values are found.
    else:
        tasks.append(task)                                                  # Task will be added to task list if inputs are valid.
        print("\n*** Task has been added successfully! ***\n")
    
    # UCID: sb2648, Date: 10/05/2023
    '''New task will be added to the task list. 
    For this we have set name, description and due date attributes to the task instance and added this dictionary to the tasks list and finally save method is called.
    Task will not be added if any of the invalid inputs are provided to this method. 
    '''
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    """ UCID:sb2648, Date: 10/05/2023
        Here, in this method if the given index is greater than or equals to zero and less than length of the tasks list then we retreive the current task details and the information is shown to the user.
        User is prompted to enter name, description and Due date details for the task update. Provided information is given to update_task function to update the task in task list.
        Incase, the index is invalid then a message is shown to user to select valid index to perform task update.
    """
    if index < 0 or index > len(tasks):
        print("\n *** No task found at the provided index, please try with a valid index **")
        return
    try:
        if index > 0 and index <= len(tasks):          # Checks the index if it is greater than zero and less than or equal to length of the list.
            selected_task = tasks[index]                # Retreives the task information for the selected index.
            curr_name, curr_due, curr_lastActivity,curr_description, curr_status = selected_task.values() # Retreiving the values of the attributes.
            name = input(f"What's the name of this task? ({curr_name}) \n").strip() # Shows the current task name and new input is taken.
            desc = input(f"What's a brief descriptions of this task? ({curr_description}) \n").strip() # Shows the current task Description new input is taken.
            due = input(f"When is this task due (format: m/d/y H:M:S) ({curr_due}) \n").strip() # Shows the current task due date new input is taken.
            update_task(index, name = name, description = desc, due = due) # Updates the task with provided information new input is taken.
    except IndexError:          # Handled out of bound exception and a message is shown to user to select valid index.
        print("\n *** No task found.Failed to process update request, please try again with valid index *** \n")

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    
    """ UCID: sb2648, Date: 10/06/2023
        Retreiving the task for the provided index and the update of new attributes are performed if new values are provided.
        Performs the task update at the provided index.
        Prints a valid message for an exception if any invalid information is provided for the update task.
    """
    try:
        if len(name)!= 0 or  len(description)!= 0 or len(due) != 0: # Checks if any updates are provided to the attributes
            curr_task = tasks[index]    # Retrives the task from the task list from the provided index
            curr_task["name"] = name    # Updates the current task with the new task name.
            curr_task["description"] = description # Updates the current task with the new task description.
            curr_task["due"] = due      # Updates the current task with the new task due.
            curr_task["lastActivity"] = datetime.now().strftime('%m/%d/%y %H:%M:%S') # Updates last Activity with the current date and time.
            print("\n*** Updated the task Successfully! ***\n")
        else:   
            curr_task["lastActivity"] = datetime.now().strftime('%m/%d/%y %H:%M:%S') # If no updates are provided then last activity is updates with current date and time.
    except Exception:
        print("\n *** No new updates were provided *** \n")
    
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    
    """ UCID: sb2648, Date: 10/06/2023 
    In this function, task at given index is retrieved and if the task is already completed then we print a message to the user saying that task is already completed.
    If the task is not completed then we mark the task as done by updating done attribute with current date and time. 
    Index out of bounds is handled and a message is shown to user to select a valid task.
    """
    try:
        task = tasks[index] # Retreives the task form the task list at the provided index.
        if not task["done"]:    # Checks for the done attribute is false.
            task["done"] = datetime.now().strftime('%m/%d/%y %H:%M:%S')     # Updates the task as done with current date time if it is not already completed.
            print("\n*** Task is marked as done at {} ***\n".format(task["done"]))
        else:
            print("\n*** This task is already completed! ***\n")    # Prints the message as already completed if task is already completed.
    except Exception:
        print("\n *** No task found at the provided index, select a valid index. *** \n") # Handled exception for list out of bounds.

    save()

def view_task(index):
    """ View more info about a specific task fetch by index """

    """ UCID: sb2648, Date: 10/05/2023
    Retrieved the task for the given index and the formatted task information is printed on the console.
    If any exception occured for invalid index then a message is shown to the user that user selected invalid index.
    """
    try:
        task = tasks[index] # Select the task from the provided index
        print(f"""
            [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
            Description: {task['description']} \n 
            Last Activity: {task['lastActivity']} \n
            Due: {task['due']}\n
            Completed: {task['done'] if task['done'] else '-'} \n
            """.replace('  ', ' ')) # Prints the output of the selected task.
    except Exception:
        print("\n*** No task found at the provided index, select a valid index to view the task ***\n")


def delete_task(index):
    """ deletes a task from the tasks list by index """
    
    """UCID: sb2648, Date: 10/06/2023
    Task for the given index is deleted from the list.
    Index out of bound exception is handled and a message is shown to select a valid input to delete the task from the list.
    """
    try:
        del tasks[index]    # Deletes selected task form the task list.
        print("\n*** Successfully deleted the selected task!***\n")
    except Exception as e:
        print("\n ** No task found at the selected index, Select valid item from the task list for deletion **\n")
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    
    """UCID:sb2648, Date:10/06/23
    We get the tasks which are not marked as done i.e, marked as False and those tasks are added to _tasks list and this list is given to list_task()function.
    """
    _tasks = []

    for each_task in tasks:
        if not each_task["done"]: 
            _tasks.append(each_task)
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    
    """ UCID:sb2648, Date: 10/06/23
    Here, we are iterating over the list of tasks and we consider the tasks which are not marked as done and which are older than the current date and time. 
    For this we take the difference of current time and due date for the task.
    These tasks are added to a list and are passed to the list_tasks().
    """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = []
    current_datetime = datetime.now()
    for each_task in tasks:
        if (current_datetime - str_to_datetime(each_task["due"]) > timedelta(0)) and (each_task["done"] == False):
            _tasks.append(each_task)
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    
    """UCID: sb2648, Date: 10/06/23
    Here, in this function we get the task by index and we calculate the time and date difference between current date and time to due date mentioned of the task. If it is overdue, we print a message saying that the task is overdue by X days, X hours, X minutes, X seconds overdue.
    Incase, it is not overdue but it is still pending then we print a message saying X days, X hours, X minutes, X seconds left remaining.
    """

    try:
        task = tasks[index]
        current_datetime = datetime.now()
        task_due_time = str_to_datetime(task["due"])
        remaining_time =  task_due_time - current_datetime
        
        if remaining_time.total_seconds() < 0:
            remaining_time = abs(remaining_time)
            overdue_message = "overdue"
        else:
            overdue_message = "remaining"
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds {overdue_message}")
    except Exception as e:
        print("\n*** No tasks found at the selected index. Select valid item from the task list to get remaining time ***\n")

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()