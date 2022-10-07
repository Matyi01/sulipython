szam1 = input("Első szám: ")
szam2 = input("Második szám: ")
muvelet = input("Művelet: ")
if muvelet == "+":
    print(int(szam1) + int(szam2))
elif muvelet == "-":
        print(int(szam1) - int(szam2))
elif muvelet == "*":
        print(int(szam1) * int(szam2))
elif muvelet == "/":
        print(int(szam1) / int(szam2))
elif muvelet == "//":
        print(int(szam1) // int(szam2))
elif muvelet == "**":
        print(int(szam1) ** int(szam2))
elif muvelet == "%":
        print(int(szam1) % int(szam2))

