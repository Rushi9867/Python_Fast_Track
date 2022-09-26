from tkinter import *

root = Tk()

e= Entry(root, width=50,bg="lightblue",borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    Label1 = Label(root, text= hello).pack()

button = Button(root, text="Submit", command=myClick,fg="blue",bg="lightblue").pack()
root.mainloop()