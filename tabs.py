from tkinter import *
from tkinter import ttk

# Creating Window 
window = Tk()

# Styling Window
window.title("Tabs Program Tkinter")
window.geometry("400x700")
window.config(bg="#232323")

# Creating a Notebook
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")

notebook.pack(fill="both", expand=True)

Label(tab1, text="Hey there it is tab1", width=50, height=25).pack()
Label(tab2, text="Good bye nice to meet u :)", width=50, height=25).pack()

# Displaying Window
window.mainloop()