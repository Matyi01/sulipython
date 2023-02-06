f = open("valaszok.txt")

adatok = f.read().split("\n")[:-1]
#adatok.remove("")
#adatok = adatok[:-1]
f.close()

helyes = adatok[0]
adatok.pop(0)

valaszok = []
for e in adatok:
    valaszok.append(e.split(" "))

    
print(valaszok)
