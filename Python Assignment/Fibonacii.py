'''
fibonacci = lambda n, a=0, b=1 :a if n==0 else fibonacci(n-1,b,a+b)
print(fibonacci(5))
'''
'''
fib = lambda n, seq=[0,1] : seq if n ==0 else fib(n-1,seq+[seq[-1]+seq[-2]])
print(fib(2)) 
'''
'''
def fib(n):
    seq =[0,1]
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(4))
'''
def fib(n,seq=[0,1]):
    if n < 1:
        return seq
    else:
        seq.append(seq[-1]+seq[-2])
        return fib(n-1,seq)
print(fib(3))