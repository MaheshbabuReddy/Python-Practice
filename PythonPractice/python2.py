fnumber =int(input())
lnumber =int(input())
for num in range(fnumber,lnumber+1):
    if num > 1:
        for i in range(2, num):
          if num % i == 0:
           break 
        else:
         print(num)
                   
