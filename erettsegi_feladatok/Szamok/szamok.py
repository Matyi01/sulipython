f = open("felszam.txt","r")
for sor in f:
    josor = sor.replace("\n","")
    print(josor)

f.close()
