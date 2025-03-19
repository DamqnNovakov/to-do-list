import json
import CONSTS

class TaskList:
    def __init__(self):
        self.task_list = []

    def _save_in_list(self, task: dict[str]):
        try:
            with open(CONSTS.TASK_LIST_NAME, 'r') as file:
                self.task_list = json.load(file)
        except FileNotFoundError:
            print('No such file exists')
            self.task_list = []
        except json.JSONDecodeError:
            print('File is empty or corrupted, initializing with empty list.')
            self.task_list = [] 
        
        self.task_list.append(task)

        try:
            with open(CONSTS.TASK_LIST_NAME, 'w') as file:
                json.dump(self.task_list, file, indent = 4)
        except FileNotFoundError:
            print('No such file exists')

    def _load_from_list(self):
        try:
            with open(CONSTS.TASK_LIST_NAME, 'r') as file:
                self.task_list: list[dict] = json.load(file)
                return self.task_list
        except FileNotFoundError:
            print('No such file exists') 

    def _update_list(self, to_do_list):
        try:
            with open(CONSTS.TASK_LIST_NAME, 'w') as file:
                json.dump(to_do_list, file, indent = 4)
        except FileNotFoundError:
            print('No such file exists')


    def add_task(self, task):
        self._save_in_list(task)

    def get_tasks(self):
        return self._load_from_list()
    
    def update_list(self, to_do_list):
        self._update_list(to_do_list)
