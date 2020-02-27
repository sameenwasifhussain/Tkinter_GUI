from tkinter import *

# Creating Root Widget
root = Tk()

# Global Variables
r = 1

# Function For Button Click Output
def buttonClick():
    global r
    myLabel = Label(root, text = "New Label")
    myLabel.grid(row = r , column = 0)
    r+=1


# Creating Button Widget
mybutton = Button(root,text = "Click Me!",command = buttonClick)
mybutton.grid(row = 0, column = 0, padx = 50)

root.mainloop()
