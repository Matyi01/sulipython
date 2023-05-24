class eu:
    def __init__(self, orszag, ev):
        self.orszag = orszag
        self.ev = ev
    def __str__(self):
        return f"A {self.orszag} ország {self.ev}-ben csatlakozott"

f = open("EUcsatlakozas.txt")

adatok = []
for e in f:
    temp = e.strip().split(";")
    adatok.append(eu(*temp))
f.close()

print("3. feladat")
csatlakozott = 0
for e in adatok:
    if int(e.ev[0:4]) <= 2018:
        csatlakozott += 1
print(csatlakozott)

print("4. feladat")
csatlakozott2007 = 0
for e in adatok:
    if int(e.ev[0:4]) == 2007:
        csatlakozott2007 += 1
print(csatlakozott2007)

print("5. feladat")
