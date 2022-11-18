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

def gyoktenyezosszorzat(a,x1,x2):
    if x1 == "":
        return "Nincs gyöktényezős alak."
    elif x1 == x2:
        if x1 < 0:
            return str(a)+"(x + "+str((-1*x1))+")²"
        elif x1 > 0:
            return str(a)+"(x - "+str((-1*x1))+")²"
        else:
            return str(a)+"x²"
    else:
        if x1 < 0:
            if x2 < 0:
                return str(a)+"(x + "+str((-1*x1))+")(x + "+str((-1*x2))+")"
            elif x2 > 0:
                return str(a)+"(x + "+str((-1*x1))+")(x - "+str(x2)+")"
            else:
                return str(a)+"(x + "+str((-1*x1))+")x"
        if x1 > 0:
            if x2 < 0:
                return str(a)+"(x - "+str(x1)+")(x + "+str((-1*x2))+")"
            elif x2 > 0:
                return str(a)+"(x - "+str(x1)+")(x - "+str(x2)+")"
            else:
                return str(a)+"(x - "+str(x1)+")x"
        else:
            if x2 < 0:
                return str(a)+"x(x + "+str((-1*x2))+")"
            else:
                return str(a)+"x(x - "+str(x2)+")"




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

x1 = ""
x2 = ""

diszkriminans = b*b-4*a*c
if diszkriminans < 0:
    print("Nincs megoldás")
elif diszkriminans == 0:
    megoldas = -b/(2*a)
    x1 = megoldas
    x2 = megoldas
    print("Egy megoldás x1:{}".format(megoldas))
else:
    x1 = (-b-math.sqrt(diszkriminans))/(2*a)
    x2 = (-b+math.sqrt(diszkriminans))/(2*a)
    print("A megoldás x1:[], x2:[]".format(x1,x2))
    
print(egyenlet(a,b,c))

#a*(x-x1)*(x-x2)=0

print(a)
print(x1)
print(x2)

print(gyoktenyezosszorzat(a,x1,x2))
