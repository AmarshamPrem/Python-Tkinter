from tkinter import *

# Functions

def createNewWin():
    # window.destroy() # Destroys the Main Window
    # newWindow = Tk() # Creates new Independent Window
    # newWindow.mainloop()
    newWin = Toplevel() # Creates a Window Dependent on the Main Window


# Creating Window 
window = Tk()

# Styling Window
window.title("Create New Window Program Tkinter")
window.geometry("400x400")
window.config(bg="black")

# Creating a Button
button = Button(window, text="Create New Window", command=createNewWin)
button.pack()

# Displaying Window
window.mainloop()