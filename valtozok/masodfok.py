import math
#a*x2+b*x+c
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
diszkriminans = b*b-4*a*c
if diszkriminans < 0:
    print("Nincs megoldás")
elif diszkriminans == 0:
    megoldas = -b/(2*a)
    print("Egy megoldás {}".format(megoldas))
else:
    x1 = (-b-math.sqrt(diszkriminans))/(2*a))
    x2 = (-b+math.sqrt(diszkriminans))/(2*a))
    
