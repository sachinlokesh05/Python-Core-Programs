def leapyear(year):
        
        if year >= 1582 and len(str(year)) == 4:
            
            if (year%4 == 0 and year % 100 != 0) or year %400  == 0:
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    year=int(input("enter year: "))
    is_leapyear=leapyear(year)
    print(is_leapyear)
