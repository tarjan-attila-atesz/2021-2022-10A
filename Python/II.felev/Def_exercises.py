#Készítsünk egy függvényt, ami összead 3 számot. 
#Az összeadást és az eredményt is kiírja.

def osszead(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

osszead(1,2,3)

#Írjunk egy függvény, ami egy nevet kér be, 
#és a bekért névvel együtt köszön!
def koszones(name):
    print("Üdvözöllek:", name)

koszones("Attila")


#Írjunk egy függvény, ami két nevet kér be, 
#és a bekért névvel együtt köszön!

def koszones(name,name2):
    print("Üdvözöllek:", name, "és téged is", name2)

koszones("Attila","Gábor")

#Írjunk függvényt, ami a lakcímedet kéri be, 
#és azt is adja vissza szöveges (beszédes formában)


def lakcim(utca, varos, irszam):
    print("A lakcímem", utca, "utca", varos, irszam)

utca = input("Utca: ")
irszam = input("Irszám: ")
varos = input("Város: ")

lakcim(utca, varos, irszam)



