import sqlite3
import bcrypt
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()




def edit_user(selected_user_id):
    edit_value = ''
    query = ''
    
    while True:
        edit_input = input("Select the number number you would like to edit:\n[1] First Name\n[2] Last Name\n[3] Phone\n[4] Email\n[5] Password\n[6] Date Created\n[7] Hire Date\n[8] User Type\n[9] Enter 'DEACTVIATE'\n[10] Enter 'REACTIVATE'\n[11] Quit\n\n")
        
        if edit_input == '5':
            edit_value = input('Password: ')
            hashed = bcrypt.hashpw(edit_value.encode('utf-8'), bcrypt.gensalt())
            query = f'UPDATE Users SET password = ? WHERE user_id = {selected_user_id};'
            cursor.execute(query,[hashed])
        
        
        
edit_user(9)



