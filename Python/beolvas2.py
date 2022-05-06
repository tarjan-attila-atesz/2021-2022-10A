with open ("jegyek.txt","r") as beolvasas:
    sorok = beolvasas.readlines

for sor in sorok:
    print(sor)
beolvasas.close()