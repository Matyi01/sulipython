def oszlopba(munkalista, db):
    for i in range(len(munkalista)):
        print(munkalista[i],end = " ")
        if i % db == db-1:
            print()
    print()
    
lista = []
for i in range(10):
    szam = ""
    while szam == "":
        try:
            szam = int(input("Kérek egy számot: "))
            lista.append(szam)
        except:
            print("Ez nem egy szám.")
print(lista)

for i in range(len(lista)):
    print(lista[i],end = " ")
    if i % 3 == 2:
        print()
print()

szamBe = ""
while szamBe == "":
    try:
        szamBe = int(input("Kérek egy számot: "))
    except:
        print("Ez nem egy szám.")
if szamBe in lista:
    print("Van benne.")
else:
    print("Nincs benne.")

oszlopba(lista, 5)
