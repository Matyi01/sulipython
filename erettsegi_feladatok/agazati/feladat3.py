def ido2mp():
    pass





eredmenyek = []

f = open("triatlon.txt")
for egysor in f:
    temp = egysor.replace("\n","").split(";")
    eredmenyek.append(temp)
f.close()

eredmenyek.pop(0)

print("2. feladat: A versenyen {} induló volt.".format(len(eredmenyek)))






