from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("This is a File Dialog")
def open():
    global my_file
    root.filename = filedialog.askopenfilename(initialdir="D:\Python Programs\Python_Fast_Track\Tkinter",title="select a File",filetypes=(("text files","*.txt"),("allfiles","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_file = ImageTk.PhotoImage(Image.open(root.filename))
    my_file_label = Label(image=my_file).pack()

my_btn = Button(root,text="Open File",command=open).pack()

root.mainloop()
