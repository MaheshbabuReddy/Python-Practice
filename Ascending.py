lst = [10,3,43,2,5]
for ele in range(len(lst)-1):
    for ele2 in range(len(lst) -1 -ele):
        if lst[ele2] > lst[ele2+1]:
           x =lst[ele2] ,lst[ele2+1] = lst[ele2+1] , lst[ele2]
           
        print(lst)    