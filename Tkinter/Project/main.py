from tkinter import * 
from PIL import ImageTk,Image 
from database import DBhandler

root = Tk()
root.title("This is a Database")


db = DBhandler()
def submit():
    db.insert(id.get(),f_name.get(),l_name.get(),address.get(),city.get(),state.get(),pincode.get())
    #clear the boxes
    id.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)

def query():
    record = db.fetch_all()
    
    query_label = Label(root,text=record)
    query_label.grid(row=15,column=0)
    
def delete():
    del1 = db.delete_user(ID.get())
    print(del1)

def Update():
    msg = db.update_user(update.get(),update1.get())
    print(msg)

    update.delete(0,END)
    update1.delete(0,END)

def drop():
    drb = db.drop_db()
    print(drb)

#Entries
id = Entry(root,width=30)
id.grid(row=0,column=1,padx=20,pady=(10,0))
f_name = Entry(root,width=30)
f_name.grid(row=1,column=1)
l_name = Entry(root,width=30)
l_name.grid(row=2,column=1)
address = Entry(root,width=30)
address.grid(row=3,column=1)
city = Entry(root,width=30)
city.grid(row=4,column=1)
state = Entry(root,width=30)
state.grid(row=5,column=1)
pincode = Entry(root,width=30)
pincode.grid(row=6,column=1)
ID = Entry(root,width=30)
ID.grid(row=9,column=1)
update = Entry(root,width=30)
update.grid(row=11,column=1)
update1 = Entry(root,width=30)
update1.grid(row=12,column=1)

#Labels
id_label = Label(root,text="Enter id")
id_label.grid(row=0,column=0,pady=(10,0))
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=1,column=0)
l_name_label =Label(root,text="Last Name") 
l_name_label.grid(row=2,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=3,column=0)
city_label = Label(root,text="City")
city_label.grid(row=4,column=0)
state_label = Label(root,text="State")
state_label.grid(row=5,column=0)
pincode_label = Label(root,text="Pincode")
pincode_label.grid(row=6,column=0)
ID_label = Label(root,text="Delete ID")
ID_label.grid(row=9,column=0)
update_label = Label(root,text="Enter the id You want to Update")
update_label.grid(row=11,column=0)
update1_label = Label(root,text="Enter the State Name")
update1_label.grid(row=12,column=0)

#Buttons
submit_btn = Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=10)
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=10)
delete_btn = Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=10)
update_btn = Button(root,text="Update Record",command=Update)
update_btn.grid(row=13,column=0,columnspan=2,padx=10,pady=10,ipadx=10)
drop_btn = Button(root,text="DROP Database",command=drop)
drop_btn.grid(row=14,column=0,columnspan=2,padx=10,pady=10,ipadx=10)

root.mainloop()
