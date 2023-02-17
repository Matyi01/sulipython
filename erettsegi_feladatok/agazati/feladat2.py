import haromszog

def ujabb(darab=3):
    haromszogek = []
    for i in range(darab):
        print(str(i+1)+". adatsor")
        haromszogek.append(haromszog.haromszog())
    for e in haromszogek:
        print("\ta={}, b={}, c={}".format(e[0],e[1],e[2]))
    return haromszogek

def haromszoge(haromszogek):
    for e in haromszogek:
        if sum(e) - max(e) > max(e):
            print("Lehet háromszög")
        else:
            print("Nem lehet háromszög")

h = ujabb(3)
haromszoge(h)


