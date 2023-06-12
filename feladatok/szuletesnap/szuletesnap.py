class szulinap:
    def __init__(self, nev, szev):
        self.nev = nev
        self.szev = szev
    def hanyeves(self, ev):
        return int(ev) - int(self.szev)

f = open("szuletesnap.txt", encoding="UTF-8")
adatok = []
for e in f:
    adatok.append(szulinap(*e.strip().split(";")))
f.close()

beev = input("Kérek egy évszámot: ")
f = open("hanyeves.txt", "w")
for e in adatok:
    print(e.hanyeves(beev))
    f.write(f"{e.nev};{e.hanyeves(beev)}\n")
f.close()

szuletesievek = {}
for e in adatok:
    szuletesievek[e.nev] = e.szev
print(f"Legidősebb: {min(szuletesievek, key=szuletesievek.get)}, {min(szuletesievek.values())}")



