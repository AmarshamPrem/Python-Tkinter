from tkinter import *
from tkinter import colorchooser

# Functions

def click():
    color = colorchooser.askcolor()
    window.config(bg=color[1])

# Creating Window 
window = Tk()

# Styling Window
window.title("Color Chooser Program Tkinter")
window.geometry("420x420")
window.config(bg="black")

# Button 
button = Button(window, command=click, text="Choose Color")
button.pack()

# Displaying Window
window.mainloop()