def darabol(sor):
    lista = sor.split("*")
    temp = lista[-1].strip().split(" ")
    lista.pop(-1)
    lista += temp
    return lista

f = open("NASAlog.txt")
naplo=[]
for e in f:
    naplo.append(darabol(e))
f.close()




print("5. feladat: Kérések száma: {}".format(len(naplo)))
print("6. feladat: Válaszok összes mérete: {} byte".format())



