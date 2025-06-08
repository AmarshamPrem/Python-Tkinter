from tkinter import *

# Functions

def showKey(event):
    label.config(text=event.keysym)

# Creating Window 
window = Tk()

# Styling Window
window.title("Key Board Events Program Tkinter")
window.geometry("500x300")
window.config(bg="black")

# Adding Event Listener
window.bind("<Key>", showKey)

# Adding Label
label = Label(window, font=("Cooper", 100))
label.pack()

# Displaying Window
window.mainloop()