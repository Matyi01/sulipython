# Import the required libraries
from tkinter import *

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

canvas.create_line(M, fill="black", width=5)
canvas.create_line(A1, fill="black", width=5)
canvas.create_line(A2, fill="black", width=5)
canvas.create_line(T, fill="black", width=5)
canvas.create_line(Y, fill="black", width=5)
canvas.create_line(I, fill="black", width=5)

win.mainloop()
