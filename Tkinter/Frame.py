from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("This is Frame Program")
frame = LabelFrame(root,text="This is my Frame...",padx=5,pady=5)
frame.pack(padx=10,pady=10)

b = Button(frame,text="Don't Click Here!").grid(row=0,column=0)
b1 = Button(frame,text="....or here!").grid(row=1,column=1)

root.mainloop()
