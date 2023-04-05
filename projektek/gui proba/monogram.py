# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x300")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack()

# Add a line in canvas widget
canvas.create_line(10,10,30,10, fill="green", width=5)
canvas.create_line(30,10,90,60, fill="green", width=5)
canvas.create_line(90,60,150,10, fill="green", width=5)
canvas.create_line(150,10,170,10, fill="green", width=5)
canvas.create_line(150,170,170,170, fill="green", width=5)
canvas.create_line(10,170,30,170, fill="green", width=5)
canvas.create_line(10,10,10,170, fill="green", width=5)
canvas.create_line(30,30,30,170, fill="green", width=5)
canvas.create_line(170,10,170,170, fill="green", width=5)
canvas.create_line(150,30,150,170, fill="green", width=5)
canvas.create_line(30,30,90,80, fill="green", width=5)
canvas.create_line(90,80,150,30, fill="green", width=5)

pontok0 = [10,10,30,10,30,10,90,60,90,60,150,10,150,10,170,10,150,170,170,170,10,170,30,170,10,10,10,170,30,30,30,170,170,10,170,170,150,30,150,170,30,30,90,80,90,80,150,30]

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]

canvas.create_line(M, fill="red", width=5)










win.mainloop()
