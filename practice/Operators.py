class Operators:
    a=None
    b=None
    c=None
    def __init__(self, a,b,c):
        self.__aa=a
        self.__bb=b
        self.__cc=c
    
    def operation(self):
        choice=int(input("enter choice of your: "))
        if choice == 1:
            return (self.__aa + self.__bb * self.__cc)
        elif choice == 2:
            return (self.__cc + self.__aa / self.__cc)
        elif choice == 3:
            return (self.__aa % self.__bb + self.__cc)
        elif choice == 4 :
            return (self.__aa * self.__bb + self.__cc)
        else:
            print("Wrong choice")
            return self.operation()



ap=Operators(1,2,5)
print('''
1. a + b * c
3. c + a / b
2. a % b + c
4. a * b + c
''')
print(ap.operation())
    
    