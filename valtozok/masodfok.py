import math
#a*x2+b*x+c

def egyenlet(a,b,c):
    szoveg = "0 = "
    if a != 0:
        szoveg += str(a) + "x²"
    if b > 0:
        szoveg += " + " + str(b) + "x"
    elif b < 0:
        szoveg += " " + str(b) + "x"
    if c > 0:
        szoveg += " + " + str(c)
    elif c < 0:
        szoveg += " " + str(c)

    return szoveg


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
    print("A megoldás x1:[], x2:[]".format(x1,x2))
    
print(egyenlet(a,b,c))
