# Import the required libraries
from tkinter import *
import math

class forgato0:
    canvas = 0
    vonalak = []
    def __init__(self,canvas,vonalak):
        self.canvas = canvas
        self.vonalak = vonalak
    def rajzol(self):
        canvas.delete("all")
        #szog += 0.1
        for i,betu in enumerate(self.vonalak):
            betu = nagyit(betu,0.7)
            betu = eltol(betu,-kozep[0],-kozep[1])
            betu = forgat(betu,szog)
            betu = eltol(betu,kozep[0],kozep[1])
            betu = eltol(betu,400,400)
            self.canvas.create_line(betu, fill="black", width=5)
class forgato:
    canvas=0
    vonalak=[]
    szog=0
    szogSebesseg=1

    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak
    def rajzol(self):
        canvas.delete("all")
        self.szog+=self.szogSebesseg
        
        for betu in self.vonalak:
            betu=self.eltol(betu,-kozep[0],-kozep[1])
            
            betu=self.forgat(betu,self.szog)
            
            betu=self.eltol(betu,400,200)
            
            betu=self.eltol(betu,kozep[0],kozep[1])
            
            self.canvas.create_line(betu,fill="black",width=5)


    def eltol(self,pontok,x,y):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==1:
                vissza.append(pont+y)
            else:
                vissza.append(pont+x)
        return vissza

    def nagyit(self,pontok,meret=1):
        vissza=[]
        for pont in pontok:
            vissza.append(pont*meret)
        return vissza


    def forgat(self,pontok,szog):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2 == 0:
                
                
                x=pontok[i]*math.cos(math.radians(szog))-pontok[i+1]*math.sin(math.radians(szog))
                
                y=pontok[i]*math.sin(math.radians(szog))+pontok[i+1]*math.cos(math.radians(szog))
                
                vissza.append(x)
                vissza.append(y)
        return vissza        



win=Tk()

win.geometry("1920x1080")

canvas=Canvas(win, width=500, height=300,bg="skyblue")
canvas.pack(fill = BOTH, expand =1)




AKOS=[[0,375,125,125,250,375,175,375,150,300,100,300,75,375,0,375,],
      [100,250,125,200,150,250,100,250,],
      [175,150,175,100,200,100,200,150,175,150,],
      [250,375,250,125,333,125,333,250,416,125,500,125,417,250,500,375,416,375,360,300,333,375,250,375,],
      [500,125,750,125,750,375,500,375,500,125,],
      [550,175,700,175,700,325,550,325,550,175,],
      [1000,125,750,125,750,249,936,249,936,311,750,311,750,375,1000,375,1000,210,812,210,810,160,1000,160,1000,125,]]




elso=forgato(canvas,AKOS)


kozep=[0,0]
db=0
for betu in AKOS:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)
    
kozep[0]/=db
kozep[1]/=db


szog=0


while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()

        
    #win.mainloop()




def eltol(pontok, x, y):
    vissza = []
    for e, pont in enumerate(pontok):
        if e % 2 == 0:
            vissza.append(pont + x)
        else:
            vissza.append(pont + y)
    return vissza

def nagyit(pontok, meret = 1):
    vissza = []
    for e in pontok:
            vissza.append(e * meret)
    return vissza

def forgat(pontok, szog):
    vissza = []
    for i, pont in enumerate(pontok):
        if i % 2 == 0:
            szogRadian = math.radians(szog)
            x = pontok[i] * math.cos(szogRadian) - pontok[i + 1] * math.sin(szogRadian)
            y = pontok[i] * math.sin(szogRadian) + pontok[i + 1] * math.cos(szogRadian)
            vissza.append(x)
            vissza.append(y)
    return vissza

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("900x300")

# Create a canvas widget
canvas=Canvas(win, width=900, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
A1 = [180,170,200,170,220,130,300,130,320,170,340,170,270,10,250,10,180,170]
A2 = [230,110,290,110,260,30,230,110]
T = [350,10,510,10,510,30,440,30,440,170,420,170,420,30,350,30,350,10]
Y = [520,10,540,10,610,70,680,10,700,10,620,82,620,170,600,170,600,82,520,10]
I = [710,10,730,10,730,170,710,170,710,10]

MATYI = [#M
        [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10],
        #A
        [180,170,200,170,220,130,300,130,320,170,340,170,270,10,250,10,180,170],
        [230,110,290,110,260,30,230,110],
        #T
        [350,10,510,10,510,30,440,30,440,170,420,170,420,30,350,30,350,10],
        #Y
        [520,10,540,10,610,70,680,10,700,10,620,82,620,170,600,170,600,82,520,10],
        #I
        [710,10,730,10,730,170,710,170,710,10]]

elso = forgato(canvas,MATYI)


kozep = [0, 0]
db = 0
for betu in MATYI:
    xK = betu[::2]
    yK = betu[1::2]
    kozep[0] += sum(xK)
    kozep[1] += sum(yK)
    db += len(xK)
kozep[0] /= db
kozep[1] /= db

szog = 0
while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()
    #win.mainloop()
    
