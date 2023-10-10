week=['sunday','Monday','Tuesday','Wednesday','Thursaday','Friday','Saturday']
sum=0
for day in week:
    Attendence=input(f"Enter the {day} Attendence[P/A]:")
    print(Attendence)
    if Attendence=="P":
        Payment=int(input("Enter the day Payment:"))
        sum=sum+Payment
        print(sum)
                    
        
        
        


