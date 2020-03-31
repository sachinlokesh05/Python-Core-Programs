import random
class empWage:
    
    def __init__(self, *args, **kwargs):
        self.__employeeWage = 20 
        self.__FULL_TIME = 2
        self.__ABSENT = 0
        self.__PART_TIME = 1
        self.__empRatePerDay = 20
        self.__maxempWrkHr = 40
        self.__maxempWrkDays = 20


    def employeeCheck(self):
        empWrkHr = 0
        empCheck = random.randint(0,2)
        if empCheck  ==  self.__FULL_TIME:empWrkHr = 8
        elif empCheck  ==  self.__PART_TIME:empWrkHr = 4
        else :
            empWrkHr = 0  
        return empWrkHr

    def monthVice_Salary(self):
        
        salary_record_dict=dict()
        print(type(salary_record_dict))
        totalWrkDay = 0 
        totalWrkHr = 0
        salary = 0
        totalSalary = 0

        while (totalWrkDay <= self.__maxempWrkDays and totalWrkHr <= self.__maxempWrkHr):
            totalWrkDay += 1
            empwrkhr  =  self.employeeCheck()
            totalWrkHr += empwrkhr
            salary = (empwrkhr*self.__empRatePerDay)
            salary_record_dict[totalWrkDay]=salary # Python Dictionaries 
            totalSalary += salary
        print(salary_record_dict)
        return totalSalary


emp = empWage()
print(emp.monthVice_Salary())