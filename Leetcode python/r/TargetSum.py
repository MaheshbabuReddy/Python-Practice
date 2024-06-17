def kadd(arr,targets):
    result = 0
    dic = {}
    for index,ele in enumerate(arr):
       result = targets - ele
       if result  not in dic:
        dic[result] = index
       else:
        return [result,ele]
arr = [1,3,1,2,5,9]
target = 9
print(kadd(arr,target))