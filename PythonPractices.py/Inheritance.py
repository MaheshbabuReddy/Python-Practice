class Account:
    def __init__(self,persons,Amount,Pansion):
        self.persons=persons
        self.Amount=Amount
        self.Pansion=Pansion
    def pension(self):
        self.Pansion=self.Amount/self.persons
        print(self.Pansion,"will be credited in all Pansion Accounts")
persons=int(input("Enter the numbers of persons"))
Amount=int(input("Enter the amount"))
Pansion=0
CM= Account(persons,Amount,Pansion)
CM.pension()


        