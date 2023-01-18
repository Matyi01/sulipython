import random

def szoBe():
    f = open("szotar.txt","a")

    x = input("kérek egy szót:")
    y = input("kérem a jelentését:")
    f.write(str(x)+" : "+str(y)+"\n")
    
    f.close()

def szoRandom():
    f = open("szotar.txt","r")

    full = f.readlines()
    for i in range(len(full)):
        full[i] = full[i].split(" : ")
        full[i][1] = full[i][1].strip("\n")
        
    x = full[random.randint(1,len(full)-1)]
    print(x[0] + " szó?")

    f.close()

szoRandom()
