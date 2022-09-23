szavak=["ló","bakfitty","csutora"]
szamok=[1,0,3000,2]
print(szavak)
szavak.sort()
print(szavak)
szavak.append("hát")
print(szavak)
szavak.insert(1,"az hogy")
print(szavak)
szamok.append(20)
szamok.append(20)
darab=szamok.count(20)
print(darab)
szamok.remove(20)
print(szamok)
for szam in szamok:
    print("szám: "+str(szam))
