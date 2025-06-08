from tkinter import *
from tkinter.ttk import *
import time

# Functions

def start():
    GB = 343
    for i in range(1, 101):
        if i == 100:
            download.set("Downloading Completed.")
            percent.set("100% Downloaded")
            progress.set("")
        download.set("Downloading Call Of Duty: Warzone IV")
        bar["value"] += 1
        time.sleep(0.05)
        percent.set(f"{i}% Downloaded")
        progress.set(f"{int((GB/100)*i)}GBs Downloaded out of {GB}GBs.")
        window.update_idletasks()

# Creating Window 
window = Tk()

# Styling Window
window.title("Progress Bar Program Tkinter")
window.geometry("450x200")

# Creating Download Variable
download = StringVar()
Label(window, textvariable=download, font=("Arial", 15)).pack()

# Creating the Progress Bar
bar = Progressbar(window, orient=HORIZONTAL, length=350)
bar.pack(pady=10)

# Representing Progress Bar in Text
progress = StringVar()
Label(window, textvariable=progress).pack()

# Creating Percent Variable
percent = StringVar()
perLbl = Label(window, textvariable=percent).pack()

# Creating Download Button
Button(window, text="Download", command=start).pack()

# Displaying Window
window.mainloop()