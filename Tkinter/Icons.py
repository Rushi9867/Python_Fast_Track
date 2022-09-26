from tkinter import * 
from PIL import ImageTk,Image

root = Tk()
root.title("Learn to code")
root.iconbitmap("R.png")
my_img = ImageTk.PhotoImage(Image.open("R.png"))
my_Label = Label(image=my_img)
my_Label.pack()

button_q = Button(root,text="Exit Program", command=root.quit).pack()

root.mainloop()
