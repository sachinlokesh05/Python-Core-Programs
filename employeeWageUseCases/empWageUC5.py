import random as ra
class empWage:
    
    def __init__(self, *args, **kwargs):
        self.__empRatePerDay = 20
        self.__totalWrkDay = 20
    

    def empWagePerDay(self):

        IS_FULLTIME = 2
        IS_PARTTIME = 1
        empWrkHr = None
        empCheck = ra.randint(0,2)

        if empCheck == IS_FULLTIME :  empWrkHr = 8
        elif empCheck == IS_PARTTIME :  empWrkHr = 4
        else : empWrkHr = 0
        
        return empWrkHr

    def CalculateTotalSalary(self):

        Salary = 0 
        totalSalary = 0
        i = 0
        while i <= self.__totalWrkDay - 1:
            empWrkhr = self.empWagePerDay()
            Salary = (empWrkhr * self.__empRatePerDay)
            totalSalary += Salary
            i+=1

        return totalSalary

emp=empWage()
totalsalary=emp.CalculateTotalSalary()
print('total employee per month is {}'.format(totalsalary))