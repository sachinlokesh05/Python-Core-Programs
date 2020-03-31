import random
class employeeWage:
    def __init__(self):
        self.__employeeWage = 20 
        self.__FULL_TIME = 2
        self.__ABSENT = 0
        self.__PART_TIME = 1

    
    def Calculate_EmpDailyWage(self):
        empCheck = random.randint(0,3)
        empWorkingHr = None

        if empCheck is self.__FULL_TIME:  empWorkingHr = 8
        elif empCheck is self.__PART_TIME:  empWorkingHr = 4
        else :  empWorkingHr=0

        Salary=empWorkingHr*self.__employeeWage
        return Salary
        
emp=employeeWage()
print(emp.Calculate_EmpDailyWage())