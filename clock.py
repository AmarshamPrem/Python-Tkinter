from tkinter import *
from time import *

# Functions 

def update():
    tim = strftime("%I : %M : %S %p")
    date = strftime("%A, %d %B")
    year = strftime("%Y")
    timelabel.config(text=tim)
    daylabel.config(text=date)
    yearlabel.config(text=year)
    window.after(1000, update)

# Creating Window 
window = Tk()

# Styling Window
window.title("Clock Program Tkinter")
window.geometry("600x300")
window.config(bg="black")

# Time Label

timelabel = Label(window, font=("Audiowide", 50), fg="#00ff00", bg="black") 
timelabel.pack()

daylabel = Label(window, font=("Audiowide", 35), fg="#00ff00", bg="black") 
daylabel.pack()

yearlabel = Label(window, font=("Audiowide", 75), fg="#00ff00", bg="black") 
yearlabel.pack()

update()

# Displaying Window
window.mainloop()