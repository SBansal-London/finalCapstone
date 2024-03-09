# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
"""
    The code allows users to register, add tasks, view tasks, view their own tasks, generate reports,
    and display statistics, with admin privileges for additional functions.
"""
from datetime import datetime, date
from tabulate import tabulate

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user ():
    """
    The function `reg_user` adds a new user to a text file after checking for unique username and
    matching passwords.
    """
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    unique_user = False
    
    # - Request input of a new username
    while not unique_user:
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print("User name already exist. Please enter another user name")
            continue
        unique_user = True
    
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

def add_task():
    """
    The `add_task` function allows a user to add a new task to a task list stored in a file, prompting
    for task details and validating input.
    :return: The `add_task()` function does not explicitly return any value. It performs the task of
    adding a new task to the `tasks.txt` file based on user input. The function prints a message "Task
    successfully added." to indicate that the task has been successfully added to the file.
    """
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
        }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")



    """
    The `view_all` function reads tasks from a file and prints them in a formatted manner to the
    console.
    """
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


    """
    The `view_mine` function reads and displays tasks assigned to the current user, allows for task
    selection and editing, and updates the task list in a file.
    
    :param curr_user: The `curr_user` parameter in the `view_mine` function represents the current user
    for whom the tasks are being viewed. This function reads the task list and displays tasks assigned
    to the current user in a specific format. The function allows the user to interact with the tasks,
    mark them as complete
    :param task_list: The `task_list` parameter in the `view_mine` function is a list of dictionaries
    where each dictionary represents a task. Each task dictionary contains the following keys:
    :return: The `view_mine` function does not explicitly return any value. However, it does print out
    messages to the console based on the user's input and updates the tasks in the `tasks.txt` file. The
    function is designed to display tasks assigned to the current user, allow the user to select a task,
    and then perform actions such as marking the task as complete or editing the task details.
    """
def view_mine(curr_user, task_list):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    task_counter=0
    for t in task_list:
        if t['username'] == curr_user:
            print(f"Task {task_counter+1} :")
            print("----"*20)
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description:  {t['description']}"
            print(disp_str)
            print("----"*20+"\n")
            task_counter+=1
    if task_counter==0:
        print(f"No task assigned to you so far")
        return
    
    valid_task_number = False
    while not valid_task_number :
        task_number =int(input("Enter the task number from above (or enter -1 to return to main menu) :"))
        if task_number==-1:
            return
        if task_number>task_counter:
            print(f"You only have {task_counter} tasks assigned to you. Enter a valid task number :")
        else :
            print(f"You have selected task {task_number}")
            valid_task_number = True
    
    my_task_counter = 0
    my_task_found = False
    task_list_pos = 0
    while not my_task_found and task_list_pos<=len(task_list):
        if task_list[task_list_pos]['username'] == curr_user :
            my_task_counter += 1
            if my_task_counter == task_number:
               my_task_found = True 
        task_list_pos+=1

    task_list_pos= task_list_pos-1

    while True:
        my_task_menu = input(f'''what do you want to do with task {task_number} - Select one of below:
        mt - Mark the task complete
        et - Edit the task
        : ''').lower()

        if my_task_menu =="mt":
            task_list[task_list_pos]['completed'] = True
            break

        elif my_task_menu =="et":
            if task_list[task_list_pos]['completed'] == True :
                print("Task is already complete and hence cannot be edited")
                return
            else:
                while True:
                    name_edit_check = input("Print 'U' if you want to edit the user assigned to this task \nPrint 'D' if you want to edit the due date assigned to this task :")
                    if name_edit_check =='U':
                        new_username_exists = False
                        while not new_username_exists:
                            new_user_edit = input("Print the new user assigned for this task :")
                            if new_user_edit not in username_password.keys():
                                print("User does not exist")
                                continue
                            else :
                                task_list[task_list_pos]['username'] = new_user_edit
                                new_username_exists = True
                        break
                
                    elif name_edit_check == 'D':
                        while True:
                            try:
                                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                                break

                            except ValueError:
                                print("Invalid datetime format. Please use the format specified")
                        
                        
                        task_list[task_list_pos]['due_date'] = due_date_time
                        break
                    else:
                        print("Invalid input. Please enter the specified inputs only")
            break

        else :
            print("Invalid input. Please enter the specified inputs only")
    
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully updated.")


    """
    The function `generate_reports` creates task and user overview reports based on the provided task
    list and username-password dictionary.
    
    :param task_list: The `task_list` parameter in the `generate_reports` function is a list of
    dictionaries where each dictionary represents a task. Each task dictionary contains information
    about the task such as whether it is completed, the due date, and the username associated with the
    task
    :param username_password: The `username_password` parameter in the `generate_reports` function seems
    to be a dictionary that likely contains usernames as keys and passwords as values. This dictionary
    is used to gather information about users and their tasks in the system
    """
