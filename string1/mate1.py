a = 0
a = int(input("Hány számot szeretnél összeadni? "))
while a < 2 or a > 5:
    print("Hiba! Kérlek, egy 2 és 5 közötti számot adj meg.")
    a = int(input("Hány számot szeretnél összeadni? "))
if a == 2:
    szam1 = int(input("1. Szám: "))
    szam2 = int(input("2. Szám: "))
    print("A megadott 2 szám összege: "+str(szam1+szam2))
elif a == 3:
    szam1 = int(input("1. Szám: "))
    szam2 = int(input("2. Szám: "))
    szam3 = int(input("3. Szám: "))
    print("A megadott 3 szám összege: "+str(szam1+szam2+szam3))
elif a == 4:
    szam1 = int(input("1. Szám: "))
    szam2 = int(input("2. Szám: "))
    szam3 = int(input("3. Szám: "))
    szam4 = int(input("4. Szám: "))
    print("A megadott 4 szám összege: "+str(szam1+szam2+szam3+szam4))
elif a == 5:
    szam1 = int(input("1. Szám: "))
    szam2 = int(input("2. Szám: "))
    szam3 = int(input("3. Szám: "))
    szam4 = int(input("4. Szám: "))
    szam5 = int(input("5. Szám: "))
    print("A megadott 5 szám összege: "+str(szam1+szam2+szam3+szam4+szam5))
