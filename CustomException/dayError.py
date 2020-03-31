class Error(Exception): 
  
    # Error is derived class for Exception, but 
    # Base class for exceptions in this module 
    pass

class DateError(Error):
    def __int__(self,*kwargs):
        self.message=kwargs

    def __str__(self):
        if self.message :
            return "You have entered wrong date: "+ self.message + "\nDate should be less then 31"
        else : return "Date should be less then 31"
    

