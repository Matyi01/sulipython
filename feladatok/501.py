#Feladat 0501Készítsen programot amely összeadja a bekért számokat 0 végjelig!Mentés: zerovegjel
beSzam = 1
lista = 0
while beSzam != 0:
    beSzam = int(input("Adj meg egy számot (program lezárása: 0): "))
    lista += beSzam

print(lista)
