class Mason():
    def __init__(self,w,d,a,t):
      self.worker=w
      self.Days=d
      self.Amount=a
      self.totalAmount=t
    def daysofwork(self):
        self.totalAmount=self.Days*self.Amount
        
        print(self.worker,"He/She has done",self.Days," days of work her/his daily payment is",
                self.Amount,"so total payment of her/his per week is",self.totalAmount,".")
w=input("Enter the name of the worker")
d=int(input("No.of days"))
a=int(input("Enter the amount per day"))
t=0
m=Mason(w, d, a, t)
m.daysofwork()
                
