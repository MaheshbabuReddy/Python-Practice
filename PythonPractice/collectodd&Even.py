n=int(input("no."))
result1 = 0
result2 = 1 
for i in range( 1, n+1):
   if i % 2 == 0:
      result1=result1 + i
      print(result1, end=" ")
   if i % 2 != 0:
      result2=result2 * i
      print(result2)
      
       