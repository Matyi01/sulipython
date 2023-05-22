class tanc:
    def __init__(self,tanc,lany,fiu):
        self.tanc = tanc
        self.lany = lany
        self.fiu = fiu
    def __str__(self):
        return "tánc: {}, lány: {}, fiú: {}".format(self.tanc,self.lany,self.fiu)
    def isvilma(self):
        return self.lany == "Vilma"

f = open("tancrend.txt")

sorok = []
#2. megoldas
tancok2 = []
temp=[]

for e in f:
    sorok.append(e.strip())
    #2. megoldas
    if len(temp) < 3:
        temp.append(e)
    else:
        tancok2.append(tanc(temp[0],temp[1],temp[2]))

f.close()

#1. megoldas
tancok =  []
for i in range(len(sorok)//3):
    tancnev = sorok[i*3]
    lany = sorok[i*3+1]
    fiu = sorok[i*3+2]
    tancok.append(tanc(tancnev,lany,fiu))


print("2. feladat")
print("első tánc: {}, utolsó tánc: {}".format(tancok[0].tanc,tancok[-1].tanc))

db = 0
for egytanc in tancok:
    if egytanc.tanc == "samba":
        db += 1
        
print("3. feladat")
print("Ennyi samba volt: {}".format(db))

print("4. feladat")
print("Vilma ezekben szerepelt: ")

for egytanc in tancok:
    if egytanc.isvilma():
        print(egytanc.tanc)

print("5. feladat")
tancnev = input("Kérek egy táncnevet: ")
for elem in tancok:
    if elem.lany == "Vilma" and elem.tanc == tancnev:
        print("A {} bemutatóján Vilma párja {} volt.".format(tancnev, elem.fiu))
        break
else:
    print("Vilma nem táncolt {}-t.".format(tancnev))

fiu = []
lany = []
for egytanc in tancok:
    if egytanc.fiu not in fiu:
        fiu.append(egytanc.fiu)
    if egytanc.lany not in lany:
        lany.append(egytanc.lany)

f = open("szereplok.txt", "w")
f.write("Lányok: "+", ".join(lany)+"\n"+"Fiuúk: "+", ".join(fiu))
f.close()

print("7. feladat")
statfiu = {}
for egy in fiu:
    statfiu[egy] = 0
for egytanc in tancok:
    statfiu[egytanc.fiu] += 1

statlany = {}
for egy in lany:
    statlany[egy] = 0
for egytanc in tancok:
    statlany[egytanc.lany] += 1

print(statfiu)
print(statlany)










