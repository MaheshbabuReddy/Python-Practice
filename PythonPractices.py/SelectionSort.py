l1=[20,12,43,22,23,5,3]
for index in range(len(l1)):
    mid_value=index
    for i in range(index+1,len(l1)):
        if l1[mid_value]>l1[i]:
         (l1[i], l1[index]) = (l1[index], l1[i])
print(l1)
