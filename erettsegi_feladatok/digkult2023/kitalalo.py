import modul

f = open("szavak.txt")

sorok = []
for e in f:
    sorok.append(e.strip())



f.close()
