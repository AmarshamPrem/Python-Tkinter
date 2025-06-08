from tkinter import *

# Functions 
def submit():
    value = text.get("1.0", END)
    print(value)

# Creating Window 
window = Tk()

# Styling Window
window.title("Text Widget Program Tkinter")
window.geometry("400x700")
window.config(bg="#333333")

# Creating Text Widget 
text = Text(window, 
            bg="light yellow",
            fg="#121212",
            # font=("Bradley Hand ITC", 20, "bold"),
            # font=("Gabriola", 20),
            font=("Ink Free", 20, "bold"),
            width=25,
            height=10,
            padx=10,
            pady=10)
text.pack()

# Creating Submit Button
submitButton = Button(window, text="Submit", command=submit, padx=10, pady=10, font=("Consontia", 20))
submitButton.pack()

# Displaying Window
window.mainloop()