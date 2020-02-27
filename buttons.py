from tkinter import *

# Creating the ROOT Widget (main window)
root = Tk()

# Function for Button Click
def buttonClick():
    myLabel = Label(root, text = "You just clicked a button!")
    myLabel.pack()

# Creating Button Widget
myButton = Button(root, text = "Click Here!", command = buttonClick, fg = "black", bg = "green")
myButton.pack()

# Running the GUI continuously
root.mainloop()