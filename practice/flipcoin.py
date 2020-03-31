import random

def flip_coin(number):
        #generated a list that consists of coin flip value
        toss = [ random.randint(0,1) for _ in range(number) ]

        #percantage calculation 
        head =  toss.count(1) * 100 / number

        return (toss,head)

a=flip_coin(10)
print(a)