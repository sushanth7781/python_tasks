import mysql.connector
DB_CONFIG={
    "host":"localhost",
    "user":"root",
    "password":"Kartheek@07",
    "database":"pythoninteg"
}
def connect_db():
    try:
        conn=mysql.connector.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("error connecting to mysql",e)
        return None
def create_table():
    conn=connect_db()
    if conn:
        cur=conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("table created succesfully")

def insert_user(name, email):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            # Delete existing user with the same email
            cur.execute("DELETE FROM users WHERE email = %s", (email,))
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cur.execute(sql, (name, email))
            conn.commit()
            print(f"User '{name}' inserted successfully.")
        except mysql.connector.errors.IntegrityError as e:
            print(f"Error: {e}. Email '{email}' already exists.")
        finally:
            cur.close()
            conn.close()

def fetch_users():
    conn=connect_db()
    if conn:
        cur=conn.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        cur.close()
        conn.close()
        return users
    
def update_user(user_id,new_email):
    conn=connect_db()
    if conn:
        cur=conn.cursor()
        sql="UPDATE users SET email = %s WHERE id = %s"
        cur.execute(sql,(new_email,user_id))
        conn.commit()
        print(f"user{user_id}updates successfully")
        cur.close()
        conn.close()

def delete_user(user_id):
    conn=connect_db()
    if conn:
        cur=conn.cursor()
        sql= "DELETE FROM users WHERE id = %s"
        cur.execute(sql,(user_id,))
        conn.commit()
        print(f"user{user_id}deleted successfully")
        cur.close()
        conn.close()
