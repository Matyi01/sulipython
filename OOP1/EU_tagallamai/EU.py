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

csatlakozott = 0
for e in adatok:
    if int(e.ev[:4]) <= 2018:
        csatlakozott += 1
print(f"3. feladat: EU tagállamainak száma: {csatlakozott}")

csatlakozott2007 = 0
for e in adatok:
    if e.ev[:4] == "2007":
        csatlakozott2007 += 1
print(f"4. feladat: 2007-ben {csatlakozott2007} ország csatlakozott.")

for e in adatok:
    if e.orszag == "Magyarország":
        print(f"5. feladat: Magyarország csatlakozásának dátuma: {e.ev}")

majus = False
for e in adatok:
    if e.ev[6:7] == "5":
        majus = True
if majus:
    print("6. feladat: Májusban volt csatlakozás!")

evek = []
for e in adatok:
    evek.append(e.ev[:4])
legutobbi = ""
for e in adatok:
    if max(evek) == e.ev[:4]:
        legutobbi = e.orszag
print(f"7. feladat: Legutoljára csatlakozott ország: {legutobbi}")

print("8. feladat: Statisztika")
stat = {}
for e in adatok:
    stat[e.ev[:4]] = 0
for e in adatok:
    stat[e.ev[:4]] += 1
for e in stat:
    print(f"\t{e} - {stat[e]} ország")






