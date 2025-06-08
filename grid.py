from tkinter import *

# Creating Window 
window = Tk()

# Styling Window
window.title("Grid Program Tkinter")
window.geometry("450x700")

# Creating Form

heading = Label(window, text="Registration Form", font=("Agency FB", 25, "bold"))
heading.grid(row=0, column=0, columnspan=2)

Label(window, text="Enter First Name: ", width=20, padx=10, pady=10).grid(row=1, column=0)
Entry(window, width=40).grid(row=1, column=1)

Label(window, text="Enter Last Name: ", padx=10, pady=10).grid(row=2, column=0)
Entry(window, width=40).grid(row=2, column=1)

Label(window, text="Enter Email: ", padx=10, pady=10).grid(row=3, column=0)
Entry(window, width=40).grid(row=3, column=1)

Button(window, text="Submit", padx=10, pady=5).grid(row=4, column=0, columnspan=2)


# Displaying Window
window.mainloop()