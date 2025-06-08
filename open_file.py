from tkinter import *
from tkinter import filedialog

# Functions 

def uploadFile():
    filePath = filedialog.askopenfilename(initialdir="C:\\Users\\ADMIN\\OneDrive\\Desktop", 
                                          title="Select Text File", 
                                          filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py")))
    # with open(filePath) as f:
    #     data = f.read()
    if filePath != "":
        fileData = open(filePath).read()
        print(fileData)
    else: print("No file was selected.")

# Creating Window 
window = Tk()

# Styling Window
window.title("Open File Program Tkinter")
window.geometry("400x700")
window.config(bg="black")

# Creating Button To Upload a File
button = Button(window, 
                text="Upload File", 
                command=uploadFile, 
                font=("Consonatia", 20, "bold"), 
                padx=10, 
                pady=10, 
                bg="light yellow", 
                activebackground="light yellow")
button.pack()

# Displaying Window
window.mainloop()