def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


s = 0
i = 2
while True:
    f = fib(i)
    if f > 4000000:
        break
    if f % 2 == 0:
        s += f
    i += 1
    
print(s)