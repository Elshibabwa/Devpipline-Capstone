import sqlite3
from ansi_lib import *
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

def user_details(user_id = None):

    while not user_id:
        clear()
        user_id = input('Enter an ID (or enter "x" to cancel): ')
        
        if user_id.lower() == 'x':
            return None
    
    user_row = cursor.execute('SELECT user_id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type FROM Users WHERE user_id = ?',(user_id,)).fetchone()
    print(f'ID:            {user_row[0]}')
    print(f'First Name:    {user_row[1]}')
    print(f'Last Name:     {user_row[2]}')
    print(f'Phone:         {user_row[3]}')
    print(f'Email:         {user_row[4]}')
    print(f'Password:      {user_row[5]}')
    print(f'Active:        {user_row[6]}')
    print(f'Date Created:  {user_row[7]}')
    print(f'Hire Date:     {user_row[8]}')
    print(f'User Type:     {user_row[9]}')
    
    
        

def comp_details(comp_name):

    if comp_name == '':
        comp_name = input('Enter Name: ')
        clear()
    if not comp_name:
        return None
    else:
        user_row = cursor.execute('SELECT comp_name, date_created FROM Competencies WHERE comp_name = ?',(comp_name,)).fetchone()
    
        print(f'Competency Name:    {user_row[0]}')
        print(f'Date Created:       {user_row[1]}')
        

def assess_details(assess_name = ''):

    if assess_name == '':
        assess_name = input('Enter Name: ')
        clear()
    if not assess_name:
        return None
    else:
        user_row = cursor.execute('SELECT assess_name, comp_name, date_created FROM Assessments WHERE assess_name = ?',(assess_name,)).fetchone()
        
        print(f'Assessment Name:  {user_row[1]}')
        print(f'Competency Name:  {user_row[2]}')
        print(f'Date Created:     {user_row[3]}')

def results_details(user_id = ''):

    if user_id == '':
        user_id = input('Enter an ID ')
        clear()
    if not user_id:
        return None
    else:
        user_row = cursor.execute('SELECT * FROM Users WHERE user_id = ?',(user_id,)).fetchone()
        print(f'ID:               {user_row[0]}')
        print(f'Assessment Name:  {user_row[1]}')
        print(f'Score:            {user_row[2]}')
        print(f'Date Taken:       {user_row[3]}')
        print(f'Time Taken:       {user_row[4]}')
        print(f'Manager:          {user_row[5]}')
       
    