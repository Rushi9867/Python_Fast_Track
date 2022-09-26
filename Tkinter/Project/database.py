import mysql.connector as connect 

class DBhandler:
    def __init__(self):
        self.mydb = connect.connect(host="localhost",user="root",passwd="R@ud!n$0903",use_pure=True)

# Insert
    def insert(self,id,f_name,l_name,address,city,state,pincode):
        cur = self.mydb.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS tkdata")
        query = "Create Table if not exists tkdata.tk_data(Id INT(5) primary key,First_name varchar(20),Last_name varchar(20),Address varchar(20),City varchar(20),State varchar(20),Pincode INT(20))"
        cur.execute(query)
        query1 = "Insert Into tkdata.tk_data(Id,First_name,Last_name,Address,City,State,Pincode) values({},'{}','{}','{}','{}','{}',{})".format(id,f_name,l_name,address,city,state,pincode)
        cur.execute(query1)
        self.mydb.commit()

# Fetch all
    def fetch_all(self):
        cur = self.mydb.cursor()
        cur.execute("SELECT *from tkdata.tk_data")
        records = cur.fetchall()
        record = ' '
        for i in records:
            record += str(i) +"\n"
        
        return record 


# Delete
    def delete_user(self,Id):
        query = "Delete from tkdata.tk_data where Id = {}".format(Id)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        return "Deleted..."

# Update
    def update_user(self,id,state):
        query = "UPDATE tkdata.tk_data SET State ='{}' WHERE Id= {}".format(state,id)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        return "Updated..."

# Drop Database
    def drop_db(self):
        cur = self.mydb.cursor()
        cur.execute("DROP DATABASE tkdata")
        self.mydb.commit()
        self.mydb.close()
        return "DATABASE DELETED...."

