class Error(Exception): 
  
    # Error is derived class for Exception, but 
    # Base class for exceptions in this module 
    pass

class Exception_custom(Exception):
    pass

class MoodanalyserException(Exception_custom):
    def __int__(self,*kwargs):
        self.message=kwargs

    def __str__(self):
        return "Mood should not be Null or Empty"
    


