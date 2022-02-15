#Hozzuk létre a numbers névre hallgató listát az alábbi számokkal: 111, 7, 2, 1. 
#Kérdezzük le a lista elemszámát, milyen adatok vannak benne?

numbers = [111, 7, 2, 1]
print("Lista elemszáma: ", len(numbers))
print("Lista tartalma: ", numbers)

#Adjuk hozzá a 4-es számot a lista végére! Kérdezzük le az elemszámot majd a tartalmát!
numbers.append(4)

print("Lista elemszáma: ", len(numbers))
print("Lista tartalma: ", numbers)

#A lista elejére szúrjuk be a 222-es számot. Kérdezzük le az elemszámot majd a tartalmát!

numbers.insert(0, 222)
print("Lista elemszáma: ", len(numbers))
print("Lista tartalma: ", numbers)

################################################################################################
#Töltsünk fel egy üres listát For ciklus használatával, majd írjuk ki az elemszámát és tartalmát!
ures_lista = [] 

for i in range(5):
    ures_lista.append(i + 1)
print("A lista elemszáma: ",len(ures_lista))
print("A lista tartalma: ",ures_lista)

############################################################
#random

from random import random 
for i in range(5): 
    print(random()) 

from random import randint
for i in range(10):
    print(randint(0,2), end=" ")





