def Twopointers(arr):
    i = 0
    j = len(arr)-1
    result = []
    sum = 0 
    while i < j:
        sum = arr[i]+arr[j]
        result.append(sum)
        i+=1
        j-=1
    return result
arr = [1,3,1,2,5,9]
print(Twopointers(arr))