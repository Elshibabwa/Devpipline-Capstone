import sqlite3
from ansi_lib import *
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

#  Search for user by first/last name
def search_user():
    search_term = input("\n\nEnter a name you want to search: ")

    search_term = f"%{search_term}%"

    
    print(f"\n{'******************** SEARCH USER ********************':^135}\n\n")
    row = cursor.execute("SELECT user_id, first_name, last_name, phone, email, hire_date, user_type FROM Users WHERE first_name LIKE ? OR last_name LIKE ? ",(search_term, search_term)).fetchall()
    print(f"{'ID:':<5}{'First Name: ':<20}{'Last Name:':<20}{'Phone:':<15}{'Email:':<25}{'Hire Date:':<15}{'User Type:':<20}\n{'-'*125}\n")

    for var in row:
        var = [str(x) for x in var]
        print(f"{var[0]:<5}{var[1]:<20}{var[2]:<20}{var[3]:<15}{var[4]:<25}{var[5]:<15}{var[6]:<20}")
    

