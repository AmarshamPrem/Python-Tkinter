from tkinter import *
from tkinter import messagebox

#| Functions
def click():
    # messagebox.showinfo(title="Information", message="This is an info message. You can click ok after you read this. This just informs you about something.")
    # messagebox.showwarning(title="Warning", message="This is a warning to you. You better not watch porn on sites expect pornhub.com. If you do your data will be leaked. The proof is that I knew this about you.")
    # messagebox.showerror(title="An Error Occured", message="This is a error. Unfortunatly an error has occured in the terminal. If you do not execute the windows defender, your computer will be hacked.")
    # isDate = messagebox.askokcancel(title="Question", message="Would you like to date me?")

    # if isDate:
    #     print("Great! Where would you like it?")
    # else: 
    #     isDate = messagebox.askretrycancel(title="Please", message="Ohh! Come on we know. We love each other.")
    #     if isDate:
    #         print("Great! Where would you like it?")
    #     else: 
    #         print("I understand. Have a nice day!")

    isDate = messagebox.askyesno(title="Question", message="Would you like to date me?", icon="info")
    if isDate:
        print("Great! Where would you like it?")
    else: 
        print("I understand. Have a nice day!")

    # messagebox.askquestion(title="Hey, Answer Honestly!!", message="Do you love me?")

#| Creating Window 
window = Tk()

#| Styling Window
window.title("Message Box Program Tkinter")
window.config(bg="black")

#| Creating an Info Button
button = Button(window, command=click, text="Click")
button.pack()

#| Displaying Window
window.mainloop()