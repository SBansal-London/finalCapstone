# finalCapstone
## Final Capstone project 

### Contents
1. Description
2. Installation
3. Instructions For Use
4. Credits

### 1 - Description
The project is designed for a small business to help it manage tasks assigned to each member of a team. 

#### Features
Initial login into the application with authentication stored in separate .txt file

Register a new user

Add a task with details : username, title, description, due date, date assigned

View all tasks

View tasks assigned to current logged in user

Current user can update its assigned tasks to either mark them complete, update the due date or assign the task to another user

Display statistics (number of users and tasks)

Admin specific tasks :

Generate user report - providing a summary of current users and statistics of various tasks assigned to them

Generate Task report - providing a summary of total tasks tracked by the application, % of open tasks and % of overdue tasks

### 2 - Installation
To install the application :
1. Click on 'task_manager.py'. This will bring up the code for the program in GitHub.
2. In the top right, click on 'Download raw file'
3. Save the file in a location of your choice. Preferably create a new folder and store the file in that location (e.g. local drive or Desktop)

### 3 - Instructions For Use
In Visual Studio Code, open the folder that you have created while installation.


Open the task manager and run the program. The first time you run the program, two text files will be created in the folder: 'tasks.txt' and 'user.txt'. It is recommended that you do NOT open or edit these, unless you want to delete a task or a user (see later).

ss2

To login, use the username "admin", and the password "password". This will bring up a menu, giving you access to the functions in the program.

ss3

If you want to delete a task, first exit the program. Then, open 'tasks.txt' and remove the single line containing the task in question. Avoid making changes to any other tasks, as this could lead to them being read in incorrectly!

ss4

ss5

The same applies for deleting a user. Avoid removing the line containing the admin login details - an empty 'user.txt' file will prevent you from using the program!

The 'generate reports' option will create two more text files in the folder: 'task_overview.txt' and 'user_overview.txt'. Each time you generate reports, these files will be overwritten with the current status of tasks managed by the program.

ss6

ss7

ss8

4 - Credits
HyperionDev: Existing features as outlined in '1. Description'
Richard Gotts: Updates as outlined in '1. Description'
