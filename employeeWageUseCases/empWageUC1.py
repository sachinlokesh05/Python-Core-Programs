import random 
import sys
sys.path.append('/home/admin123/Desktop/EmployeeWagePrograms/CustomException/')
from dayError import DateError
class employeeWageUC1:
    def __init__(self):
        self.__employeeWage = 20 
        self.__FULL_TIME = 2
        self.__ABSENT = 0
        self.__PART_TIME = 1
        self.month=['march','april','may','june']
        
    def empPresentOrNot(self):
        empCheck=random.randint(0,2)
        if empCheck is self.__FULL_TIME: return "full time employee"
        elif empCheck is self.__PART_TIME: return "part time employee"
        else : return "empolyee is absent today"
    
    # def Calculate_EmpDailyWage(self):
    #     empCheck = random.randint(0,3)
    #     empWorkingHr = None

    #     if empCheck is self.__FULL_TIME:  empWorkingHr = 8
    #     elif empCheck is self.__PART_TIME:  empWorkingHr = 4
    #     else :  empWorkingHr=0

    #     Salary=empWorkingHr*self.__employeeWage
    #     return Salary

    
emo=employeeWageUC1()

print(emo.empPresentOrNot())