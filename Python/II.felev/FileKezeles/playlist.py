def beolvas():
    zenek = [] # ebben tárolom el a zenéket
    with open("playlist.csv","r", encoding="UTF-8") as file:
        sorok = file.readlines() # fájl végéig beolvasás
        for sor in sorok: #bejárom a fájl tartalmát
            sor = sor.strip() #sorvége karaktert távolitok el
            darabok = sor.split(";") #elválasztás
            zene ={"eloado":darabok[0],"cim": darabok[1], "mufaj":darabok[2], "hossz":int(darabok[3]) }
            zenek.append(zene)
    return zenek


def teljes_hossz(zenek):
    hossz = 0
    for zene in zenek:
        hossz += zene["hossz"] #hossz változóban összeadom a mp-ek számát
    hossz_perc = hossz // 60
    hossz_masodperc = hossz % 60
    with open("02_hossz.txt","w", encoding="UTF-8") as file: #kiiratom a két számitott értékemet
        file.write(f"A lejátszási lista hossza: {hossz_perc} perc, {hossz_masodperc} másodperc \n")


def leghosszabb_rockzene(zenek):
    max_hossz =0
    leghosszabb_rockzene_cime = ""
    for zene in zenek:
        if zene["mufaj"]=="rock" and zene["hossz"] > max_hossz:
            max_hossz = zene["hossz"]
            leghosszabb_rockzene_cime =zene["cim"]
    with open("03_leghosszabb_rockzene_cime.txt","w", encoding="UTF-8") as file:
        file.write(f"{leghosszabb_rockzene_cime}\n")


def leggyakoribb_mufaj(zenek):
    stat = {}
    for zene in zenek:
        mufaj = zene["mufaj"].upper()

        if mufaj not in stat:
            stat[mufaj] =1
        else:
            stat[mufaj] +=1

    max_elofordulas = 0
    leggyakoribb =""

    for mufaj, elofordulas in stat.items():
        if elofordulas > max_elofordulas:
            max_elofordulas = elofordulas
            leggyakoribb = mufaj

    with open("04_leggyakoribb_mufaj.txt","w", encoding="UTF-8") as file:
        file.write(f"{leggyakoribb}\n")

lejatszai_lista = beolvas()
teljes_hossz(lejatszai_lista)
leghosszabb_rockzene(lejatszai_lista)
leggyakoribb_mufaj(lejatszai_lista)