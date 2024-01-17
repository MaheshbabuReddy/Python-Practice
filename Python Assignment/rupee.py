money=[1,2,5,10,20,50,100,500,1000]
rupee=48
n=9
for i in range(n-1,-1,-1):
    while(rupee>=money[i]):
        rupee-=money[i]
        print(money[i])
