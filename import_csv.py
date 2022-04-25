import sqlite3
import csv

connection = sqlite3.connect('Capstone.db')

cursor = connection.cursor()

def import_csv():
    list = []

    with open('import.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        headerrow = next(data)
        query = "INSERT INTO Competency_Assessment_Results (user_id, assess_name, score, date_taken, time_taken, manager) VALUES(?,?,?,?,?,?)"
        
        if headerrow != None:
            for row in data:
                list.append(row)
                print(list)

        cursor.executemany(query, list)

        connection.commit()


