f = open("tancrend.txt")

tancok = []
kislista = []
for e in f:
    e = e.replace("\n","")
    kislista.append(e)
    if len(kislista) == 3:
        tancok.append(kislista)
        kislista = []

f.close()

print("2. feladat. Az első tánc: {}, az utolsó tánc: {}".format(tancok[0][0], tancok[-1][0]))

x = 0
for e in tancok:
    if e[0] == "samba":
        x += 1
print("3. feladat. A sambát {} pár mutatta be.".format(x))

vilma = []
for e in tancok:
    if e[1] == "Vilma":
        vilma.append(e[0])

print("4. feladat. Vilma ezekben a táncokban vett részt: "+", ".join(vilma))

tanc = input("5. feladat. Adj meg egy táncot: ")

y = 0
for e in tancok:
    if e[0] == tanc:
        print("A {} bemutatóján Vilma párja {} volt.".format(e[0], e[2]))
        y += 1
if y == 0:
        print("Vilma nem táncolt {}-t".format(tanc))

