from tkinter import *

# Creating Window 
window = Tk()

# Styling Window
window.title("Frames Program Tkinter")
window.geometry("400x700")
window.config(bg="light yellow")

# Creating Frame
frame = Frame(window)
frame.pack()

# Creating Buttons
btns = ["W", "A", "S", "D"]
for btn in btns:
    if btn == "W": side = "top"
    else: side = "left"
    Button(frame, text=btn, font=("Consolas", 25), width=3).pack(side=side)

# Displaying Window
window.mainloop()