def generate_reports(task_list, username_password):
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass
    
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
 
    completed_task = 0
    overdue_tasks = 0
    task_overview_list = []
    task_overview_list.append(["Total number of tasks",str(len(task_list))])
    for t in task_list:
            if t['completed'] == True :
                completed_task += 1
    task_overview_list.append(["Total number of completed tasks",completed_task])
    task_overview_list.append(["Total number of incompleted tasks",str(len(task_list)-completed_task)])
    for t in task_list:
            if t['completed'] == False and  t['due_date']<datetime.now():
                    overdue_tasks +=1
    task_overview_list.append(["Total number of overdue tasks",overdue_tasks])
    task_overview_list.append(["Percentage of incomplete tasks", int((len(task_list)-completed_task)/len(task_list)*100)])
    task_overview_list.append(["Percentage of overdue tasks", int(overdue_tasks/len(task_list)*100)])

    with open("task_overview.txt", 'w') as task_overview_file:
        task_overview_file.write(tabulate(task_overview_list))
        

    with open("user_overview.txt", 'w') as user_overview_file:
        user_overview_file.write("Total number of users \t\t\t\t\t"+str(len(username_password)))
        user_overview_file.write("\nTotal number of tasks \t\t\t\t\t"+str(len(task_list))+"\n")
        table = [["User", "Total tasks", "'%' of total tasks", "'%' of completed tasks", "'%' of uncompleted tasks", "'%' of overdue tasks"]]
        
        for user in username_password.keys():
            total_tasks_user = 0
            completed_task_user = 0
            overdue_task_user = 0
            for t in task_list:
                if t['username'] == user :
                    total_tasks_user +=1
                    if t['completed'] == True :
                        completed_task_user +=1
                    elif t['due_date']<datetime.now() :
                        overdue_task_user+=1

            if len(task_list)== 0 :
                per_total_task = 0
                per_completed_task = 0
                per_incomplete_task = 0
                per_overdue_task = 0
            else :
                per_total_task = int(total_tasks_user/len(task_list)*100)
            
            if total_tasks_user == 0 :
                per_completed_task = 0
                per_incomplete_task = 0
                per_overdue_task = 0
            else :
                per_completed_task = int(completed_task_user/total_tasks_user*100)
                per_incomplete_task = int(100-per_completed_task)
                per_overdue_task = int(overdue_task_user/total_tasks_user*100)
            
            table.append([user,total_tasks_user,per_total_task,per_completed_task,per_incomplete_task,per_overdue_task])
            
        user_overview_file.write((tabulate(table)))


    # Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# The code provided is a Python script that implements a basic login system. Here is a breakdown of
# what the code does:

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# The above Python code is creating a dictionary `username_password` from `user_data`, where each
# key-value pair represents a username and password. It then prompts the user to input a username and
# password for login. It checks if the entered username exists in the dictionary and if the
# corresponding password matches. If the username does not exist, it prints "User does not exist" and
# continues the loop. If the password is incorrect, it prints "Wrong password" and continues the loop.
# If the username and password are correct, it prints "Login Successful!" and sets `logged_in` to
# True, exiting

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # The code snippet provided is a Python script that presents a menu of options based on the user
    # currently logged in. If the current user is not "admin", a menu with options for registering a
    # user, adding a task, viewing all tasks, viewing the user's tasks, displaying statistics, and
    # exiting is displayed. If the current user is "admin", an additional option to generate reports
    # is included in the menu.
    
    if curr_user != "admin":
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    : ''').lower()
    
    else:
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    if menu == 'r':
        reg_user()    

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(curr_user,task_list)
                
    
   # The code snippet provided is a part of a Python program that handles different menu options based
   # on user input. Here is a breakdown of what the code is doing:
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        
        if not (os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt")):
            generate_reports(task_list, username_password)
        
        with open("task_overview.txt", 'r') as task_overview_file:
            task_stats_data = task_overview_file.read().split("\n")
        print("Tasks overview:\n")
        for t in task_stats_data:
            print(t)

        with open("user_overview.txt", 'r') as user_overview_file:
            user_stats_data = user_overview_file.read().split("\n")
        print("\n\nUsers overview:\n")
        for t in user_stats_data:
            print(t)

    elif menu == 'gr':
        if curr_user == 'admin':
            generate_reports(task_list, username_password)
        else :
            print("You have made a wrong choice, Please Try again")
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
