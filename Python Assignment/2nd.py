list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
left_diagnal= []
right_diagnal=[]
for i in range(len(list_of_lists)):
     left_diagnal.append(list_of_lists[i][i])
total_sum = sum(left_diagnal)
print(total_sum)
for i in range(len(list_of_lists)):
        right=list_of_lists[i][3-i]
        right_diagnal.append(right)
total_sum2=sum(right_diagnal)
print(total_sum2)
if total_sum==total_sum2:
     print("The  Sum of two diagnals are  equal")
else:
     print("The Sum of two diagnals are not equal ")