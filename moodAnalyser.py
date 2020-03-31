#!/usr/bin/env python

class MoodAnalyser:

    def __init__(self, mood=None):
        self.mood=mood
    
    # '''

    #         Given a Message,
    #     ability to analyse and
    #     respond Happy or Sad
    #     Mood
    #     UC 1
    #     - Create MoodAnalyser Object
    #     - Call analyseMood function with message as
    #     parameter and return Happy or Sad Mood


    # '''

    # def analyseMood(self):

    #     if self.mood.__contains__('Sad'): return "Sad"
    #     else: return "Happy"



    # '''

    # Refactor the code to take
    # the mood message in
    # Constructor
    # Refactor
    # - Note:
    # - MoodAnalyser will have a message Field
    # - MoodAnalyser will have 2 Constructors –
    #     Default - MoodAnalyser() and with
    #     Parameters – MoodAnalyser(message)
    # - analyseMood method will change to
    # support no parameters and use message
    # Field defined for the Class

    # '''

    # def analyseMood(self,mood=None):
    #     if self.mood is None:

    #         if mood.__contains__('Sad'): return "Sad"
    #         else: return "Happy"

    #     if self.mood.__contains__('Sad'): return "Sad"
    #     else: return "Happy"


    '''

    Handle Exception if
    User Provides
    Invalid Mood
    - Like NULL

    '''
    ''' NOTE: there is no null in python,insted,there is None,the equivalent of the null keyword in python is none '''

    def analyseMoodUC1(self):
        try: 
            if self.mood.__contains__("Sad") : return "Sad"
        except Exception :
            return "Happy"


if __name__ == "__main__":
    a=MoodAnalyser("Sad").analyseMoodUC1()
    print(a)
