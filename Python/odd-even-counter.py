# Készítsünk egy olyan programot, 
# ami megszámolja, hogy hány páros és 
# páratlan számot írunk be a konzolra. 
# A program csak akkor áll le, hogyha 0-át ütünk be!

odd_number = 0  #paratlan
even_number = 0 #paros

stopNumber = int(input("Írd be a számokat, de 0-ra leállok!"))

while stopNumber!=0:
    if stopNumber %2 ==0:
        even_number +=1
    else:
        odd_number +=1
    stopNumber = int(input("Írd be a számokat, de 0-ra leállok!"))
    
print("Paros szamok: ",even_number)
print("Paratlan szamok: ",odd_number)