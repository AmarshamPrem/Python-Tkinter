from tkinter import *

# Functions

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

# Creating Window 
window = Tk()

# Styling Window
window.title("Dragable Widgets Program Tkinter")
window.geometry("900x900")
window.config(bg="black")

# Creating the dragable label
label = Label(window, bg="red", width=10, height=5)
label.place(x=0,y=0)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=0,y=0)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

# Displaying Window
window.mainloop()