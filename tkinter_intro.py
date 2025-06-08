from tkinter import *

window = Tk()
icon = PhotoImage(file="logo.png")

window.title("My First GUI Prgoram Tkinter")
window.geometry("250x400")
window.iconphoto(True, icon)
window.config(bg="black")

window.mainloop()