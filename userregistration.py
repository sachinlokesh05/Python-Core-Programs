# -*- coding: utf-8 -*-


'''

As a User need to
enter a valid First
Name
- First name starts with Cap and has
minimum 3 characters

'''
import re as r

def UserRegistrationUC1(username):
    __pattern = r.compile(r'[A-Z]\w{3}\w*$')
    
    ismatched =__pattern.match(username)
    if ismatched :
        return True
    else:
        return False



'''

As a User need to
enter a valid Last
Name
- Last name starts with Cap and has
minimum 3 characters

'''

def UserRegistrationUC2(username):
    __pattern = r.compile(r'[A-Z]\w{3}\w*\s[A-Z]\w{3}\w*$')
    
    ismatched =__pattern.match(username)
    if ismatched :
        return True
    else:
        return False

'''

As a User need to
enter a valid email
- E.g. abc.xyz@bl.co.in
- Email has 3 mandatory parts (abc, bl
& co) and 2 optional (xyz & in) with
precise @ and . positions

'''

def UserRegistrationUC3(email):
    __pattern = r.compile(r'[A-Za-z]+[\.\-\+]?[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2}[A-Za-z]*\.?(?=[^\d])\w*\,?$')
    
    ismatched =__pattern.match(email)
    if ismatched :
        return True
    else:
        return False


'''

As a User need to
follow pre-defined
Mobile Format
- E.g. 91 9919819801
- Country code follow by space and 10
digit number

'''

def UserRegistrationUC4(phone_number):
    __pattern = r.compile(r'91\s[1-9]\d{9}')
    
    ismatched =__pattern.match(phone_number)
    if ismatched :
        return True
    else:
        return False
    

'''
As a User need to
follow pre-defined
Password rules.
Rule1 – minimum 8 Characters
 - NOTE – All rules must be passed.
'''

def UserRegistrationUC5(password):
    __pattern = r.compile(r'\w{8}\w*')
    
    ismatched =__pattern.match(password)
    if ismatched :
        return True
    else:
        return False
    

'''

Rule2 – Should
have at least 1
Upper Case
- NOTE – All rules must be passed

'''


def UserRegistrationUC6(password):
    __pattern = r.compile(r'[A-Z]\w{7}\w*')
    
    ismatched =__pattern.match(password)
    if ismatched :
        return True
    else:
        return False


'''

Rule3 – Should
have at least 1
numeric number in
the password
- NOTE – All rules must be passed

'''

def UserRegistrationUC7(password):
    __pattern = r.compile(r'[A-Z][0-9]+\w{6,7}\w*')
    
    ismatched =__pattern.match(password)
    if ismatched :
        return True
    else:
        return False


'''

Rule4 – Has exactly
1 Special Character
- NOTE – All rules must be passed

'''

def UserRegistrationUC8(password):
    __pattern = r.compile(r'^(?=.*[\d])(?=.*[A-Z])[@][a-zA-Z\d]{6,}$')
    
    ismatched =r.match(__pattern,password)
    if ismatched :
        return True
    else:
        return False

