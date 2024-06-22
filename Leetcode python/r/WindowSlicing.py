def window_space(arr, k):
    window_sum = sum(arr[:k])
    result = [window_sum]
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        result.append(window_sum)
    return result

arr = [2, 3, 1, 2, 4, 1, 2, 2, 3]
k = 3
print(window_space(arr, k))