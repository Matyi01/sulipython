def haromszog():
    vissza = []
    for i in range(3):
        szam = ""
        while szam == "":
            try:
                szam = int(input(str(i+1)+". oldal: "))
            except:
                print("Ez nem egész szám!")
        vissza.append(szam)
    return vissza
