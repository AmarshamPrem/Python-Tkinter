from tkinter import *
from tkinter import filedialog

# Functions

def openFile():
    filePath = filedialog.askopenfilename(initialdir="C:\\Users\\ADMIN\\OneDrive\\Desktop", 
                                          title="Open File", 
                                          filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py")))
    if filePath != "":
        with open(filePath) as f:
            data = f.read()
            print(data)
    else: print("No file was selected.")

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",title="Save the file as", filetypes=[("Text File", ".txt"), ("Python File", ".py")])
    if file != "":
        fileText = input("Enter your text here: ")
        file.write(fileText)
        file.close()

def cutText():
    print("Text cutted!")

def copyText():
    print("Text copied!")

def pasteText():
    print("Text pasted!")

# Creating Window 
window = Tk()

# Styling Window
window.title("Navbar Menu Program Tkinter")
window.geometry("300x500")
window.config(bg="light yellow")

# Creating Menu
menubar = Menu(window, font=("Candara", 15))
window.config(menu=menubar)

# Creating File Menu
fileMenu = Menu(menubar, tearoff=0, font=("Candara", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=quit)

# Creating Edit Menu
editMenu = Menu(window, tearoff=0, font=("Candara", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cutText)
editMenu.add_command(label="Copy", command=copyText)
editMenu.add_command(label="Paste", command=pasteText)


# Displaying Window
window.mainloop()