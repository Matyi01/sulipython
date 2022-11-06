import math
#a*x2+b*x+c

a = ""
while a == "":
    try:
        a = int(input("a = "))
    except ValueError:
        print("Ez nem szám!")
    except:
        print("Ismeretlen hiba!")

b = ""
while b == "":
    try:
        b = int(input("b = "))
    except ValueError:
        print("Ez nem szám!")
    except:
        print("Ismeretlen hiba!")

c = ""
while c == "":
    try:
        c = int(input("c = "))
    except ValueError:
        print("Ez nem szám!")
    except:
        print("Ismeretlen hiba!")

diszkriminans = b*b-4*a*c
if diszkriminans < 0:
    print("Nincs megoldás")
elif diszkriminans == 0:
    megoldas = -b/(2*a)
    print("Egy megoldás {}".format(megoldas))
else:
    x1 = (-b-math.sqrt(diszkriminans))/(2*a)
    x2 = (-b+math.sqrt(diszkriminans))/(2*a)
    
