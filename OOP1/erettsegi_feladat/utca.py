class telek:
    paros = False
    szelesseg = 0
    kerites = ""
    hazszam = 0
    def __init__(self,sor,hazszam):
        #sor: 1 8 k
        vag = sor.replace("\n","").split(" ")
        
        if vag[0] == 1:
            self.paros = False
        else:
            self.paros = True
            
        paros = vag[0] == 0
        
        self.szelesseg = int(vag[1])

        self.kerites = vag[2]

        if self.paros:
            self.hazszam = hazszam[1]*2
        else:
            self.hazszam = hazszam[0]*2-1

#t = telek("1 8 k")

telkek = []
f = open("kerites.txt")

db = 0
for sor in f:
    telkek.append(telek(sor,[len(telkek)-paros,paros]))
    if telkek[-1].paros:
        db += 1

    
f.close()

#print(telkek[0].kerites)


print("2. feladat")
print("Az eladott telkek száma {}".format(len(telkek)))



print("3. feladat")
if telkek[-1].paros:
    print("A páros oldalon adták el az utolsó telket.")
else:
    print("A páratlan oldalon adták el az utolsó telket.")

print("az utolsó telek házszáma {}".format(telkek))







