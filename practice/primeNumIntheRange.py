class PrimeNumber:   
    def is_prime(self,num):
        if num > 1:
    # check for factors
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    break
            else:
                self.__primeNumber(n=num)
        
        # if input number is less than
        # or equal to 1, it is not prime
        else:
            print(num,"is not a prime number")

    def __primeNumber(self,n):
            count = 0
            for i in range (1,n):
                if i>1:
                    for j in range (2,i):
                        if i%j==0:
                            break
                    else:
                        count+=1
                        print(i,end=" ")
                        

if __name__ == "__main__":
    prime = PrimeNumber()
    num=int(input("enter your number: "))
    prime.is_prime(num)
