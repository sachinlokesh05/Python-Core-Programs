# import urllib.request
import re as r
class ListOfEmailTest:
    def __init__(self, filename):
        #opening the file
        self.__filename=open(filename,'r')

    
    def checkEmail(self):
        a = []
        email_data = self.__filename.readlines()
        # abc=['abc@yahoo.com,','abc-100@yahoo.com,','abc.100@yahoo.com','abc111@abc.com,','.abc@abc.com']
        for i in email_data:
            #checking maid id is vaid or not
            if r.match(r'[A-Za-z]+[\.\-\+]?[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2}[A-Za-z]*\.?(?=[^\d])\w*\,?$',i.strip()):
                #adding valid email id to list
                a.append(i.strip())
        return a
        f.close()
list_email = ListOfEmailTest('emails.txt').checkEmail()
print(list_email)
