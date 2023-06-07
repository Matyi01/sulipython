import modul

teglalapok = [[10, 20]
,[30, 40]
,[50, 10]
,[70, 5]
,[10, 10]]

for i,e in enumerate(teglalapok):
    print(f"A(z) {i+1}. téglalap hosszúsága: {e[0]}, magassága: {e[1]}")

adatok = []
for e in teglalapok:
    adatok.append(modul.szamitas(*e))

keruletek = []
for e in adatok:
    keruletek.append(modul.szamitas.kerulet(e))
print(f"Legnagyobb kerület: {max(keruletek)}")

teruletek = []
for e in adatok:
    teruletek.append(modul.szamitas.terulet(e))
print(f"Legnagyobb terület: {max(teruletek)}")
