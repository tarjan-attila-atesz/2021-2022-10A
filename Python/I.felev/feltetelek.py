#IF-es feladatok - Feltetelvizsgalatok
#ismetles
print("Atesz") #kiiratas
eletkor = (int)(input("Hány éves vagy?")) #CASTING szambekeresnel
kedvencTantargy = input("Mi a kedvenc tantárgyad?") #STRING-et kerunk be
print("Az életkorod:" , eletkor)
print("A kedvenc tantárgyad: ", kedvencTantargy)
######################################
#Kérjünk be két számot a konzolról és 
#határozzuk meg melyik a nagyobb! 

szambe1 = (int)(input("Adj meg egy számot: "))
szambe2 = (int)(input("Adj meg másik számot: "))
if(szambe1>szambe2):
    print(szambe1)
else:
    print(szambe2)
