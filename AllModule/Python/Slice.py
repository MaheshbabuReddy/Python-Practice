l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
my_dict = {}

for i in range(len(l2)):
    temp = []
    for j in range(len(l1)):
        mul = l1[j] * l2[i]
        temp.append(int(str(mul)[:4]))
    l3.append(temp)
print("Sublist the L3 list ")
for sublist in l3:
    print(sublist)

for id in range(len(l3)):
    sublist_sum = sum(l3[id])
    key = f"Sum{id + 1}"
    my_dict[key] = sublist_sum

print("Sums of each sublist:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")






    