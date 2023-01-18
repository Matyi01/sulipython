import random

def szoBeker():
    szo = input("Kérek egy szót: ")
    if szo == "":
        jelentes = ""
    else:
        jelentes = input(szo + " jelentése: ")
    return[szo, jelentes]

szavak = []
def sokBeker():
    szo = szoBeker()
    while szo[0] != "":
        szavak.append(szo)
        szo = szoBeker()

    return szavak

def filebaIr(lista):
    f = open("szotar2.txt","a")

    f.close()
