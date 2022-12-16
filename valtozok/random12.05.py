import random
import math


l = []
for i in range(10):
    szam = random.random()
    l.append(math.floor(szam * 90)+10)

print(l)

l = []
for i in range(10):
    szam = random.random()
    l.append(random.randint(10,99))

print(l)

l = []
for i in range(100):
    l.append(random.randint(-1000,1000)*3)


print(l)

print(sum(l))

l5 = []
for e in l:
    if e % 5 == 0:
        l5.append(e)
    
print(l5)

l5 = [e for e in l if e % 5 == 0]

print(l5)


szavak = ["alma","körte","barack","banán","dinnye","szőlő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

print("-"*20)

nagylista = []
for e in szavak:
    kislista = []
    kislista.append(e)
    kislista.append(random.randint(12,312))
    nagylista.append(kislista)
print(nagylista)

for e in nagylista:
    print(e[0].ljust(10),str(e[1]).rjust(4),"kg","-"*(e[1]//10))
    

minert = int(input("Add meg, hogy hol kezdődjön: "))
maxert = int(input("Add meg, hogy hol érjen véget: "))
db = int(input("Add meg, hogy hány értéket generáljon: "))

szamok = []

for i in range(db):
    szamok.append(random.randint(minert,maxert))
print(szamok)

legnagyobb = max(szamok)
egyseg = 80//legnagyobb
for e in szamok:
    print("-"*math.floor(e*egyseg))

szam = ""
while len(szam) != 3:
    szam = input("Kérek egy 3 jagyű számot: ")
szam = int(szam)

if szam % 12 == 0:
    print("Osztható")
print(szam)

szoveg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec feugiat facilisis magna ac finibus. Nunc sagittis a turpis quis vehicula. Etiam elementum mollis augue. Pellentesque consectetur lorem interdum sollicitudin porttitor. Nulla faucibus lobortis velit vitae pharetra. Praesent commodo sodales facilisis. Aenean tristique libero sed ex ornare, et congue velit luctus. Curabitur pulvinar turpis ac purus congue, ut iaculis dolor fringilla. Morbi in ligula quam. Aenean ipsum turpis, vulputate sit amet pretium sit amet, tempus eu augue."


betu = "k"
print(len(szoveg.split(" ")))
szoveg2 = szoveg.replace(betu,betu.upper())
print(szoveg2)










