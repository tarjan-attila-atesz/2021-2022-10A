atlag = 0                       			# változó az átlagnak
with open("jegyek.txt","r") as f:  		    # be.txt megnyitása olvasásra
    # a beolvasott számok összege (az átlaghoz kell)
    osszeg = 0
    # hány számot olvastunk be (az átlaghoz kell)
    darab = 0
    sor = f.readline()         			    # első sor beolvasása

    while sor:                  			# amíg van sor a fájlban...
        osszeg += int(sor)      			# ...hozzáadjuk az adott számot az összeghez
        darab += 1              			# ...növeljük a beolvasott számok darabszámát
        sor = f.readline()      			# ...beolvassuk a következő sort
atlag = osszeg / darab         			    # az átlag az összeg és a darabszám hányadosa
with open("ki.txt", "w") as f:  		    # ki.txt megnyitása írásra
    f.write("Az átlag: " + str(atlag) + "\n")  	# az eredmény fájlba írása
