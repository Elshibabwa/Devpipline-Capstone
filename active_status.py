import sqlite3
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()


def deactivate_user(user_id):
    query = (f'UPDATE Users SET active = 0 WHERE user_id ={user_id}')
    cursor.execute(query)

   

    connection.commit()

def reactiviate_user(user_id):
    query = (f'UPDATE Users SET active = 1 WHERE user_id ={user_id}')
    cursor.execute(query)

  

    connection.commit()