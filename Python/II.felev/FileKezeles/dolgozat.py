from xmlrpc.client import boolean


atlag = 0

with open("homerseklet.txt","r") as file:
    osszeg = 0
    darab = 0
    sor = file.readline()

    while sor:
        osszeg += int(sor)
        darab +=1
        sor = file.readline()
atlag = osszeg/darab
print("1.feladat:")
print(f"\tA fájl összesen {darab} napi adatot tartalmaz!")
print(f"\tAz átlagos napi hőmérséklet: {atlag} °C volt")


def beolvas():
    Juventus = []
    with open("juve.txt","r", encoding="UTF-8") as file:
        sorok = file.readlines()
        for sor in sorok:
            sor = sor.strip()
            darabok = sor.split(";")
            juvent = {"Mezszám":darabok[0], "Név":darabok[1],"Nemzetiség":darabok[2], "Poszt":darabok[3], "Születési év":int(darabok[4])}
            Juventus.append(juvent)

JuventusFC = beolvas()

