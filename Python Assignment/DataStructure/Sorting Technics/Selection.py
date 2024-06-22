def selection_sort(arr1):
    n = len(arr1)
    for i in range(n):    
        min_index = i      
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j     
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr1

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
