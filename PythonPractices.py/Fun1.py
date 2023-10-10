def SumevenOdd(n):
     s1=0
     s2=0
     for i in range(0,n+1):
        if i%2==0:
            s1=s1+i
        
        else:
          s2+=i
     return s1 ,s2
n=int(input("Enter the number"))
result=SumevenOdd(n)
print(result)
            
