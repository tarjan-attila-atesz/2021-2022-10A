def fibo2(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibo2(n-1)+fibo2(n-2)


print(fibo2(10))

