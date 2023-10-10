def power(x, n):
    if n == 1:
        return x
    else:
        y = x * power(x, n-1)
        return y

x = int(input('Enter a number: '))
n = int(input('Enter the power of x: '))
print(power(x, n))
