import unittest
from userregistration import UserRegistrationUC3


class TestEmail(unittest.TestCase):
    '''

    Invalid Emails (TLD - Top Level Domains)

    '''

    def test_with_out_domain(self):
        result=UserRegistrationUC3('email')
        self.assertEqual(result,False)

    def test_double_atTheRate_is_not_allow(self):
        result=UserRegistrationUC3('abc@abc@gmail.com')
        self.assertEqual(result,False)

    def test_email_only_allow_character_and_digitself(self):
        result=UserRegistrationUC3('abc()*@gmail.com')
        self.assertEqual(result,False)
    
    def test_TDD_can_not_start_with_dot(self):
        result=UserRegistrationUC3('abc123@.com')
        self.assertEqual(result,False)
    
    def test_TDD_can_not_end_with_dot(self):
        result=UserRegistrationUC3('abc123.@.com')
        self.assertEqual(result,False)
    
    def test_emails_1st_character_can_not_start_with(self):
        result=UserRegistrationUC3('.abc@abc.com')
        self.assertEqual(result,False)

    def test_email_double_dots_are_not_allow(self):
        result=UserRegistrationUC3('abc..2002@gmail.com')
        self.assertEqual(result,False)

    def test_emails_TDD_which_has_two_characters_can_not_contains_digit(self):
        result=UserRegistrationUC3('abc@gmail.com.1a')
        self.assertEqual(result,False)

    def test_cannont_have_multiple_emails_TDD(self):
        result=UserRegistrationUC3('abc@gmail.com.1a')
        self.assertEqual(result,False)

    def test_last_TDD_must_contains_at_least_two_characters(self):
        result=UserRegistrationUC3('abc123@gmail.aa')
        self.assertEqual(result,False)

    '''

    Valid Emails

    '''

    def test_valid_email_type1(self):
        result=UserRegistrationUC3('abc@yahoo.com,')
        self.assertEqual(result,True)

    def test_valid_email_type2(self):
        result=UserRegistrationUC3('abc-100@yahoo.com,')
        self.assertEqual(result,True)

    def test_valid_email_type3(self):
        result=UserRegistrationUC3('abc.100@yahoo.com')
        self.assertEqual(result,True)

    def test_valid_email_type4(self):
        result=UserRegistrationUC3('abc-100@abc.net,')
        self.assertEqual(result,True)

    def test_valid_email_type5(self):
        result=UserRegistrationUC3('abc.100@abc.com.au')
        self.assertEqual(result,True)

    def test_valid_email_type6(self):
        result=UserRegistrationUC3('abc@1.com,')
        self.assertEqual(result,True)

    def test_valid_email_type7(self):
        result=UserRegistrationUC3('abc@gmail.com.com')
        self.assertEqual(result,True)

    def test_valid_email_type18(self):
        result=UserRegistrationUC3('abc+100@gmail.com')
        self.assertEqual(result,True)
    
if  __name__ == "__main__":
    unittest.main()