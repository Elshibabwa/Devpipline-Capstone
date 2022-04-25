import sqlite3
import csv

connection = sqlite3.connect('Capstone.db')

cursor = connection.cursor()

def export_csv_user():
    csv_row = cursor.execute ('SELECT * FROM Users').fetchall()
    
    with open('export_users.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'First Name', 'Last Name', 'Phone', 'Email', 'Password', 'Active', 'Date Created', 'Hire Date', 'User Type'])
        writer.writerows(csv_row)



def export_csv_comp():
    csv_row = cursor.execute ('SELECT * FROM Competency_Assessment_Results').fetchall()
    
    with open('export_competencies.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'Assessment', 'Score', 'Date Taken', 'Time Taken', 'Manager'])
        writer.writerows(csv_row)