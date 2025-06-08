from tkinter import *

x = 0
def click():
    global x
    x += 1
    print(f"{x} ", end="")

window = Tk()
window.title("Button Program Tkinter")
window.geometry("300x200")
window.config(bg="gray")

photo = PhotoImage(file="logo.png")


button = Button(window,
                text="Click Me",
                command= click,
                font=("Audiowide", 30, "italic"),
                fg="green",
                bg="black",
                activebackground="black",
                activeforeground="green",
                image=photo,
                compound="top",
                state=ACTIVE)
button.pack()

window.mainloop()