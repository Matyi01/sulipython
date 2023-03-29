f = open("snooker.txt")
snooker = []
for e in f:
    temp = e.replace("\n","").split(";")
    snooker.append(temp)
f.close()
snooker.pop(0)

print("3. feladat: A világranglistán {} versenyző szerepel".format(len(snooker)))

bevetelek = []
for e in snooker:
    bevetelek.append(int(e[3]))

print("4. feladat: A versenyzők átlagosan {:.2f} fontot kerestek".format(sum(bevetelek)/len(bevetelek)))

kinaiak = []
for e in snooker:
    if e[2] == "Kína":
        kinaiak.append(e)
kbevetel = []
for e in kinaiak:
    kbevetel.append(int(e[3]))

for e in kinaiak:
    if int(e[3]) == max(kbevetel):
        print("5. feladat: A legjobban kereső kínai versenyző:")
        print("\tHelyezés: {}".format(e[0]))
        print("\tNév: {}".format(e[1]))
        print("\tOrszág: {}".format(e[2]))
        print("\tNyeremény összege: {} Ft".format(int(e[3])*380))

x = False  
for e in snooker:
    if e[2] == "Norvégia":
        x = True

if x == True:
    print("6. feladat: A versenyzők között van norvég versenyző.")
else:
    print("6. feladat: A versenyzők között nincs norvég versenyző.")

print("7. feladat: Statisztika")

orszagok = {}
for e in snooker:
    if e[2] not in orszagok:
        orszagok[e[2]] = 1
    else:
        orszagok[e[2]] += 1

for e in orszagok:
    if orszagok[e] > 4:
        print("\t{} - {} fő".format(e,orszagok[e]))
