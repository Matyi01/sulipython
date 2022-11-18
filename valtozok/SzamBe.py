#Számbekérő modul
#Többféle paraméterezéssel
#2022. 11. 18. Holczer Mátyás

def szamBe(szoveg,tort=False,minimum=False,maximum=False):
#    print(szoveg)
#    print(tort)
#    print(minimum)

    hiba = True
    while hiba:
        try:
            if tort:
                szam = float(input(szoveg))
            else:
                szam = int(input(szoveg))

        except:
            print("Hiba!")
        else:
            hiba = False
    
szamBe("Aggyá meg számót: ",minimum=10,tort=True)

