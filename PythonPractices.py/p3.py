Bahu=int(input("Enter num"))
Balla=int(input("Enter num"))
Katapa=int(input("Enter num"))
if Bahu>Balla and Bahu>Katapa:
    print("Bahu is the King")
elif Balla>Katapa:
    print("Balla is king")
elif Katapa>Bahu or Katapa>Balla:
    print("As per Katapa wish Bahu wanted to be King")
    print("So Katapa wanted his  50 persons of kills  to Bahu ")
    Add_Kill=Katapa*50//100+Bahu
    print(Add_Kill)
else:
    print("Bahu is king of Mahishmati:Add_kill")  