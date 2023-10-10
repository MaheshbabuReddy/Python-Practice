l=[22,43,56,45,45,23,37,35]
dict={}
for i in l:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
max_val=max(dict.values())
print("Max highest value in dictionary:",max_val)
mode=0
for key, value in dict.items():
    if value == max_val:
        mode=key
print("mode is:",mode)