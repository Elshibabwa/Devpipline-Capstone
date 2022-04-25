import email
import sqlite3
import bcrypt
from pkg_resources import cleanup_resources
from login import login, is_manager
from add import *
from view import *
from details import *
from edit import *
from search import *
from active_status import *
from delete import *
from ansi_lib import *
from import_csv import *
from export_csv import *

connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

print(f"\n{'******************** WELCOME ********************':^120}\n")

while True:

    main_menu = input('\nPlease choose from the following options\n\n[1] Login\n[2] Create Account\n[3] Quit\n\n>>>')
    if main_menu == '1':
        user_id = login()
        user_type = is_manager()
        print(user_type)
        while user_type == '1':
            print(f"\n{'******************** ADMIN MENU ********************':^120}\n")
            admin_menu = input('\nPlease select from the following options:\n[1] Users\n[2] Competencies\n[3] Assessments\n[4] Quit\n\n>>>')
            while admin_menu == '1':
                u_menu = input('\n\nWhat would you like to do:\n[1] View a User\n[2] Search User\n[3] Edit User\n[4] Quit\n\n>>>')
                if u_menu == '1':
                    user_id = view_users()
                    user_details(user_id) 
                if u_menu == '2':
                    search_user()

                if u_menu == '3':
                    search_user()
                    selected_user_id = view_users()
                    edit_user(selected_user_id)
                    
                if u_menu == '4':
                    print(f"\n{'******************** Returning to Menu ********************':^120}\n") 
                    break
                if u_menu == '':
                    input(f"\n{'**** ERROR. Please select from the menu. Press ENTER to continue ****':^120}\n")
                    continue
                
            while admin_menu == '2':
                c_menu = input('\nWhat would you like to do:\n[1] View All Users For A Competency\n[2] View Individual User Competency\n[3] Edit Competency\n[4] Edit Competency Assessment Result\n[5] Add Competency\n[6] Export Reports\n[7] Import Competency Report\n[8] Quit\n\n>>>')
                if c_menu == '1':
                    name = input('\nPlease enter a Competency name:  ')
                    view_all_competency(name)
                    
                if c_menu == '2':
                    user_id = input('\nPlease enter a user id: ')
                    view_individual_competency(user_id)
                   
                if c_menu == '3':
                    user_id,comp_name = view_all_competency(True)
                    comp_details(comp_name)
                    edit_competency(comp_name)
                if c_menu == '4':
                    assessment = input('\nPlease enter an assessment name:  ')
                    edit_assessment_result(assessment)
                if c_menu == '5':
                    add_competency() 

                if c_menu == '6':
                    print("Exporting all Users and Competencies to CSV.")
                    export_csv_comp()
                    export_csv_user()     
                    
                    print(f"\n{'******************** Competency has been added ********************':^120}\n")
                while c_menu == '2':
                    export_menu = input('\nWhich report would you like to export:\n[1] Assessment Results by User\n[2] Assessment Results by Competency\n[3] Quit\n\n>>>')
                    if export_menu == '1':
                        user_id = view_users()
                        export_csv_user(user_id)
                    if export_menu == '2':
                        name = input('\nPlease enter a Competency:  ')
                        export_csv_comp(name)
                    if export_menu == '3':
                        print(f"\n{'******************** Returning to Menu ********************':^120}\n")
                        break
                    if c_menu == '':
                        print(f"\n{'**** ERROR. Please select from the menu. Press ENTER to continue ****':^120}\n")
                        continue
                if c_menu == '7':
                    import_csv()
                if c_menu == '8':
                    print(f"\n{'******************** Returning to Menu ********************':^120}\n")          
                    break
                if c_menu == '':
                    print(f"\n{'**** ERROR. Please select from the menu. Press ENTER to continue ****':^120}\n")
                    continue

                
            while admin_menu == '3':
                print(f"\n{'******************** ADMIN MENU ********************':^120}\n")
                a_menu = input('\nWhat would you like to do:\n[1] View Assessments\n[2] Edit Assessment\n[3] Edit Assessment Result\n[4] Add Assessment to Competency\n[5] Add Assessment Result\n[6] Quit\n\n>>>')
                if a_menu == '1':
                    user_id = view_users()
                    view_assessments_user(user_id)
                    user_details(user_id)
                if a_menu == '2':
                    user_id = view_users()
                    edit_assessment(user_id) 
                if a_menu == '3':
                    user_id = view_users()
                    edit_assessment_result(user_id) 
                if a_menu == '4':
                    add_assessment_to_competency()            
                    user_details()
                    print(f"\n{'******************** Assessment has been added ********************':^120}\n")
                if a_menu == '5':
                    add_assessment_result()            
                    user_details()
                    print(f"\n{'******************** Assessment Result has been added ********************':^120}\n")
                if a_menu == '6':
                    print(f"\n{'******************** Returning to Menu ********************':^120}\n")          
                    break
                if a_menu == '':
                    print(f"\n{'**** ERROR. Please select from the menu. Press ENTER to continue ****':^120}\n")
                    continue
            
        while user_type == '0':
            print(f"\n{'******************** USER MENU ********************':^120}\n")

            user_menu = input('\nPlease select one of the following:\n[1] View User Information\n[2] Edit User Information\n[3] View Competency Assessment Results\n[4] Quit\n\n>>>')
            if user_menu == '1':
                user_details(user_id) 
            if user_menu == '2':
                user_details(user_id)
                print('\n\n')
                user_edit_user(user_id)
                user_details(user_id)
            
            if user_menu == '3':
                view_individual_competency(user_id)

            if user_menu == '4':
                print(f"\n{'******************** Returning to Menu ********************':^120}\n") 
                break
            if user_menu == '':
                print(f"\n{'**** ERROR. Please select from the menu. Press ENTER to continue ****':^120}\n")
                continue

    if main_menu == '2':
        add_user()
        print(f"\n{'******************** Returning to Menu ********************':^120}\n") 
        continue
    if main_menu == '3':
        print(f"\n{'******************** GOODBYE ********************':^120}\n")
        break 