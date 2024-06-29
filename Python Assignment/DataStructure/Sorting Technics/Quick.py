def QuickSort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle =[x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return  QuickSort(left) + middle + QuickSort( right)
    
arr = [4,2,1,34,12,30]
print(QuickSort(arr))


'''
def QuickSort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [4, 2, 1, 34, 12, 30]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
'''