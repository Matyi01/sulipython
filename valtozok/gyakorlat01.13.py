import random

def randomDatum():
    ev = random.randint(2003,2008)
    h = random.randint(1,12)
    hk = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    if h == 1 or h == 3 or h == 5 or h == 7 or h == 8 or h == 10 or h == 12:
        nap = random.randint(1,31)
    elif h == 4 or h == 6 or h == 9 or h == 11:
        nap = random.randint(1,30)
    else:
        if ev % 4 == 0:
            nap = random.randint(1,29)
        else:
            nap = random.randint(1,28)
    if nap // 10 == 0:
        nap = str(nap).zfill(2)
    if h // 10 == 0:
        h = str(h).zfill(2)
    datum = str(ev) + ". " + hk[int(h)-1] + ". " + str(nap) + ". "
    return datum

def randomIdo():
    ora = random.randint(1,23)
    p = random.randint(1,59)
    mp = random.randint(1,59)
    ido = str(ora) + ":" + str(p) + ":" + str(mp)
    return ido

def fileIras():
    f = open("datumok.txt","w")
    for i in range(10):
        f.write(randomDatum() + randomIdo() + "\n")
    f.close()


fileIras()
