from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox

root = Tk()
root.title("This is a Message Box Program")

#showinfo, showwarning, showerror, askquestion, askokcancel,askyesno 

def popup():
    response = messagebox.askyesno("This is my PopUp!","Hello World!")
    if response == 1:
        Label(root,text="You clicked Yes").pack()
    else:
        Label(root,text="You Clicked No").pack()

Button(root,text="PopUp",command=popup).pack()

root.mainloop()
