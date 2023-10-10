L1=[[1,3,4,5],[6,7,8,12],[1,4,3,23]]
L2=[[2,7,6,16],[1,8,7,3],[1,5,3,6]]

Add=[]
Mult=[]
print("To perform Addition")
for i in range(0,len(L1)):
    for j in range(0,len(L1[i])):
        Add.append(L1[i][j]+L2[i][j])        
print(Add)
print("To perform Multiplication")
for i in range(0,len(L1)):
    for j in range(0,len(L1[i])):
     Mult.append(L1[i][j]*L2[i][j])     
print(Mult)




        

    
    