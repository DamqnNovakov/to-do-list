import calendar
import CONSTS
from datetime import datetime


class Calendar:
    def __init__(self):
        self._current_date = datetime.now().day
        self._month = datetime.now().month
        self._year = datetime.now().year

        self._cal = calendar.TextCalendar(firstweekday = 0)
        self._cal_str = self._cal.formatmonth(self._year,self._month)
        self._current_m = calendar.month_name[self._month]
        self._last_day = calendar.monthrange(self._year, self._month)[1]


    def _displayCalendar(self):
        print(f'   {self._current_m}')

        for i,line in enumerate(self._cal_str.split('\n')):
            if i >= 1 and any(char.isdigit() for char in line): 
                for num in line.split():
                    if int(num) == self._current_date:
                        print(f"{CONSTS.GREEN}{num}{CONSTS.RESET}", end=' ') 
                    else:
                        print(num, end=' ') 
                print()

        
    def _chooseDeadline(self):
        self._displayCalendar()

        while True:
            try:
                deadline = int(input(f'Choose from the calendar the deadline day> '))
                duration = deadline - self._current_date
                
                if 1 <= deadline <=  self._last_day and deadline >= self._current_date:
                    
                    print(f'   {self._current_m}')
                    for i,line in enumerate(self._cal_str.split('\n')):
                        if i >= 1 and any(char.isdigit() for char in line): 
                            for num in line.split():
                                if int(num) == deadline:
                                    print(f"{CONSTS.RED}{num}{CONSTS.RESET}", end=' ') 
                                elif int(num) == self._current_date:
                                    print(f"{CONSTS.GREEN}{num}{CONSTS.RESET}", end=' ') 
                                elif self._current_date < int(num) < deadline:
                                    print(f"{CONSTS.YELLOW}{num}{CONSTS.RESET}", end=' ')
                                else:
                                    print(num, end=' ') 
                            print()
                    print('')
                    print('Task deadline set successfully!')
                    print(f'You have {duration} days to finish!')
                    c_m = self._current_m

                    return deadline, c_m 
                else:
                    print('Can not choose a date in the passed')
            except ValueError:
                print(f'Choose a range of days from {self._current_date}th on!')

    def pass_calendar(self):
        return self._chooseDeadline()

    

    


             