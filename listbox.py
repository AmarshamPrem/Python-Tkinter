from tkinter import *

# Creating functions
def order(): # Function to order an Item
    curSel = listbox.curselection()
    if curSel:
        print("Successfully ordered!")
        i = 1
        for ind in curSel:
            print(f"    {i}). {listbox.get(ind)}")
            i += 1


def addItem(): # Function to add an Item
    item = newItem.get()
    foodList.append(item)
    listbox.insert(len(foodList)-1, item)
    print(f"Successfully Added {item}!")
    setHeight()

def delItem(): # Function to delete an Item
    curSel = listbox.curselection()
    print("Successfully Removed!")
    i = 1
    for ind in reversed(curSel):
        item = listbox.get(ind)
        foodList.remove(item)
        listbox.delete(ind)
        print(f"    {i}). {item}")
        i += 1
    setHeight()

def setHeight(): # Function to set the height of the ListBox
    listbox.config(height=listbox.size())


# Creating Window 
window = Tk()

# Styling Window
window.title("Listbox Program Tkinter")
window.config(bg="black")

# Creating the listbox
foodList = ["Pizza", "Fries", "Apple", "Soda", "Biryani", "Paneer", "Ice Cream", "Salad", "Chai"]
listbox = Listbox(window, 
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  selectmode=MULTIPLE,
                  width=12)
listbox.pack()

for food in foodList:
    ind = foodList.index(food)
    listbox.insert(ind, food)
setHeight()

# Creating an Input Entry for Any New Item
newItem = Entry(window, 
                fg="black", 
                bg="#f7ffde",
                font=("Consonatia", 35),
                width=10)
newItem.pack()
newItem.insert(0, "New Item")

# Creating a Submit Button
subBtn = Button(window, text="Submit", command=order, padx=10)
subBtn.pack()

# Creating Submit Button for Input Field
addBtn = Button(window, text="Add Item", command=addItem, padx=10)
addBtn.pack()

# Creating the Delete Button
delBtn = Button(window, text="Remove Item", command=delItem, padx=10)
delBtn.pack()

# Displaying Window
window.mainloop()