class Person:
    def __init__(self, n, a, acc, I, r, y):
        self.Intrest = I
        self.rate = r
        self.year = y
        self.name = n
        self.Account = acc
        self.Amount = a

    def getdata(self):
        print('My Account name is', self.name, 'and ID', self.Account,
              'Bank Money Deposited by', self.name, 'credit', self.Amount, '.')

    def calculate(self):
        self.Intrest = self.Amount * self.rate * self.year / 100
        self.Intrest+=self.Amount
        print('The Interest of Amount after', self.year, 'years is', self.Intrest, '.')


n = input('Enter your name: ')
acc = int(input('Enter the account number: '))
a = int(input('Enter the Amount: '))
r=int(input('Enter Rate'))
y=int(input("Enter the year"))
I=0

# The last three arguments (I, r, y) are not used, so we can set them to 0.
P = Person(n, a, acc,I, r, y)

P.getdata()
P.calculate()


        
        
