import sqlite3

from view import view_all_competency
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

def delete_assessment():
    name = input('Please enter a Competency Name. ')
    user_id, assess_name = view_all_competency(name, True)

    query = (f'DELETE FROM Competency_Assessment_Results WHERE assess_name LIKE %?% AND user_id = ?')
    cursor.execute(query,(name,user_id))
    
    print(f'**** Assessment {assess_name} had been deleted. Press any key to continue ****')

    connection.commit()    