n =int(input('Enter a number')) 
if n % 2 != 0:  # n is odd
        print("Weird")
elif n % 2 == 0 and 2 < n <= 5:  # n is even and in the inclusive range of 2 to 5
        print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # n is even and in the inclusive range of 6 to 20
        print("Weird")
elif n % 2 == 0 and n > 20:  # n is even and greater than 20
        print("Not Weird")
