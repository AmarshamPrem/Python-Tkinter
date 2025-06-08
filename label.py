from tkinter import *

window = Tk()
# window.geometry("360x460")
window.title("Label Program Tkinter")

# icon = PhotoImage(file="logo.png")
# window.iconphoto(True, icon)

photo = PhotoImage(file="logo.png")
window.config(background="#525954")

label = Label(window,
            text="Hello World!", 
            font=("Audiowide", 40, "bold"), 
            fg="green", 
            bg="#525954",
            relief=RAISED,
            bd=10,
            padx=50,
            pady=50,
            image=photo,
            compound="bottom")

# label.place(x=0, y=0)
label.pack()

window.mainloop()