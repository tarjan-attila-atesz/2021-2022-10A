#Osszegzés tétele

osszeg = 0
osszegzoLista = [1,2,3,4,5]

for i in osszegzoLista:
    osszeg = osszeg + i
print("A lista összege: ",osszeg," elemszáma: ",len(osszegzoLista))
print("A lista tartalma: ",osszegzoLista)

#megszámlálás tétele

megszamolLista=[10,20,25,45,46,59] #6os lottó nyerőszámait

parosSzamok = 0

for i in megszamolLista:
    if(i%2==0):
        parosSzamok += 1
print("Páros számok: ",parosSzamok)

## Játékos feladatok
#Tároljuk el egy jegyek listában, a programozás félévi jegyeket
#számítsuk a jegyek összegét, átlagát, és azt, hogy hány bukás volt


from random import randint
jegyek =[]
for i in range(22):
    jegyek.append(randint(1,5))
print(jegyek)
osszeg2 = 0
bukasokSzama = 0
for i in jegyek:
    osszeg2 = osszeg2 + i
    if(i==1):
        bukasokSzama +=1
print(osszeg2)
print(bukasokSzama)





