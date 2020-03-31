import random 
'''
randint():-To generate random number in given range

'''
class diceRoll:
    print(random.randint(0,2))

    def __init__(self, *args, **kwargs):
        pass

    def getDiceFrom_OneToTwo(self):
        return random.randint(1,6)

    def toFind_FiverandomNum_avg(self):
        diceValue=[]
        ran=0
        __N=4
        i=0
        while i<=__N:
            ran=random.randint(1,7)
            diceValue.append(ran)
            i+=1
        print(diceValue)
        return (sum(diceValue) / float(len(diceValue)))
    

dice=diceRoll()
print(dice.getDiceFrom_OneToTwo())
print(dice.toFind_FiverandomNum_avg())