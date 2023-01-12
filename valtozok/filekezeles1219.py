f = open("proba.txt","w")

f.write("Hello")
f.write("\n")
f.write("világ")

f.close()

f = open("proba.txt","r")

szoveg = f.read()

sorok = szoveg.split("\n")
print(sorok)

f.close()

f = open("proba.txt","r")

sorok = []
for sor in f:
    sorok.append(sor.replace("\n","").replace("\r",""))

print(sorok)

f.close()

#hf:

f = open("proba.txt","w")

x = "a"
while x != "":
    x = input("Irj be valamit: ")
    f.write(x)
    f.write("\n")

f.close()

f = open("proba.txt","r")

for x in f:
    print(x.replace("\n",""))

f.close()
