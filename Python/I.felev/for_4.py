#break

# írjuk ki a számokat 1-10-ig és ha elérte az 5-ös értéket, álljon meg
# a program.

for i in range(1,11):
    print(i,"")
    if(i == 5):
        break

## írjuk ki a számokat 1-10-ig és ha elérte az 5-ös értéket, NE álljon meg
# a program.
print ("____________________")
for i in range(1,11):
    print(i,"")
    if(i == 5):
        print("Megvan a szám...")
        continue
        