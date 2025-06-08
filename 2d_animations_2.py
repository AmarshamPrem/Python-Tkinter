from tkinter import *
from Ball_Module import *
import time

WIDTH  = 500
HEIGHT = 500

# Creating Window 
window = Tk()

# Styling Window
window.title("2D Animations Program Tkinter")
window.geometry("500x500")

# Creating Canvas
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

ball1 = Ball(canvas, 0, 0, 100, 2, 2, "red")
ball2 = Ball(canvas, 0, 0, 50, 3, 2, "orange")
ball3 = Ball(canvas, 0, 0, 10, 4, 3, "blue")
ball4 = Ball(canvas, 0, 0, 200, 1, 2, "green")
while True:
    ball1.move()
    ball2.move()
    ball3.move()
    ball4.move()
    window.update()
    time.sleep(0.01)

# Displaying Window
window.mainloop()