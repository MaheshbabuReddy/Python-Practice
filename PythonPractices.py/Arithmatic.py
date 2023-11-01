class Arithmatic:
    def __init__(self,num1,num2,result):
        self.num1=num1
        self.num2=num2
        self.result=result
    def add(self):
        self.result=self.num1+self.num2
        print(self.result)
    def sub(self):
        self.result=self.num1-self.num2
        print(self.result)
    def mul(self):
        self.result=self.num1*self.num2
        print(self.result)
    def div(self):
        self.result=self.num1//self.num2
        print(self.result)
    def module(self):
        self.result=self.num1%self.num2
        print(self.result)
num1=int(input("Enter the Number1"))
num2=int(input("Enter the Number2"))
result=0
mahesh=Arithmatic(num1,num2,result)
mahesh.add()
mahesh.sub()
mahesh.mul()
mahesh.div()
mahesh.module()
        
