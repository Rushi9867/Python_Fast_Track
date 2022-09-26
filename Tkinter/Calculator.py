from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=45,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=15)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_addition():
    first_num = e.get()
    global f_num 
    global math 
    math = "add" 
    f_num = int(first_num)
    e.delete(0,END)

def button_subtraction():
    first_num = e.get()
    global f_num 
    global math 
    math = "sub"
    f_num = int(first_num)
    e.delete(0,END)


def button_multiplication():
    first_num = e.get()
    global f_num 
    global math 
    math = "mul"
    f_num = int(first_num)
    e.delete(0,END)


def button_division():
    first_num = e.get()
    global f_num 
    global math
    math = "div" 
    f_num = int(first_num)
    e.delete(0,END)


def button_equal():
    second_num = e.get()
    e.delete(0,END)

    if math == "add":
        e.insert(0,f_num + int(second_num))
    
    if math == "sub":
        e.insert(0,f_num - int(second_num))
    
    if math == "mul":
        e.insert(0,f_num * int(second_num))
    
    if math == "div":
        e.insert(0,f_num / int(second_num))
    

button1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(root,text="+",padx=40,pady=20,command=button_addition)
button_eql = Button(root,text="=",padx=40,pady=20,command=button_equal)
button_clear = Button(root,text="C",padx=40,pady=20,command=button_clear)
button_sub = Button(root,text="-",padx=40,pady=20,command=button_subtraction)
button_mul = Button(root,text="*",padx=40,pady=20,command=button_multiplication)
button_div = Button(root,text="/",padx=40,pady=20,command=button_division)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=1,column=3)


button_eql.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_div.grid(row=4,column=2)
button_clear.grid(row=4,column=3)


root.mainloop()