import pytest
from userregistration import UserRegistrationUC3

list_email = (

    ('abc@yahoo.com,',True),
    ('abc-100@yahoo.com,',True),
    ('abc',False),
    ('abc@yahoo.com,',True),
    ('abc-100@yahoo.com,',True),
    ('abc.100@yahoo.com,',True),
    ('abc111@abc.com,',True),
    ('abc-100@abc.net,',True),
    ('abc.100@abc.com.au,',True),
    ('abc@1.com,',True),
    ('abc@gmail.com.com,',True),
    ('abc+100@gmail.com,',True),
    ('abc',False),
    ('abc@.com.my',False),
    ('abc123@gmail.a',False),
    ('characters',False),
    ('abc123@.com',False),
    ('abc123@.com.com',False),
    ('.abc@abc.com',False),
    ('abc(,False)*@gmail.com',False),
    ('abc@%*.com',False),
    ('abc..2002@gmail.com',False),
    ('1abc.@gmail.com',False),
    ('1abc@abc@gmail.com',False),
    ('1abc@gmail.com.1a',False),
    ('abc+100@gmail.com',True),
)

@pytest.mark.parametrize("email_input,expected_output",list_email)
def test_email_from_file(email_input,expected_output):
    result = UserRegistrationUC3(email_input)
    assert  result == expected_output