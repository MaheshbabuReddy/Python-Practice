age=int(input("Enter the Age"))
gender=input("Enter the male/female")
amount=int(input("Enter the Amount you deposited"))
years=int(input("Number of years"))
if age>60:
    if gender=="female":
        rate=0.08
    else:
        rate=0.075
if age<60:
      rate=0.06  
print("Calculate the Insterest of 5 years")
Intrest=amount+rate+years
Intrest+=amount
print(Intrest)