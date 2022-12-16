def szamok1():
    szamok = []
    while len(szamok) != 7:
        try:
            szamok.append(int(input("Kérek egy számot: ")))
        except:
            print("Ez nem egy szám.")
    return szamok

szamok = szamok1()

print(szamok[::-1])

for i in range(len(szamok)):
    if i % 5 == 0 and i != 0:
        print()
    print(str(szamok[i])+"\t",end="")

print()

print(sum(szamok))

szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

betu = ""
while betu != "fin":
    betu = input("Kérek egy betűt: ")
    if betu in szoveg:
        print(szoveg.index(betu))

szoveg2 = szoveg.split(".")
print(szoveg2[::-1])

szoveg = szoveg.replace("a","")
szoveg = szoveg.replace("e","")
print(len(szoveg))

def fenyo():
    lista = [[3,1],[2,3],[1,5],[0,7],[2,3],[1,5],[0,7],[2,3],[1,5],[0,7],[3,1],[2,3]]

    karakter = ""
    while karakter != "1":
        karakter = input("Kérek egy karaktert: ")
        for e in lista:
            print(" "*e[0],karakter*e[1])
fenyo()








