import random

evek = []
datumok = []
for i in range(1000):
    ev = random.randint(1900,1999)
    h = random.randint(1,12)
    if h == 1 or h == 3 or h == 5 or h == 7 or h == 8 or h == 10 or h == 12:
        nap = random.randint(1,31)
    elif h == 4 or h == 6 or h == 9 or h == 11:
        nap = random.randint(1,30)
    else:
        if ev % 4 == 0 and ev % 400 == 0:
            nap = random.randint(1,29)
        else:
            nap = random.randint(1,28)
    evek.append(ev)
    datum = str(ev)+"."+str(h)+"."+str(nap)
    datumok.append(datum)
print(datumok)
atlag = sum(evek) / len(evek)
print(atlag)
