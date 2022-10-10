beSzam = 0

while beSzam < 2 or beSzam > 5:
    beSzam = int(input("Adj meg egy számot 2 és 5 között: "))

autok = []
for i in range(0, beSzam):
    autok.append(input("Kérem az "+str(i+1)+". autó márkát: "))

print(autok)
