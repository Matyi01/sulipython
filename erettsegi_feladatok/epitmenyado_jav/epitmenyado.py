def ado(adosav, alapterulet):
    if adosav == "A":
        ar = int(arak[0]) * alapterulet
    elif adosav == "B":
        ar = int(arak[1]) * alapterulet
    else:
        ar = int(arak[2]) * alapterulet
    if ar >= 10000:
        return ar
    else:
        return 0

f = open("utca.txt")
hazak = []
for e in f:
    hazak.append(e.replace("\n","").split(" "))
f.close()

arak = hazak.pop(0)

print("2. feladat. A mintában {} telek szerepel.".format(len(hazak)))

adoszam = input("3. feladat. Egy tulajdonos azonosítója: ")
tulajdonok = []
for e in hazak:
    if e[0] == adoszam:
        tulajdonok.append(e)

#tulajdonok = [e for e in hazak if e[0] == adoszam]

if len(tulajdonok) == 0:
    print("Nem szerepel az adatállományban.")
else:
    for e in tulajdonok:
        print("{} utca {}".format(e[1],e[2]))

hazakA = [e for e in hazak if e[3] = "C"]







