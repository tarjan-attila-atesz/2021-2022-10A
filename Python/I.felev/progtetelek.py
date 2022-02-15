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
#számítsuk a jegyek összegét, átlagát, és azt, hogy hány bukás volt!


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

#Határozzuk meg, hogy van-e 3-as az adatsorban. (Eldöntés tétele)
x = 0
while x < len(jegyek) and jegyek[x] != 3:
    x = x+1
if(x<len(jegyek)):
    print("Van 3-as az adatsorban.")
else:
    print("Nincs 3-as az adatsorban.")

#Mekkora a legnagyobb és legkisebb érték az adatsorban. (Min és Max tétel)
#Megoldás#1
print("A legkisebb érték: ",min(jegyek))
print("A legnagyobb érték: ",max(jegyek))
#Megoldás2 - Min és max tétellel


minElem = jegyek[0]
for legkisebbElem in jegyek:
    if legkisebbElem < minElem:
        minElem = legkisebbElem
print("Minimuma: ",minElem)

maxElem = jegyek[0]
for legnagyobbElem in jegyek:
    if legnagyobbElem > maxElem:
        maxElem = legnagyobbElem
print("Maximum: ",legnagyobbElem)

#Van e az adatsorozatomban 1-es, ha igen, akkor hol található?
keresettErtek = 1

x = 0
while x < len(jegyek) and jegyek[x] != keresettErtek:
    x = x+1
if(x<len(jegyek)):
    print("Van ilyen elem az ",x+1," helyen")
    print(jegyek)
else:
    print("Nincs ilyen elem.")