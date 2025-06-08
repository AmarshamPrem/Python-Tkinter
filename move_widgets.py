from tkinter import *

# Functions

def move(event):
    if event.keysym.lower() == "w" or event.keysym.lower() == "up":
        label.place(x=label.winfo_x(), y=label.winfo_y()-10)
    elif event.keysym.lower() == "s" or event.keysym.lower() == "down":
        label.place(x=label.winfo_x(), y=label.winfo_y()+10)
    elif event.keysym.lower() == "d" or event.keysym.lower() == "right":
        label.place(x=label.winfo_x()+10, y=label.winfo_y())
    elif event.keysym.lower() == "a" or event.keysym.lower() == "left":
        label.place(x=label.winfo_x()-10, y=label.winfo_y())
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
label = Label(window, image=image)
label.place(x=0, y=0)

# Displaying Window
window.mainloop()