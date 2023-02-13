def pontszamit(valasz, helyes):
    pont = 0
    for sorszam, betu in enumerate(valasz):
        if betu == helyes[sorszam]:
            if sorszam < 5:
                pont += 3
            elif sorszam < 10:
                pont += 4
            elif sorszam < 14:
                pont += 5
            else:
                pont += 6
    return pont

f = open("valaszok.txt")

adatok = f.read().split("\n")[:-1]
#adatok.remove("")
#adatok = adatok[:-1]
f.close()

helyes = adatok[0]
adatok.pop(0)

valaszok = []
for e in adatok:
    valaszok.append(e.split(" "))
    
print("2. feladat: A vetélkedőn "+str(len(valaszok))+" versenyző indult.")

versenyzo = input("3. feladat: A versenyző azonosítója = ")
versenyzovalasza = ""
for e in valaszok:
    if e[0] == versenyzo:
        print(e[1]+"\t (a versenyző válasza)")
        versenyzovalasza = e[1]

#print("{} \t (a versenyző válasza)".format([e[1] for e in valaszok if e[0] == versenyzo[0]]))

print("4. feladat")
print(helyes+"\t (a helyes megoldás)")
print(versenyzovalasza)

for sorszam, betu in enumerate(versenyzovalasza):
    if betu == helyes[sorszam]:
        print("+", end = "")
    else:
        print(" ", end = "")
print("\t (a versenyző helyes válaszai)")

feladat = int(input("5. feladat: A feladat sorszáma = "))

db = 0
        
for e in valaszok:
    if e[1][feladat] == helyes[feladat]:
        db += 1

print("A feladatra {0} fő, a versenyzők {1:.2%}-a adott helyesválaszt.".format(db, db/len(valaszok)))

f = open("pontok.txt","w")

eredmenyek = []
for e in valaszok:
    pont = pontszamit(e[1], helyes)
    f.write(e[0]+" "+str(pont)+"\n")
    eredmenyek.append([pont,e[0]])

f.close()

#eredmenyek.sort()
#eredmenyek.reverse()
#print(eredmenyek[:10])

csakpontok = set({})
for e in eredmenyek:
    csakpontok.add(e[0])
print(list(csakpontok)[-3:])





















