# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x300")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="gray")
canvas.pack()

# Add a line in canvas widget
canvas.create_line(10,10,210,10, fill="green", width=5)
canvas.create_line(10,10,10,210, fill="green", width=5)
canvas.create_line(10,210,210,210, fill="green", width=5)
canvas.create_line(210,10,210,210, fill="green", width=5)

canvas.create_line(300,10,250,210, fill="red", width=5)
canvas.create_line(300,10,350,210, fill="red", width=5)
canvas.create_line(250,210,350,210, fill="red", width=5)






win.mainloop()
