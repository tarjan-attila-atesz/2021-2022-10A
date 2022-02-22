def oszegzo(lista):
    osszeg = 0
    for szam in lista:
        osszeg = osszeg +szam
    return osszeg

aktlista = [1,2,3,4,5,6,7,8,9,10]
print(oszegzo(aktlista))