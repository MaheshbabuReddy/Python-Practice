def isornotprime(n):
    if n<=1:
        return False
    if n>1:
      for i in range(2,int(n/2)+1):
         if n%i==0:
            return False
    return True
         
n=int(input("Enter the number"))
x=isornotprime(n)
print(x)