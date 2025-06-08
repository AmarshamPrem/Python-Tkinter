from tkinter import *

def submit():
    entryValue = entry.get()
    print("Hello " + entryValue)

def delete():
    entry.delete(0, END)

def backSpace():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1, END)

window = Tk()
window.title("Input Box Program Tkinter")
window.geometry("300x200")
window.config(bg="gray")

entry = Entry(window,
              font=("Audiowide", 40, "bold"),
              fg="green",
              bg="black",)

# entry.insert(0, "Enter Your Name") to add default text
# entry.config(state=DISABLED) to disable input 
# entry.config(show="*") to hide input

entry.pack(side=LEFT)

submit_button = Button(window, 
                       text="Submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backSpace_button = Button(window, 
                          text="BackSpace",
                          command= backSpace)
backSpace_button.pack(side=RIGHT)

window.mainloop()