from tkinter import *

# Functions

def showCords(event):
    print(f"You clicked on ({event.x}, {event.y})")

# Creating Window 
window = Tk()

# Styling Window
window.title("Mouse Events Program Tkinter")
window.geometry("300x300")
window.config(bg="black")

# Adding Event Listener
# window.bind("<Button-1>", showCords)
# window.bind("<Enter>", showCords)
# window.bind("<Leave>", showCords)
# window.bind("<ButtonRelease>", showCords)
# window.bind("<Motion>", showCords)

# Displaying Window
window.mainloop()