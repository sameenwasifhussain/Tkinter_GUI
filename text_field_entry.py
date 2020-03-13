from tkinter import *

# Creating the ROOT Widget (main window)
root = Tk()

# Creating an entry widget
entryField = Entry(root, width = 50, borderwidth = 5)
entryField.pack()
entryField.insert(0, "Enter Your Name: ")

# Function for Output after Button Click
def buttonClick():
    helloText = "Hello " + entryField.get()
    myLabel = Label(root, text = helloText)
    myLabel.pack()

# Creating Button Widget
myButton = Button(root, text = "Enter Your Name", command = buttonClick)
myButton.pack()

# Running the GUI continuously
root.mainloop()
