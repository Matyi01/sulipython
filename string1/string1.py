nev = input("Kérek egy nevet: ")

z = ""
print(z)
if nev[0] == "A"or"a"or"E"or"e"or"I"or"i"or"O"or"o"or"Í"or"í"or"Ö"or"ö"or"Ü"or"ü"or"Ó"or"ó"or"Ő"or"ő"or"Ú"or"ú"or"Ű"or"ű"or"Á"or"á"or"É"or"é":
    z += "z"
print(z)

print("A"+z+" "+nev+" nevet írtad be.")

print("A{z} {belsonev} nevet írtad be.".format(belsonev = nev, z = z))

if len(nev) < 5:
    print("Jó rövid név.")
elif len(nev) >= 10:
    print("Very big név.")
    
be = "nemvégjel"
szavak=[]

while be != "":
    be = input("Írj be valamit: ")
    szavak.append(be)
    
#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavak)-1)
szavak = szavak[:-1]
print(szavak)
