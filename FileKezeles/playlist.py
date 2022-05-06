#1. feladat - Olvasd be és tárold el egy adatszerkezetben a fájl tartalmát [Lista]

def beolvas():
    zenek = []

    with open("playlist.csv", "r", encoding="UTF-8") as file:
        sorok = file.readlines()

        for sor in sorok:
            sor = sor.strip()
            darabok = sor.split(";")

            zene = {"előadó:":darabok[0], "cím:":darabok[1], 
                    "műfaj:":darabok[2], "hossz:":int(darabok[3])
            
            }
            zenek.append(zene)
        return zenek