'''
Write a program that takes a command-line argument n and prints a table of the
powers of 2 that are less than or equal to 2^n.

'''

import sys
class powerOf2:
    
    def powerof2(self):
        num=int(sys.argv[1])
        i=0        
        print(2**num)
        while i <= num :
            value=2**i
            print(str(2)+" ^ "+str(i)+" = "+ str(value))
            i+=1

pw=powerOf2()
pw.powerof2()