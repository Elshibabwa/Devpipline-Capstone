import sqlite3
import bcrypt
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

def add_user():
    # while True:
    print('**** Please Add User Information ****\n\n')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    password = input('Password: ')
    date_created = input('Current Date (YYYY-MM-DD): ')
    hire_date = input('Hire Date (YYYY-MM-DD): ')
    user_type = input('Please enter the user type: ')
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query = "INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = [first_name, last_name,phone, email, hashed.decode(), date_created, hire_date, user_type]

    if input == '':
        print(f"\n{'**** ERROR. Please enter information. Press ENTER to continue ****':^120}\n") 
        pass

    cursor.execute(query, values)

    connection.commit()

def add_competency():
    print('**** Please Add Competency Information ****\n\n')
    print('Competency List:\n\nData Types\nVariables\nFunctions\nBoolean Logic\nConditionals\nLoops\nData Structures\nLists\nDictionaries\nWorking with Files\nException Handling\nQuality Assurance (QA)\nObject-Oriented Programming(OOP)\nRecursion\nDatabases\n')
    name = input('Competency Name: ')
    date_created = input('Current Date (YYYY-MM-DD): ')

    query = "INSERT INTO Competencies (comp_name, date_created) VALUES (?, ? )"
    values = [name, date_created]

    cursor.execute(query, values)

    connection.commit()

def add_assessment_to_competency():
    print('**** Please Add Assessment Information ****\n\n')
    name = input('Assesment Name: ')
    competency = input('Competency Name: ')
    date_created = input('Current Date (YYYY-MM-DD): ')

    query = "INSERT INTO Assessments (assess_name, comp_name, date_created) VALUES (?, ?, ?)"
    values = [name, competency, date_created]

    cursor.execute(query, values)

    connection.commit()

def add_assessment_result():
    print('**** Please Add Assessment Results Information ****\n\n')
    assessment = input('Assessment Taken: ')
    score = input('Score: ')
    date_taken = input('Date Taken (YYYY-MM-DD): ')
    time_taken = input('Time Taken (hh:mm): ')
    manager = input('Manager ID number: ')

    query = "INSERT INTO Competency_Assessment_Results (assess_name, score, date_taken, time_taken, manager) VALUES (?, ?, ?, ?, ?)"
    values = [assessment, score, date_taken, time_taken, manager]

    cursor.execute(query, values)
    connection.commit()

    