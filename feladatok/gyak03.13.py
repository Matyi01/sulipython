tablazat = []

for i in range(20):
    sor = []
    for e in range(10):
        sor.append((e+1)*(i+1))
    tablazat.append(sor)
print(tablazat)

beker = int(input("Melyik oszlop? "))
oszlop = []
for e in tablazat:
    oszlop.append(e[beker-1])
print(oszlop)

f = open("oszlop.txt","w")

    
