szamok=[]
for i in range(0,8):
    szamok.append(int(input("Adj meg egy srámot: ")))
print(szamok)
print(szamok[0:4])
print(szamok[4:8])
osszeg = szamok[0] + szamok[1] + szamok[2] + szamok[3] + szamok[4] + szamok[5] + szamok[6] + szamok[7]
print(osszeg)
szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
betu = ""
while betu != "end":
    betu = input("Adj meg egy betűt: ")
    print(szoveg.count(betu))
print(szoveg[::-1])
szoveg.replace("orna","")
print(len(szoveg))

def fenyo():
    x = ""
    while x == "":
        x = input("Adj meg egy karaktert: ")
    fenyo = """
               {x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
               {x}
              {x}{x}{x}   
            """
    print(fenyo.format(x=x))
    
fenyo()
