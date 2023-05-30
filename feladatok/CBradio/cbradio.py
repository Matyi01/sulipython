class cb:
    def __init__(self, ora, perc, adasok, nev):
        self.ora = ora
        self.perc = perc
        self.adasok = adasok
        self.nev = nev
    def negyadas(self):
        if self.adasok == "4":
            return True
#6. feladat
    def atszamolpercre(self):
        return int(self.ora)*60 + int(self.perc)

#2. feladat
f = open("cb.txt")
adatok = []
for e in f:
    temp = e.strip().split(";")
    adatok.append(cb(*temp))
f.close()
adatok.pop(0)

#3. feladat
print(f"3. feladat: Bejegyzések száma: {len(adatok)} db")

#4. feladat
volte = False
for e in adatok:
    if e.negyadas() == True:
        volte = True
        break
if volte == True:
    print("4. feladat: Volt négy adást indító sofőr.")
else:
    print("4. feladat: Nem volt négy adást indító sofőr.")

#5. feladat
nevbe = input("5. feladat: Kérek egy nevet: ")
hivasok = 0
for e in adatok:
    if e.nev == nevbe:
        hivasok += int(e.adasok)
if hivasok != 0:
    print(f"\t{nevbe} {hivasok}x használta a CB-rádiót.")
else:
    print("\tNincs ilyen nevű sofőr!")

#7. feladat
f = open("cb2.txt","w")
f.write("Kezdes;Nev;AdasDb\n")
for e in adatok:
    temp = f"{e.atszamolpercre()};{e.nev};{e.adasok}\n"
    f.write(temp)
f.close()

#8. feladat
nevek = []
for e in adatok:
    if e.nev not in nevek:
        nevek.append(e.nev)
print(f"8. feladat: Sofőrök száma: {len(nevek)} fő")

#9. feladat
print("9. feladat: Legtöbb adást indító sofőr")
adasok = {}
for e in nevek:
    adasok[e] = 0
for e in adatok:
    adasok[e.nev] += int(e.adasok)
maxadas = max(adasok.values())
maxnev = max(adasok, key = adasok.get)
print(f"\tNév: {maxnev}")
print(f"\tAdások száma: {maxadas} alkalom")
