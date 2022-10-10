nev = input("Kérek egy nevet: ")
mgh = "ö","ü","ó","ő","ú","é","á","ű","a","e","i","u","o"
z = ""
if nev[0].lower() in mgh:
    z += "z"

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
