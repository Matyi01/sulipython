import modul, random

f = open("szavak.txt")
adatok = (f.read().strip().replace('"',"").split(", "))
f.close()

szavak = []
for e in adatok:
    szavak.append(modul.szo(e))
    
rejtett = random.choice(szavak)

x = 0
while True:
    x += 1
    be = input("Kérem a tippet: ")
    if be == "stop":
        break
    vissza = rejtett.minta(be)
    print(f"Az eredmény: {vissza}\n")
    if vissza == be:
        print(f"{x} tippeléssel sikerült kitalálni.")
        break
