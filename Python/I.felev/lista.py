numbers =[10,5,7,3,2,1]

#Lista kiírása

print("A lista elemei: ",numbers)
print("A lista hossza: ",len(numbers))

# Új elem beszúrása (régi helyére [csere]) + Új lista kiírása

numbers[0]=17 #első hely
numbers[3]=9 #lista "közepére"
print("Az új lista elemei: ",numbers)
print("Az új lista hossza: ",len(numbers))
del numbers[0]
print("Az új lista elemei: ",numbers)
print("Az új lista hossza: ",len(numbers))
numbers.append(6) # Lista végére szúr be elemet
print(numbers)
numbers.insert(3,60)
print(numbers)
print("Az új lista hossza: ",len(numbers))

progjegyek = ["Géza",2,"Roland",1,"Dávid",3,"Elizabet",5]
print("A Prgjgyk elemei: ", progjegyek)
progjegyek[3] = 2
print("A Prgjgyk elemei: ", progjegyek)
progjegyek.append(4)
progjegyek.insert(8,"Zoltán")
print("A Prgjgyk elemei: ", progjegyek)
