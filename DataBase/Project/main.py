from database import DBHelper

def main():
    db = DBHelper()
    while True:
        print("********* Welcome **********")
        print("Press 1 to Insert New User")
        print("Press 2 to Display All User")
        print("Press 3 to Delete User")
        print("Press 4 to Update User")
        print("Press 5 to Exit Program")
        print()
        try:
            choice = int(input())
            if choice == 1:
                # insert user
                uid = int(input("Enter user id: "))
                uname= input("Enter user name: ")
                uphone = input("Enter user phone: ")
                db.insert_user(uid, uname, uphone)
            elif choice == 2:
                # Display user
                db.fetch_all()
            elif choice == 3:
                uid1 = int(input("Enter user id to which you want to delete: "))
                db.delete_user(uid1)
            elif choice == 4:
                uid2 = int(input("Enter user id: "))
                uname2 = input("Enter new name: ")
                uphone2 = input("Enter new phone: ")
                db.update_user(uid2, uname2,uphone2)
            elif choice == 5:
                break
            
            else:
                print("Invalid Input ! Try Again")
        except Exception as e:
            print(e)   

if __name__ == "__main__":
    main()