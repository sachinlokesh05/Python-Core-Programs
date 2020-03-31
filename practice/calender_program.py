class Calender:
    
    def __init__(self, *args, **kwargs):
        self.__day=("sunday",'monday','tuesday','wednesday','thursday','friday','saturday')

    
    def find_which_Day(self,y,m,d):
        y_ = (y - (14 - m) // 12)
        x= y_ + y_ /4 - y_ // 100 + y_ // 400
        m_ = m + 12 * ((14 - m) // 12) - 2
        d_ = (d + x + 31 * m_ // 12) % 7

        return self.__day.__getitem__(d_)


cal=Calender()
a=cal.find_which_Day(1996,7,18)
print(a)