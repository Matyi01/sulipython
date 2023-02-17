print("1. faladat")
szoveg = input("Kérek egy szöveget: ")

szam = ""

#while type(szam) != int:
while szam == "":
    try:
        szam = int(input("Kérek egy egész számot: "))
    except:
        print("Ez nem egész szám!")
try:
    print(szoveg[szam-1]*szam)
except:
    print("Sajnos nincs ilyen betű.")











