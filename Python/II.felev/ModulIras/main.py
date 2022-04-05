from elsoModulom import sum1, prod1
from sys import path

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))

#Modul betöltése a fő klönyvtárba

path.append('..\\modules')
