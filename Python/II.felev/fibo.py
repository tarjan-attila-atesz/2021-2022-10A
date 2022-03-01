def fib(n):
    if n < 1:
        return None
    if n < 2:
        return 1

    elem_1 = elem_2 = 1
    osszeg = 0
    for i in range(3, n + 1):
        osszeg = elem_1 + elem_2
        elem_1, elem_2 = elem_2, osszeg
    return osszeg


for n in range(1, 10):  
    print(n, "->", fib(n))

