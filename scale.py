from tkinter import *

# Creating Window 
window = Tk()

# Styling Window
window.title("Scale Program Tkinter")
window.geometry("480x800")
window.config(bg="black")

# Creating Scale
scale = Scale(window, 
              from_=100, 
              to=0, 
              length=600,
              fg="#ff1c00",
              bg="#333333",
              orient=VERTICAL, # orientaion of the scale VERTICAL or HORIZONTAL
              font=("Gabriola", 25, "bold"),
              tickinterval=10, # Adds Numeric Indicators
              resolution=5, # increment of the slider 
              showvalue=0, # shows the Current Value if 1
              troughcolor="#69eaff" # Sets the Slider Color
              )
scale.set((scale["from"] + scale["to"])/2) # Sets the Default Value of the Slider
scale.pack()

submitButton = Button(window, 
                      text="Submit", 
                      command=lambda: print(f"The temprature is {scale.get()} degree Celsius"),
                      font=("Cascadia Mono", 15, "bold"))
submitButton.pack()

# Displaying Window
window.mainloop()