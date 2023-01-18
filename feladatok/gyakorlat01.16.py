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
    x = full[random.randint(1,len(full)-1)]
    x = x.split(" : ")
    x[1] = x[1].strip("\n")
    print("Mit jelent az "+x[0]+" szó?")
    
    for e in full:
        full.remove(e)
        e = e.split(" : ")
        e[1] = e[1].strip("\n")
        
        
        
    
    f.close()

szoRandom()
