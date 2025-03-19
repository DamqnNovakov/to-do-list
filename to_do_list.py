import time
import CONSTS

from utils import clear_console
from datetime import datetime
from calendar_logic import Calendar
from task_storage import TaskList
from sorting_logic import SortList


# Welcome to my ToDo List
class TO_DO_LIST:
    def __init__(self):
        self._title = None
        self._description = None
        self._completed = False
        self._tasks_list = TaskList()
        self._sorting = SortList()
        self.task = {}


    def _add_task(self):
        
        self._title = input('Enter the title of your task!> ')
        feetback = input('Do you want to add a discription to your task? (Yes/No)> ').upper()
        creation_time = time.time()
        formatted_time = str(datetime.fromtimestamp(creation_time))

        while True:
            if feetback == 'YES':
                if self._title and self._title.isdigit() == False and len(self._title) <= 20:
                    
                    self._description = input(f'Enter description to your task: {self._title}!> ')
                    if self._description:
                        while True:
                            set_deadline = input('Do you want to add a deadline to your task? (Yes/No)> ').upper()
                            
                            if set_deadline == 'YES':
                                calendar_instance = Calendar()
                                deadline, c_m = calendar_instance.pass_calendar()
 
                                print(f'The deadline for the project {self._title} is {deadline}th. of { c_m}')
                                display_deadline = f'{deadline}th. of {c_m}'
                                break
                            elif set_deadline == 'NO':
                                print('No deadline for this task')  
                                display_deadline = 'No deadline'
                                break
                            else:
                                print('Do you want to add a deadline or not?')
                                
                        

                self.task = {'Title':self._title, 'Description': self._description, 'Status' : self._completed, 'CreationDate': formatted_time, 'Deadline': display_deadline}
                self._tasks_list.add_task(self.task)
                print(f'Task: {self._title} successfully added')
            elif feetback == "NO":
                while True:
                    set_deadline = input('Do you want to add a deadline to your task? (Yes/No)> ').upper()

                    if set_deadline == 'YES':
                        calendar_instance = Calendar()
                        deadline, c_m = calendar_instance.pass_calendar()

                        print(f'The deadline for the project {self._title} is {deadline}th. of {c_m}')
                        display_deadline = f'{deadline}th. of {c_m}'
                        break
                    elif set_deadline == 'NO':
                        print('No deadline for this task')
                        display_deadline = 'No deadline' 
                        break
                    else:
                        print('Do you want to add a deadline or not?')
                        

                self.task = {'Title': self._title, 'Status' : self._completed, 'CreationDate': formatted_time, 'Deadline': display_deadline}
                self._tasks_list.add_task(self.task)
                print(f'Task: {self._title} successfully added')
            else: 
                print('Choose if you want a discription or not!')    
            break  
    
    

    def _delete_task(self):
        to_do_list = self._display_list()

        if not to_do_list or len(to_do_list) == 0:
            return
        
        delete_index = int(input('Choose the number of the task you want to delete!> ')) - 1
        
        try:
            if 0 <= delete_index < len(to_do_list):
                delete_task = to_do_list.pop(delete_index)

                # Update the existing list
                self._tasks_list.update_list(to_do_list)

                print(f'Task "{delete_task['Title']} deleted succesfully"')    
            else:
                print('Task does not exists!')
        except ValueError:
            print('Please enter a valid number!')


    def _display_list(self):
        to_do_list = self._tasks_list.get_tasks()

        if len(to_do_list) > 0:
            for i,task in enumerate(to_do_list):

                current_status = f'{CONSTS.GREEN}Completed{CONSTS.RESET}' if task['Status'] == True else f'{CONSTS.YELLOW}Active{CONSTS.RESET}'

                print(f"{i + 1}: Title: {task.get('Title', 'No Title')} | "
                f"Description: {task.get('Description', 'No Description')} | "
                f"({current_status}) {task.get('CreationDate', 'Unknown Time')} | "
                f"{CONSTS.RED}Deadline:{CONSTS.RESET} {task.get('Deadline', 'No Deadline')} | "
                f"Priority: {task.get('Priority', 'No Priority')}")
        else:
            self._empty_list()
        
        return to_do_list #return the the to_do_list here so i can use it when i call the display function!


    def _edit_task(self):
        to_do_list = self._display_list()

        if not to_do_list or len(to_do_list) == 0:
            return
        
        try:
            task_number = int(input('Choose the number of the task you want to upgrade!> ')) - 1
            if 0 <= task_number <= len(to_do_list):
                task = to_do_list[task_number]
                
                while True:
                    component_update = input('Choose the component of the tast you want to update (Title/Description) or q to quit.> ').lower()

                    if component_update == 'title':
                        new_title = input('Enter the new title!> ')
                        task['Title'] = new_title 
                    elif component_update == 'description':
                        new_description = input('Enter the new description!> ')
                        task['Description'] = new_description
                    elif component_update == 'q':
                        break
                    else:
                        print('Invalid option, try again')
                        
                self._tasks_list.update_list(to_do_list)
                print(f"Task updated: {task['Title']}")
            else:
                print('Invalid task number!')    
        except ValueError:
            print('Please enter a valid number')


    def _task_status(self):
        to_do_list = self._display_list()

        if not to_do_list or len(to_do_list) == 0:
            return
        
        try:
            task_number = int(input('Choose the number of the task you want mark as completed!> ')) - 1

            if 0 <= task_number < len(to_do_list):
                to_do_list[task_number]['Status'] = True

                self._tasks_list.update_list(to_do_list)
                task = to_do_list[task_number]['Title']
                print(f'The task {task} marked completed')
            else:
                print("Incorrect status! Mark the task as 'completed'.")
        except ValueError:
            print('Please enter a valid number')

    def _set_priority_level(self):
        to_do_list = self._tasks_list.get_tasks()
        
        if not to_do_list or len(to_do_list) == 0:
            self._empty_list()
            return
        
        level = input('Choose a priority level to your task (Low/Medium/High)> ').capitalize()
        if level not in ['Low', 'Medium', 'High']:
            print('Invalid property level! Choose from Low, Medium, High.')
            return
        try:
            self._display_list()

            choose_task = int(input('Choose the task you want and set priority level> ')) - 1

            if 0 <= choose_task < len(to_do_list):
                task_dict = to_do_list[choose_task]
                add_priority = {'Priority': level}
                task_dict.update(add_priority)

                self._tasks_list.update_list(to_do_list)
                print(f'Priority level for {to_do_list[choose_task]['Title']}')
            else:
                print('Invalid task! Please choose a valid task')
        except ValueError:
            print('Please enter a valid number')


    def _empty_list(self):
        to_do_list = self._tasks_list.get_tasks()

        if not to_do_list:
            print('------------')
            print('No Tasks Yet')
            print('------------')
            return


    # ---------------------------------------------------------------------------- 
    def run_list(self):
        while True:

            clear_console()

            print('''
########################################
#              TO-DO LIST              #
########################################
  1.  Add Task
  2.  Display List
  3.  Delete Task
  4.  Edit Task
  5.  Task Status
  6.  Add Priority Level
  7.  Sort To-Do List
  8.  Exit
########################################
''')
            
            choose = input('Choose an option (1-8)> ')

            if choose == '1':     
                self._add_task()   
            elif choose == '2':
                self._display_list()
            elif choose == '3':
                self._delete_task()    
            elif choose == '4':
                self._edit_task()               
            elif choose == '5':
                self._task_status()
            elif choose == '6':
                self._set_priority_level() 
            elif choose == '7':
                self._sorting.priority_sort()             
            elif choose == '8':
                print('Good bye!')
                break
            else:
                print('Invalid operation! Please choose again.')

            input('Press Enter to continue...')

           
        

     
    