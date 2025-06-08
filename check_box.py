from tkinter import *

# Creating Display Function
def display():
    if (x.get() == 1): print("You agree!")
    else: print("You don't agree :(")

# Creating Window
window = Tk() 

# Styling The Window
window.title("Check Box Program Tkinter")
window.geometry("400x400")
window.config(bg="gray")

# Import Image for Check Box
photo = PhotoImage(file="circles.png")

# Getting the value of x
x = IntVar()

# Making Check Box
check_button = Checkbutton(window, 
                           text="I agree",
                           bg="black",
                           fg="#00ff00",
                           font=("Audiowide", 25, "bold"),
                           activebackground="black",
                           activeforeground="#00ff00",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT)
check_button.pack()

window.mainloop() # Displaying Window