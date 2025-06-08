from tkinter import *
import time

WIDTH  = 400
HEIGHT = 700
XVelocity = 1
YVelocity = 1

# Creating Window 
window = Tk()

# Styling Window
window.title("2D Animations Program Tkinter")
window.geometry("400x700")

# Creating Canvas
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

photoimage = PhotoImage(file="circles.png")
image = canvas.create_image(0,0,image=photoimage, anchor=NW)

imageWidth = photoimage.width()
imageHeight = photoimage.height()

while True:
    coords = canvas.coords(image)
    if (coords[0]>= WIDTH - imageWidth or coords[0]<0):
        XVelocity *= -1
    if (coords[1]>= HEIGHT - imageHeight or coords[1]<0):
        YVelocity *= -1
    canvas.move(image, XVelocity, YVelocity)
    print(coords)
    window.update()
    time.sleep(0.01)

# Displaying Window
window.mainloop()