Array = [1,3,4,5,2,3]
result = []
key = int(input("Enter the Number"))
for i in range(len(Array)):
    for j in range(len(Array)):
        if i != j and Array[i] + Array[j] == key:
            res = [Array[i], Array[j]]
            result.append(res)
for pair in result:
    print(pair)
