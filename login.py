import sqlite3
import bcrypt 
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

email_addr = ''

def login(): 
    global email_addr
    print(f"\n{'******************** LOGIN MENU ********************':^120}\n")
    
    while True:
        email_addr = input('email: ')
        password = input('Password: ')

        query_result = cursor.execute('SELECT password,user_id FROM Users WHERE email = ? AND active = 1 ',(email_addr,)).fetchone()
       
        if not query_result:
            print('**** User Does not Exist. ****')
            continue


        hashed_pass = query_result[0]
        user_id = query_result[1]

        if bcrypt.checkpw(password.encode(), hashed_pass.encode()):
            print("**** You're In ****")
            return(user_id)

        else:
            print('**** Incorrect. Try again ****')
            continue

def is_manager():
    global email_addr
    user_type = ''

    user = cursor.execute("SELECT user_type FROM Users WHERE email=?",(email_addr,)).fetchone()
    
    if user and user[0].lower() == 'manager':
        user_type = '1'
    if user and user[0].lower() == 'user':
        user_type = '0'

    return user_type        
        

    
  
