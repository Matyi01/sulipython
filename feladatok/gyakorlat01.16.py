import random
import datetime

def szoBe():
#ures sor vegjelig keri be
    x = "a"
    while x != "":
        f = open("szotar.txt","a")

#szavak bekerese
        x = input("kérek egy szót: ")
        if x == "":
            y = ""
        else:
            y = input("kérem a jelentését: ")

#datum generalasa a szoparhoz
        ido = datetime.date.today()

#adatok hozzaadasa a fajlhoz
        if x != "":
            f.write(str(x)+" : "+str(y)+" : "+str(ido)+"\n")
        
        f.close()

def szoRandom():
    f = open("szotar.txt","r")

#fajl adatait listava alakitja amivel lehet dolgozni
    full = f.readlines()
    for i in range(len(full)):
        full[i] = full[i].split(" : ")
        full[i][2] = full[i][2].strip("\n")

#bekeri hogy milyen ido legyen a legkisebb amitol kerdezi
    idomin = input("mettől szeretnéd a szavakat? (YYYY-MM-DD): ")

#elso elem keresese a listaban amiben megvan a bekert ido
    for i in range(len(full)):
        if str(full[i][2]) == str(idomin):
            idomin = int(i)

#bekeri hogy milyen ido legyen a lenagyobb ameddig kerdezi
    idomax = input("meddig szeretnéd a szavakat? (YYYY-MM-DD): ")

#elso elem keresese hatulrol a listaban amiben megvan a bekert ido
    for i in reversed(range(len(full))):
        if str(full[i][2]) == str(idomax):
            idomax = int(i)

#jo es rossz valaszok szamanak valtozoi
    jo = 0
    rossz = 0
    
#ures sor vegjelig kerdez
    b = "a"
    while b != "":
#szo generalasa amit kerdez
        x = full[random.randint(idomin,idomax)]

#megkerdezi a generalt szo jelenteset
        print(x[0] + " szó jelentése?")

#ciklus ami harom kulonbozo rossz szot general es listaba rakja
        szavak = [x[1]]
        for i in range(3):
            y = full[random.randint(idomin,idomax)][1]
            while y in szavak:
                y = full[random.randint(idomin,idomax)][1]
            szavak.append(y)

#az elobb generalt lista elemeit osszekeveri es elemenkent kiiratja
        random.shuffle(szavak)
        print(szavak[0]+", "+szavak[1]+", "+szavak[2]+", "+szavak[3])
        
#bekeri a szo jelenteset es megnezi hogy jo e
        b = input()
        if b == "":
            break
        if b == x[1]:
            print("Jol tudtad!")
            jo += 1
        else:
            print("Nem jo...")
            rossz += 1

#jo es rossz valaszok szamanak kiiratasa
    print(str(jo)+" jo es "+str(rossz)+" rossz valaszod volt")
    szazalek = (jo / (jo + rossz)) * 100
    
    print("az eredmenyed: "+str(round(szazalek,2))+"%")
    f.close()


szoBe()
szoRandom()
