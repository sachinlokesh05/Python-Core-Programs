import unittest
# import failure

from moodanalyzer import *


class test_moodAnalyzerFactory(unittest.TestCase):
    

    def test_mood_null(self):
        self.assertRaises(NullMessageException, MoodAnalyzerFactory.MoodAnalyzer(""))

    def test_mood_sad(self):
        reflector = MoodAnalyzerFactory.MoodAnalyzer("i am sad")
        self.assertEqual(reflector, "sad")

    def test_mood_happy(self):
        reflector = MoodAnalyzerFactory.MoodAnalyzer("i am happy")
        self.assertEqual(reflector, "happy")

    def test_argument_error(self):
        self.assertRaises(ParameterError, MoodAnalyzerFactory.MoodAnalyzer(122))


if __name__ == "__main__":
    unittest.main()