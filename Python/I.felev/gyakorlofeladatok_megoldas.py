#1) Helló világ: Készíts programot, mely kiírja a képernyőre azt a szöveget, hogy „Hello World”!
print("Hello World!")

#2) Üdvözlés: Készíts programot, amely bekéri a felhasználó nevét, majd üdvözli őt a nevén szólítva!
nev = input("Addja meg a nevét: ")
print("Hello",nev)
#3) Pénzes: Készíts programot, mely bekéri a felhasználótól, hogy a kasszában hány 100, 200 és 500 Ft-os található. A program számolja ki, hogy mennyi a beírt pénz összege!
szazas = int(input("Százasok száma? "))
ketszaz = int(input("Kétszázasok száma? "))
otszaz = int(input("Ötszázasok száma? "))
osszeg = szazas*100 + ketszaz*200 + otszaz*500
print("Összesen: ",osszeg)
#4) Celsius–Fahrenheit: Készíts programot, amely bekér a felhasználótól egy valós számot (Celsius fok), az eredményt átváltja Fahrenheit értékbe, és kiírja az eredményt a képernyőre (0°C=32°F, 40°C=104°F, lineáris)! Írd meg ugyanezt fordítva is!
Farenheit = int(input("Mennyi Farenheit értéke? "))
Celsius = (Farenheit - 32) * 5.0/9.0
Celsuis2 = int(input("Mennyi Celsius értéke? "))
Fahrenheit2 = 9.0/5.0 * Celsius + 32
print("Farenheitből Celsiusba:",Celsius)
print("Celsiusbol Farenheitbe:",Fahrenheit2)
#5) Időtartam: Készíts programot, mely két időpontot kérdez a felhasználótól (óra, perc, másodperc külön), majd kiszámítja a két időpont közötti időtartamot másodpercben, és az eredményt kiírja a képernyőre.
print("Add meg óra - perc - másodperc értékeket!")
ora = int(input("Óra"))
perc = int(input("Perc"))
masodperc = int(input("Masodperc"))


#6) Pozitív, negatív, nulla: Készíts programot, mely a felhasználótól bekért számról megállapítja, hogy az a.) pozitív, negatív vagy nulla, b.) egész vagy nem egész. Az eredményt a képernyőre szöveges válasz formájában írja ki!

#7) Fizetés: Készíts programot, mely beolvas a felhasználótól egy fizetést, és a fizetés nagyságától függően kiírja, hogy az alacsony, átlagos, vagy magas! A kategóriákat a saját preferenciád alapján határozhatod meg! :D

#8) Turkáló: Egy turkálóban minden póló darabja 500 Ft. Ha egy vásárlás során valaki több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik vásárlása után már nem csökken tovább. Írj programot, amely a vásárolt pólók darabszámának ismeretében megmondja, hogy mennyit fizet a vásárló!

#9) Számok kiírása: Az ábrán egy program algoritmusa látható, amely kiírja a számokat 1-től 20-ig.

#Gondolok egy számra, legyen ez 1.
#Ismétlés, amíg a szám ≤ 20
#    Leírom a számot.
#    Új sort kezdek.
#    Növelem a számot 1-gyel.
#Ismétlés eddig

#10) Hatványozó program: Írj programot, amely hatványozni képes! Kérdezze meg az alapot (valós) és a kitevőt (egész), és írja képernyőre a hatvány értékét!

#11) Négyzetszám: Készíts programot, amely egy pozitív egész számról négyzetgyökvonás nélkül eldönti, hogy négyzetszám-e!

#12) Páratlan számok: Egy program bekér a felhasználótól két pozitív egész számot, és kiírja a két szám közötti összes páratlan számot. A program akkor is helyesen működik, ha a felhasználó előbb a felső, aztán az alsó határt adja meg (és fordítva is).  A program alogirtmusa a következő:

#Első és második szám bekérése
#Ha első > második
#    alsó = második, felső = első
#Egyébként
#    alsó = első, felső = második
#A ciklusváltozó legyen alsó
#Amíg a ciklusváltozó kisebb vagy egyenlő a felsővel
#    Ha a ciklusváltozó páratlan
#       Írd ki a ciklusváltozót
#    Növeld a ciklusváltozót eggyel
