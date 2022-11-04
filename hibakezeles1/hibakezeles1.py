lista = ["Bence","László","Ferenc"]
lista.append("Martin")
try:
    print(lista[3])
except:
    print("Valami nem jó!")
else:
    print("Sikeres lefutás!")
finally:
    print("Ez a vége.")

szam = ""
while szam == "":
    try:
        szam = int(input("Kérek egy számot: "))
    except ValueError:
        print("Ez nem szám!")
    except:
        print("ismeretlen hiba!")
print(szam)
