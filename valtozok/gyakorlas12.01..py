def oszlopba(munkalista, db):
    for i in range(len(munkalista)):
        print(munkalista[i],end = " ")
        if i % db == db-1:
            print()
    print()
    

lista = [3,1,6,2,7,3,4,9,6,8]
for i in range(0):
    lista.append(int(input("Kérek egy számot: ")))
print(lista)

for i in range(len(lista)):
    print(lista[i],end = " ")
    if i % 3 == 2:
        print()
print()

szamBe = int(input("Kérek egy számot: "))
if szamBe in lista:
    print("Van benne.")
else:
    print("Nincs benne.")

oszlopba(lista, 5)
