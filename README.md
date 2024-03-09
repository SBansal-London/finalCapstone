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

Updates
Existing functionality moved from main body to a set of functions, improving readability
Issue of registering duplicate users fixed
Option to edit tasks assigned to current user (mark as complete, reassign task, change due date)
Functionality added to automatically update .txt file with these changes
Option to generate task overview report with data regarding the status of tasks managed by the application
Option to generate user overview report with data regarding allocation of tasks to users registered with the application and the status of tasks managed by application for each user
Display statistics function modified to read in information directly from .txt files
Control flow improved for better user experience
Code checked for style consistency and descriptive variable names
Thorough documentation added
2 - Installation
To install the application, simply click on 'task_manager.py'. This will bring up the code for the program in GitHub. In the top right, click on 'Download raw file' and save the file in a location of your choice.

3 - Instructions For Use
In your IDE (e.g. Visual Studio Code), open the folder that you have saved the task manager in. It is important that you always have this folder open when using the task manager, as the program reads from and writes to text files that will be created and stored in this folder.

ss1

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
