import random
import datetime

def szoBe():
    x = "a"
    while x != "":
        f = open("szotar.txt","a")

        x = input("kérek egy szót: ")
        if x == "":
            y = ""
        else:
            y = input("kérem a jelentését: ")

        ido = datetime.date.today()
        
        if x != "":
            f.write(str(x)+" : "+str(y)+" : "+str(ido)+"\n")
        
        f.close()

def szoRandom():
    f = open("szotar.txt","r")

    full = f.readlines()
    for i in range(len(full)):
        full[i] = full[i].split(" : ")
        full[i][2] = full[i][2].strip("\n")

    ido = input("mettől szeretnéd a szavakat? (YYYY-MM-DD): ")

    for i in range(len(full)):
        if str(full[i][2]) == str(ido):
            ido = i
    print(ido)

    
    b = "a"
    while b != "":

        print(full[4],full[5],full[6],full[7])
            
        x = full[random.randint(ido,len(full)-1)]
        szo1 = x[1]
        
        print(x[0] + " szó jelentése?")

#while y == x:
        y = full[random.randint(ido,len(full)-1)]

        szo2 = y[1]

        
        z = full[random.randint(ido,len(full)-1)]

        szo3 = z[1]


        q = full[random.randint(ido,len(full)-1)]
        szo4 = q[1]


        
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
