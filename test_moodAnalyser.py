#!/usr/bin/env python

import unittest
from moodAnalyser import MoodAnalyser
import failure   
class test_moodAnalyser(unittest.TestCase):

    # def setUp(self):
    #     pass
    
    

    # def test_Mood_function_return_Happy_or_Sad_Mood_UC1(self):
    #     result=MoodAnalyser().analyseMood("Happy")
    #     self.assertEqual(result,'Happy') 



    # '''

    # Given “I am in Sad
    # Mood” message
    # Should Return SAD
    # TC 1.1
    # analyseMood method can just return SAD to
    # pass this Test Case (TC)

    # '''

    # def test_Iam_in_Sad_Mood_message_Should_Return_SAD_TC1_1(self):
    #     result=MoodAnalyser().analyseMood("I am in Sad Mood")
    #     self.assertEqual(result,"Sad")



    # '''

    # Given “I am in Any
    # Mood” message
    # Should Return HAPPY
    # TC 1.2
    # To make the Test case pass analyseMood
    # method need to check for Sad else return
    # HAPPY

    # '''

    # def test_Iam_in_Any_Mood_message_Should_Return_HAPPY_TC1_2(self):
    #     result=MoodAnalyser().analyseMood("I am in Any Mood")
    #     self.assertEqual(result,"Happy")



    # '''

    # Given “I am in Sad
    # Mood” message in
    # Constructor Should
    # Return SAD
    # Repeat TC 1.1
    # To pass this Test Case when calling
    # analyseMood method with no params should
    # return SAD

    # '''

    # def test_Iam_in_Sad_Mood_message_in_Constructor_Should_Return_SAD_Repeat_1_1(self):
    #     result=MoodAnalyser('I am in Sad Mood').analyseMood()
    #     self.assertEqual(result,"Sad")


    # '''

    # Given “I am in Happy
    # Mood” message in
    # Constructor Should
    # Return SAD
    # Repeat TC 1.2
    # To pass this Test Case when calling
    # analyseMood method with no params should
    # return HAPPY

    # '''

    # def test_Iam_in_Any_Mood_message_in_Constructor_Should_Return_HAPPY_Repeat_1_2(self):
    #     result=MoodAnalyser('I am in Happy Mood').analyseMood()
    #     self.assertEqual(result,"Happy")


    '''

    Given Null Mood
    Should Return Happy
    TC 2.1
    To make this Test Case pass Handle NULL
    Scenario using try catch and return Happy

    '''
    
    def test_Given_Null_Mood_Should_Return_Happy(self):
        with self.assertRaises(Exception):
            result = MoodAnalyser().analyseMoodUC1()
            print(result)  
            self.assertEqual(result,"Happy")  



if __name__ == "__main__":
    unittest.main() 