def ado(sav, ter):
    f = open("utca.txt")
    arak = []
    arak = f.readline()
    arak = arak.replace("\n","").split(" ")
    f.close()

    ar = 0
    if sav == "A":
        ar = ter * int(arak[0])
    elif sav == "B":
        ar = ter * int(arak[1])
    elif sav == "C":
        ar = ter * int(arak[2])
        
    return ar


f = open("utca.txt")
hazak = []
for egysor in f:
    temp = egysor.replace("\n","").split(" ")
    hazak.append(temp)
f.close()

hazak.pop(0)

print("2. feladat. A mintában {} telek szerepel.".format(len(hazak)))

bekert = str(input("3. feladat. Egy tulajdonos adószáma: "))
x = 0
for e in hazak:
    if e[0] == bekert:
        print("{} utca {}".format(e[1], e[2]))
        x += 1
if x == 0:
    print("Nem szerepel az adatállományban.")

print("5.feladat")
A = []
B = []
C = []
for e in hazak:
    if e[3] == "A":
        A.append(e)
    if e[3] == "B":
        B.append(e)
    if e[3] == "C":
        C.append(e)

Aossz = 0
for e in A:
    Aossz += ado("A", int(e[4]))

Bossz = 0
for e in B:
    Bossz += ado("B", int(e[4]))

Cossz = 0
for e in C:
    Cossz += ado("C", int(e[4]))

print("A sávba {} telek esik, az adó {} Ft.".format(len(A), Aossz))
print("B sávba {} telek esik, az adó {} Ft.".format(len(B), Bossz))
print("C sávba {} telek esik, az adó {} Ft.".format(len(C), Cossz))









