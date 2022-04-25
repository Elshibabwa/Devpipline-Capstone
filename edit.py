import sqlite3
import bcrypt
from delete import delete_assessment
from active_status import *
from details import *
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

def edit_user(selected_user_id):
    edit_value = ''
    query = ''
    
    while True:
        edit_input = input("Select the number number you would like to edit:\n[1] First Name\n[2] Last Name\n[3] Phone\n[4] Email\n[5] Password\n[6] Date Created\n[7] Hire Date\n[8] User Type\n[9] Quit\n\nEnter 'DEACTVIATE'\nEnter 'REACTIVATE'\n\n")
        if edit_input == '1':
            edit_value = input('First Name: ')
            query = 'UPDATE Users SET first_name = ? WHERE user_id = ?;'
            cursor.execute(query, (edit_value, selected_user_id))
        if edit_input == '2':
            edit_value = input('Last Name: ')
            query = 'UPDATE Users SET last_name = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))
        if edit_input == '3':
            edit_value = input('Phone: ')
            query = f'UPDATE Users SET phone = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))
        if edit_input == '4':
            edit_value = input('Email: ')
            query = f'UPDATE Users SET email = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))
        if edit_input == '5':
            edit_value = input('Password: ')
            hashed = bcrypt.hashpw(edit_value.encode('utf-8'), bcrypt.gensalt())
            query = f'UPDATE Users SET password = ? WHERE user_id = ?;'
            cursor.execute(query,(hashed.decode(),selected_user_id))
        if edit_input == '6':
            edit_value = input('Date Created: ')
            query = f'UPDATE Users SET date_created = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))    
        if edit_input == '7':
            edit_value = input('Hire Date: ')
            query = f'UPDATE Users SET hire_date = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))     
        if edit_input == '8':
            edit_value = input('User Type: ')
            query = f'UPDATE Users SET user_type = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, selected_user_id))                 
        if edit_input == '9':
            print('**** Returning to menu ****\n\n')
            break
        

        if edit_input == 'DEACTIVATE':
            deactivate_user(selected_user_id)
        if edit_input == 'REACTIVATE':
            reactiviate_user(selected_user_id)
        if edit_input == '':
            print('**** ERROR. Please select from the menu ****\n\n')  

        connection.commit()
        
        
        print('\n\n')
        user_details(selected_user_id)
        print(f'\n**** User record {selected_user_id} had been updated. Press any key to continue ****\n\n')
        break

def user_edit_user(selected_user_id):
    edit_value = ''
    query = ''
    
    while True:
        edit_input = input("Select the number number you would like to edit:\n[1] First Name\n[2] Last Name\n[3] Password\n[4] Quit\n\n")
        if edit_input == '1':
            edit_value = input('First Name: ')
            query = f'UPDATE Users SET first_name = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, selected_user_id))
        if edit_input == '2':
            edit_value = input('Last Name: ')
            query = f'UPDATE Users SET last_name = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, selected_user_id))
        if edit_input == '3':
            edit_value = input('Password: ')
            hashed = bcrypt.hashpw(edit_value.encode('utf-8'), bcrypt.gensalt())
            query = f'UPDATE Users SET password = ? WHERE user_id = ?'
            cursor.execute(query,(hashed.decode(),selected_user_id))
        elif edit_input == '4':
            print('**** Returning to menu ****\n\n')
            break
        else:
            print('**** ERROR. Please select from the menu ****\n\n')     
            
        connection.commit()
        
        print('\n\n')
        user_details(selected_user_id)
        print(f'\n**** User record {selected_user_id} had been updated. Press any key to continue ****\n\n')
        break



def edit_competency(comp_name):
    edit_value = ''
    query = ''
    while True:
        edit_input = input("Select the number number you would like to edit:\n[1] Competency Name\n[2] Date Created\n[3] Quit\n\n")
        if edit_input == '1':
            edit_value = input('Competency Name: ')
            query = f'UPDATE Competencies SET comp_name = ? WHERE comp_name= ?'
            cursor.execute(query,(edit_value, comp_name))
        if edit_input == '2':
            edit_value = input('Date Created: ')
            query = f'UPDATE Competencies SET date_created = ? WHERE comp_name = ?;'
            cursor.execute(query,(edit_value, comp_name))
        elif edit_input == '3':
            print('**** Returning to menu ****\n\n')
            break
        else:
            print('**** ERROR. Please select from the menu ****\n\n')  
            continue
        connection.commit()

        print('\n\n')
        comp_details(comp_name)
        print(f'\n**** User record {comp_name} had been updated. Press any key to continue ****\n\n')
        break

def edit_assessment(name):
    edit_value = ''
    query = ''
    while True:
        edit_input = input("\nSelect the number number you would like to edit:\n[1] Assessment Name\n [2] Competency Name\n[3] Date Created[4] Quit\n\n")
        if edit_input == '1':
            edit_value = input('Assessment Name: ')
            query = f'UPDATE Assessments SET assess_name = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, name))
        if edit_input == '2':
            edit_value = input('Competency Name: ')
            query = f'UPDATE Assessments SET comp_name = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, name))
        if edit_input == '3':
            edit_value = input('Date Created: ')
            query = f'UPDATE Assessments SET date_created = ? WHERE user_id = ?;'
            cursor.execute(query,(edit_value, name))
        elif edit_input == '4':
            print('**** Returning to menu ****\n\n')
            break
        else:
            print('**** ERROR. Please select from the menu ****\n\n')  
            continue
            

        connection.commit()

        print('\n\n')
        user_details(name)
        print(f'\n**** User record {name} had been updated. Press any key to continue ****\n\n')
        break

def edit_assessment_result(assessment):
    edit_value = ''
    query = ''
    while True:
        edit_input = input("Select the number number you would like to edit:\n[1] Assessment Name\n[2] Score\n[3] Date Taken\n[4] Time Taken\n[5] Quit\nEnter 'DELETE' to Remove Assessment Result\n\n")
        if edit_input == '1':
            edit_value = input('Assessment Name: ')
            query = f'UPDATE Competency_Assessment_Results SET asses_name = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, assessment))
        if edit_input == '2':
            edit_value = input('Score: ')
            query = f'UPDATE Competency_Assessment_Results SET score = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, assessment))
        if edit_input == '3':
            edit_value = input('Date Taken: ')
            query = f'UPDATE Competency_Assessment_Results SET date_taken = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, assessment))
        if edit_input == '4':
            edit_value = input('Time Taken: ')
            query = f'UPDATE Competency_Assessment_Results SET time_taken = ? WHERE user_id = ?'
            cursor.execute(query,(edit_value, assessment))
        if edit_input == '5':
            print('**** Returning to menu ****\n\n')
            break
       
        if edit_input == 'DELETE':
            delete_assessment(assessment)
        else:
            print('**** ERROR. Please select from the menu ****\n\n')
            continue  

        connection.commit()
        print('\n\n')
        user_details(assessment)
        print(f'\n**** User record {assessment} had been updated. Press any key to continue ****\n\n')
        break