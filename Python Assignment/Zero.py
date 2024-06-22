arr= [2,0,0,1]
nonZero =0
j=0
while j < len(arr):
        if arr[j] != 0:    
            arr[j],arr[nonZero]= arr[nonZero],arr[j]
            nonZero +=1
        j+=1
            
print(arr)