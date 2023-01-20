import random
import datetime

def szoBe():
    x = "a"
    while x != "":
        f = open("szotar.txt","a")

        x = input("kérek egy szót:")
        if x == "":
            y = ""
        else:
            y = input("kérem a jelentését:")

        ido = datetime.date.today()
        
        if x != "":
            f.write(str(x)+" : "+str(y)+" : "+str(ido)+"\n")
        
        f.close()

def szoRandom():
    f = open("szotar.txt","r")

    full = f.readlines()
    for i in range(len(full)):
        full[i] = full[i].split(" : ")
        full[i][1] = full[i][1].strip("\n")

    ido = input("mettől szeretnéd a szavakat? (YYYY-MM-DD): ")

    for i in range(len(full)):
        if str(full[i][2]) == str(ido):
            print(full[i][2])
        
    
    b = "a"
    while b != "":


            
        x = full[random.randint(0,len(full)-1)]
        
        print(x[0] + " szó jelentése?")
        
        szo1 = x[1]
        full.remove(x)
        
        y = full[random.randint(0,len(full)-1)]
        szo2 = y[1]
        full.remove(y)
        
        z = full[random.randint(0,len(full)-1)]
        szo3 = z[1]
        full.remove(z)

        q = full[random.randint(0,len(full)-1)]
        szo4 = q[1]

        full.append(x)
        full.append(y)
        full.append(z)
        
        szavak = [szo1,szo2,szo3,szo4]
        random.shuffle(szavak)
        print(szavak[0]+", "+szavak[1]+", "+szavak[2]+", "+szavak[3])

        b = input()
        if b == "":
            break
        if b == x[1]:
            print("Jol tudtad!")
        else:
            print("Nem jo...")

    f.close()


szoBe()
szoRandom()
