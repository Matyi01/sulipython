#Feladat 0608Írjon programot, amely megkérdezi, milyen számokkal szeretnénk dolgozni: „Egész/Valós?” A program kérjen be egy 'E' vagy egy 'V' betűt. Ha a felhasználó 'E' betűt választja akkor deklaráljunk egy egészeket tárolni képes változót és kérjünk be egy egész számot. Ha a 'V' betűt valós számokat tárolni képes változót deklaráljunk és kérjünk be egy valós számot. A bekért értéket szorozzuk meg kettővel, az eredményt írjuk a képernyőre.Mentés: duplami
E = 0
V = 0.0
EV = input("Egész/Valós? ")
if EV == "E":
    E = int(input("Írj be egy egész számot: "))
    print(E*2)
elif EV == "V":
    V = float(input("Írj be egy valós számot: "))
    print(V*2)
