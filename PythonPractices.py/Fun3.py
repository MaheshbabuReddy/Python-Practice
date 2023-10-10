def IsArmornot():
    x=input("Enter the numbeer")
    l=len(x)
    sum=0
    temp=int(x)
    while(x>1):
        rev=x%10
        sum=sum+(rev**l)
        x=x//10
    if(sum==temp):
        return True
    else:
        return False
result=IsArmornot()
print(result)


