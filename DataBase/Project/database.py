import mysql.connector as connect 

class DBHelper:
    def __init__(self):
        self.mydb = connect.connect(host="localhost",user="root",passwd="R@ud!n$0903",database="raudin",use_pure=True)
        query = "Create Table if not exists user(userId INT(5) primary key , userName varchar(200),phone varchar(12))"
        cur = self.mydb.cursor()
        cur.execute(query)
        print("Created")

# Insert
    def insert_user(self,userid,username,phone):
        query = "Insert Into User(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        #print(query)
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print("User saved to DB")

# Fetch all
    def fetch_all(self):
        query = "select *from user"
        cur = self.mydb.cursor()
        cur.execute(query)
        for i in cur:
            print("User Id :",i[0])
            print("User Name :",i[1])
            print("User Phone :",i[2])
            print()

# Delete
    def delete_user(self,userId):
        query = "Delete from user where userId = {}".format(userId)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print("Deleted")

# Update
    def update_user(self,userId,newName,newPhone):
        query = "Update user set userName ='{}',phone='{}' WHERE userId= {}".format(newName,newPhone,userId)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print("Updated")

