import random

f = open("datumok.txt","w")

for i in range(100000):
    ev = random.randint(2003,2008)
    h = random.randint(1,12)
    if h == 1 or h == 3 or h == 5 or h == 7 or h == 8 or h == 10 or h == 12:
        nap = random.randint(1,31)
    elif h == 4 or h == 6 or h == 9 or h == 11:
        nap = random.randint(1,30)
    else:
        if ev % 4 == 0:
            nap = random.randint(1,29)
        else:
            nap = random.randint(1,28)
    ev = str(ev)
    h = str(h)
    nap = str(nap)
    f.write(ev + ". " + h + ". " + nap + ". ")

f.close()
