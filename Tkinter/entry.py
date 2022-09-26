from tkinter import*

root = Tk()
e = Entry(root,width=50,)#fg,bg
e.pack()
#e.insert(0,"Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack()

myButton = Button(root,text="Enter Your Name",command=myClick,fg="blue",bg="red") #state=DISABLED,pady=,padx
myButton.pack()

root.mainloop()