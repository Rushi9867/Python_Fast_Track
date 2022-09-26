from tkinter import *
#import tkinter as tk 
#from tkinter import Tk, ttk

root = Tk()
root.title("First_Program")
#creating a Label widget
myLabel1 = Label(root, text= "Hello World!")
myLabel2 = Label(root, text="My Name is Rushikesh")
myLabel3 = Label(root, text ="My name is also Raudin")
# Showing it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)
myLabel3.grid(row=2,column=2)
root.mainloop()
