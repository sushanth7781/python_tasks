from database import create_table,insert_user,fetch_users,update_user,delete_user
if __name__=="__main__":
    create_table()
    insert_user("alice","alice@example.com")
    insert_user("tony","tony@gmail.com")
    print("Users:",fetch_users())
    update_user(1,"alice_new@example.com")
    delete_user(2)
    print("updated users:",fetch_users())