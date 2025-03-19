import CONSTS
import copy
from task_storage import TaskList

class SortList:
    def __init__(self):
        self._task_list = TaskList()

    def _sorting_by_priority_level(self):
        to_do_list = self._task_list._load_from_list()

        if not to_do_list or len(to_do_list) == 0:
            print('------------')
            print('No Tasks Yet')
            print('------------')
            return
        
        while True:
                try:
                    option = int(input('''What option do you choose:
        1. Sort by priority level (Low/Medium/High).
        2. Show all tasks from a single level (Low/Medium/High).
        3. Exit
        > '''))
                    if option in [1, 2, 3]:
                        break 
                    else:
                        print("Incorrect option! Choose 1 or 2.")

                except ValueError:
                    print("Invalid input! Please enter a number (1 or 2).")

        print(f"You selected option {option}")

        tasks = copy.deepcopy(to_do_list)

        if option == 1:
            priority_order = {'High': 1, 'Medium': 2, 'Low': 3, '': 4}
            sorted_tasks = sorted(tasks, key= lambda task : priority_order.get(task.get('Priority', ''), 4))

            for i, task in enumerate(sorted_tasks):
                print(f"{i + 1}: Title: {task.get('Title', 'No Title')} | "
                f"Description: {task.get('Description', 'No Description')} | "
                f"({task.get('Status', 'No Status')}) {task.get('CreationDate', 'Unknown Time')} | "
                f"{CONSTS.RED}Deadline:{CONSTS.RESET} {task.get('Deadline', 'No Deadline')} | "
                f" Priority:{task.get('Priority', 'No Priority')}")
        elif option == 2:
            level = input('Choose a priority level to your task (Low/Medium/High)> ').capitalize()
            if level not in ['Low', 'Medium', 'High']:
                print('Invalid property level! Choose from Low, Medium, High.')
                return

            sorted_tasks = [task for task in tasks if task.get('Priority', '') == level]

            if not sorted_tasks:
                print(f'No tasks founded with priority: {level}')
                return

            for i, task in enumerate(sorted_tasks):
                print(f"{i + 1}: Title: {task.get('Title', 'No Title')} | "
                f"Description: {task.get('Description', 'No Description')} | "
                f"({task.get('Status', 'No Status')}) {task.get('CreationDate', 'Unknown Time')} | "
                f"{CONSTS.RED}Deadline:{CONSTS.RESET} {task.get('Deadline', 'No Deadline')} | "
                f" Priority: {task.get('Priority', 'No Priority')}")
        elif option == 3:
            return
    
    def priority_sort(self):
        return self._sorting_by_priority_level()

    
