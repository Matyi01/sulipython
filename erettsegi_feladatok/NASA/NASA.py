def darabol(sor):
    lista = sor.split("*")
    temp = lista[-1].strip().split(" ")
    lista.pop(-1)
    lista += temp
    return lista

def ByteMeret(meret):
    if meret == "-":
        return 0
    else:
        return int(meret)

def Domain(nev):
    return not nev[-1] in "0123456789"

f = open("NASAlog.txt")
naplo=[]
for e in f:
    naplo.append(darabol(e))
f.close()

print("5. feladat: Kérések száma: {}".format(len(naplo)))

meretek = []
for e in naplo:
    meretek.append(ByteMeret(e[4]))

print("6. feladat: Válaszok összes mérete: {} byte".format(sum(meretek)))

domaine = []
for e in naplo:
    domaine.append(Domain(e[0]))

print("8. feladat: Domain-es kérések: {:.2%}".format(domaine.count(True) / len(domaine)))


print("9. feladat: Statisztika:")
hibakodok = []
for e in naplo:
    if e[3] not in hibakodok:
        hibakodok.append(e[3])

for e in hibakodok:
    temp = []
    for o in naplo:
        if o[3] == e:
            temp.append(e)
    print("\t{}: {} db".format(e,len(temp)))


