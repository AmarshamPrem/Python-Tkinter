from tkinter import *
from tkinter import filedialog

# Functions
def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",title="Save the file as", filetypes=[("Text File", ".txt"), ("Python File", ".py")])
    fileText = str(textarea.get("1.0", END))
    file.write(fileText)
    file.close()


# Creating Window 
window = Tk()

# Styling Window
window.title("Save File Program Tkinter")
window.geometry("400x700")
window.config(bg="light yellow")

# Creating Save Button
saveBtn = Button(window, text="Save File", command=saveFile, font=("Ink Free", 15, "bold"))
saveBtn.pack(side=TOP)

# Creating Textarea
textarea = Text(window, font=("Ink Free", 15, "bold"))
textarea.pack()

# Displaying Window
window.mainloop()