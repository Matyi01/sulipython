import math
from tkinter import *


class forgato:
    canvas=0
    vonalak=[]
    szog=0
    szogSebesseg=0.1
    szinek=[]
    
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak
        self.kozepSzamol()
    def rajzol(self):
        canvas.delete("all")
        self.szog+=self.szogSebesseg
        
        for i, betu in enumerate(self.vonalak):
            betu=self.eltol(betu,-self.kozep[0],-self.kozep[1])
            
            betu=self.forgat(betu,self.szog)
            
            betu=self.eltol(betu,200,200)
            
            betu=self.eltol(betu,self.kozep[0],self.kozep[1])
            
            self.canvas.create_line(betu,fill=self.szinek[i],width=5)

    def rajzol2(self):
        canvas.delete("all")
        self.szog+=self.szogSebesseg

        self.vonalak[0] = self.eltol(self.vonalak[0], 0, 0)
        self.vonalak[1] = self.eltol(self.vonalak[1], 900, 0)
        self.vonalak[2] = self.eltol(self.vonalak[2], 900, 0)
        self.vonalak[3] = self.eltol(self.vonalak[3], -330, 750)
        self.vonalak[4] = self.eltol(self.vonalak[4], -330, 750)
        self.vonalak[5] = self.eltol(self.vonalak[5], 500, 750)
        for betu in self.vonalak:
            self.canvas.create_line(betu,fill="red",width=5)
            
            
        

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

    
    def kozepSzamol(self):
        self.kozep=[0,0]
        db=0
        for betu in MATYI:
            xK=betu[::2]
            yK=betu[1::2]
            self.kozep[0]+=sum(xK)
            self.kozep[1]+=sum(yK)
            db+=len(xK)
            
        self.kozep[0]/=db
        self.kozep[1]/=db



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


elso=forgato(canvas,MATYI)
elso.szinek=["red","blue","blue","green","yellow","red",]


szog=0

"""
while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()
"""
elso.rajzol2()
        
win.mainloop()







