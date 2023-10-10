n1 = int(input("enter the First number of Lower Boundary"))
n2 = int(input("enter the Last number of Upper Boundary"))
s = int(input("Enter Size of Class Intervals"))
class_Intervals=[]
mid_point=[]
frequency=[]
sum_cf=0
N=0
sum_mp=0
cumulative_frequency=[]
for i in range(n1, n2 + 1, s):
    values=(int(str(i)[0:i + s]))
    class_Intervals.append(values)
print(class_Intervals)
for i in range(0,len(class_Intervals)-1):
    f=int(input("enter the frequency:"))
    print("Enter the frequency for",class_Intervals[i],"to",class_Intervals[i+1],"is",f)
    sum_cf+=f
    N+=f
    cumulative_frequency.append(sum_cf)
    m=class_Intervals[i]+class_Intervals[i+1]//2
    sum_mp+=f*m
    mid_point.append(m)
    frequency.append(f)
print(sum_mp)

print("Midpoints",mid_point)
print("Frequency",frequency)
print("class_Intervals",class_Intervals)
print("cumulative_frequency ",cumulative_frequency)
print("------------------------------------------------------------")
print("To find mean")
mean=sum_mp/N
print("Mean is :",mean)
print("To find Median")
median_index = N // 2
median = None
for i in range(len(cumulative_frequency)):
    if cumulative_frequency[i] >= median_index:
        median = mid_point[i]
        break
print("Median is:",median)
print("To find Mode")
max_frequency = max(frequency)
modes = [mid_point[i] for i in range(len(frequency)) if frequency[i] == max_frequency]
print("Mode is:", modes)
print("--------------------------------------------------------------")





