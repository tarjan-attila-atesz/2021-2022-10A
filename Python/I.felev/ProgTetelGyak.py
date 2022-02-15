#Hozz létre 10-30 közötti véletlenszámokból egy 30 elemű listát! 
#Ez a vendéglőd elmúlt hónapjának forgalma, 
#az az ennyi vendéged volt az egyes napokon.

#FA01: Határozd meg, egy hónapban összesen hány vendéged volt?
#FA02: Volt-e olyan nap, amikor teltházad volt (tehát 30 vendég volt 1 napon)
#FA03: Mekkora volt a legkisebb vendégszámod?
#FA04: Mekkora volt a legnagyobb vendégszámod?
#FA05: Hanyadik napon volt teltház a vendéglőben?

from random import randint
vendegloHavi =[]
for i in range(30):
    vendegloHavi.append(randint(10,30))

#####################
#FA01
osszeg = 0
for i in vendegloHavi:
    osszeg += i
print("Összesen ",osszeg," vendég volt egy hónapban!")
x = 0
#FA02
while x < len(vendegloHavi) and vendegloHavi[x] != 30:
    x = x+1
if(x<len(vendegloHavi)):
    print("Volt teltház a vendéglőben!")
else:
    print("Nem volt teltház a vendéglőben")
#FA03-04
print("A legkisebb vendégszám: ",min(vendegloHavi))
print("A legnagyobb vendgszám: ",max(vendegloHavi))
#FA05
while x < len(vendegloHavi) and vendegloHavi[x] != 30:
    x = x+1
if(x<len(vendegloHavi)):
    print("A",x+1,"-ik napon volt teltház a vendéglőben!")



