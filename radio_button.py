from tkinter import *

# Creating display function

def display():
    print(f"Placed an order for {foodList[x.get()]}")

# Creating Window 
window = Tk()

# Styling Window
window.title("Radio Button Program Tkinter")
window.geometry("250x400")
window.config(bg="black")

# Creating Radio Buttons

foodList = ["Pizza", "Burger", "Fries"]

x = IntVar()

for food in foodList:
    radioButton = Radiobutton(window, 
                              text=food,
                              font=("Audiowide", 15, "italic"),
                              variable=x,
                              value=foodList.index(food),
                              command=display,
                            #   indicatoron=0,
                            #   width=400,
                              background="black",
                              fg="#00ff00",
                              activebackground="black",
                              activeforeground="#00ff00",
                              padx=25,
                              pady=10)
    radioButton.pack(anchor=W)



# Displaying Window
window.mainloop()