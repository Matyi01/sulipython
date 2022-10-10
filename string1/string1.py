nev = input("Kérek egy nevet: ")
print("A "+nev+" nevet írtad be.")
print("A {belsonev} nevet írtad be.".format(belsonev = nev))
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
#szavak = szavak[:-1]
print(szavak)
