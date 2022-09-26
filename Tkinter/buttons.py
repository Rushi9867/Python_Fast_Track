from tkinter import*

root = Tk()
def myClick():
    myLabel = Label(root,text="Look! I Clicked a Button!!")
    myLabel.pack()

myButton = Button(root,text="Click Me!",command=myClick,fg="blue",bg="red") #state=DISABLED,pady=,padx
myButton.pack()

root.mainloop()