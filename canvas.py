from tkinter import *

# Creating Window 
window = Tk()

# Styling Window
window.title("Canvas Program Tkinter")
window.geometry("600x600")
window.config(bg="black")

# Creating Canvas
canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0,0,500,500, fill="green", width=200)
# canvas.create_line(0,500,500,0, fill="green", width=200)
# canvas.create_oval(120, 120, 380, 380, fill="red")
# canvas.create_rectangle(200, 0, 400, 300, fill="blue")
canvas.create_oval(200, 200, 300, 300, fill="green", outline="black", width=3)
canvas.create_arc(480, 480, 20, 20, style=PIESLICE, extent=300, start=30, fill="yellow", outline="black", width="5")
canvas.pack()

# Displaying Window
window.mainloop()