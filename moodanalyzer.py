# define Python user-defined exceptions
class NullMessageException(Exception):
   """Raised when the input value null"""
   def __str__(self):
    return "Null message exception"


class ParameterError(Exception):
   """Raised when the incorrect argument is passed to the constructor"""
   def __str__(self):
    return "Parameter type exception"

class MoodAnalysisException(Exception):
   """Raised when the incorrect argument is passed to the constructor"""
   def __str__(self):
    return "No Such class exception"


class MoodAnalyzerFactory:

    def __init__(self, mood=None, reflection=None):
        self.mood = mood
        self.reflection = reflection

    @staticmethod
    def MoodAnalyzer(mood):
        reflection = None
        # print(mood)
        try:
            if mood == "":
                raise NullMessageException
            elif not type(mood) == str:
                raise ParameterError
            elif mood.__contains__("sad"):
                reflection = "sad"
            elif mood.__contains__("happy"):
                reflection = "happy"
            else:
                reflection = "happy"
            return reflection
        except NullMessageException as f:
            # print("Null message, try again!")
            print(f)
        except ParameterError as e:
            # print("No Such Method Error")
            print(e)


if __name__ == "__main__":
    
    msg = input('enter the msg: ')
    # msg = 123
    try:
        m = MoodAnalyzerFactory
        # m.MoodAnalyzer(12)
        mood = m.MoodAnalyzer(msg)
        if mood is not None:
            print(mood)
    except NameError:
        print("No such Class Error")
