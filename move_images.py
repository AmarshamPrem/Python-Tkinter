from tkinter import *

# Functions

def move(event):
    if event.keysym.lower() == "w" or event.keysym.lower() == "up":
        canvas.move(canvasImage, 0, -10)
    elif event.keysym.lower() == "s" or event.keysym.lower() == "down":
        canvas.move(canvasImage, 0, 10)
    elif event.keysym.lower() == "d" or event.keysym.lower() == "right":
        canvas.move(canvasImage, 10, 0)
    elif event.keysym.lower() == "a" or event.keysym.lower() == "left":
        canvas.move(canvasImage, -10, 0)
    else:
        return

# Creating Window 
window = Tk()

# Styling Window
window.title("Move Widget Progarm Tkinter")
window.geometry("400x400")
window.config(bg="#232323")

# Adding Event Listener on Window
window.bind("<Key>", move)

# Creating Label
image = PhotoImage(file="circles.png")
canvas = Canvas(window, width=500, height=500)
canvasImage = canvas.create_image(0,0, image=image, anchor=NW)
canvas.pack()

# Displaying Window
window.mainloop()