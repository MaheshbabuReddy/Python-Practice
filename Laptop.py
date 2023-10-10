Laptops = []
n = int(input("Enter the number of Laptops: "))
good_Laptop = []
bad_laptop = []

for i in range(n):
    laptop = input('Enter the Name of Laptop: ')
    status = input("Enter the Status of Laptop (good/bad): ")
    Laptops.append({"name": laptop, "Status": status})
    
    print(Laptops)

for lapps in Laptops:
    if lapps["Status"] == "good":
        good_Laptop.append(lapps["name"])
        print("Good Conditional Laptops are:",good_Laptop)
    else:
        bad_laptop.append(lapps["name"])

print("Bad Conditional Laptops are:",bad_laptop)

    


