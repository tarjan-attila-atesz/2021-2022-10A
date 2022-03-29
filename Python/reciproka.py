value = int(input("Kérem a számot: "))
print("A szám ",value," reciproka: ",1/value)


value2 = int(input("Kérem a számot: "))
if(value2>0):
    print("A szám reciproka: ",1/value2)
else:
    print("Rossz adatot adtál meg!")


value3 = int(input("Kérem a természetes számot:"))
try:
    print("A szám ",value3," reciproka: ",1/value3)
except:
    print("Rossz adatot adtál meg!")