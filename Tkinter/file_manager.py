from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python Programs",title="Open file okay?",
                                          filetypes=(("text files","*.txt"),("allfiles","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
window.geometry("450x500") #resize the window
'''def resize(): 
    w = 500
    h = 500
    window.geometry(f"{w}x{h}")
    window.geometry("{width}x{height}".format(width=w,height=h))
    window.geometry("%ix%i" %(w,h))'''
button = Button(text="Open",command=openFile)#command=resize
button.pack()
window.mainloop()