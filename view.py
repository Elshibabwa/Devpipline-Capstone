import sqlite3
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()
#1 view all users in a list
def view_users():
    print(f"\n{'******************** USERS ********************':^140}\n\n")
    row = cursor.execute('SELECT user_id, first_name, last_name, phone, email, active, hire_date, user_type FROM Users').fetchall()
    print(f"{'ID:':<5}{'First Name: ':<20}{'Last Name:':<20}{'Phone:':<15}{'Email:':<25}{'Active:':<5}{'Hire Date:':<15}{'User Type:':<20}\n{'-'*125}\n")

    for var in row:
        var = [str(x) for x in var]
        print(f"{var[0]:<5}{var[1]:<20}{var[2]:<15}{var[3]:<20}{var[4]:<25}{var[5]:<5}{var[6]:<15}{var[7]:<20}")

    sel_user_id = input("Please type in the User ID you'd like to select: ")
    return sel_user_id

#2 view a report of all users and their competency levels for a given competency
def view_all_competency(choose = False):
    print(f"\n{'******************** ALL USERS FOR COMPETENCY ********************':^65}\n\n")
    row = cursor.execute('SELECT U.user_id, U.first_name, U.last_name, A.comp_name FROM Users U JOIN Competency_Assessment_Results CAR ON U.user_id = CAR.user_id JOIN Assessments A ON CAR.assess_name = A.assess_name').fetchall()
    print(f"{'Choice':<8}{'ID:':<5}{'First Name: ':<20}{'Last Name:':<20}{'Competency Name:':<20}\n{'-'*65}\n")

    counter = 1
    user_id_row = []
    assess_name_row = []

    for var in row:
        var = [str(x) for x in var]
        print(f"{counter:<8}{var[0]:<5}{var[1]:<20}{var[2]:<20}{var[3]:<20}")
        user_id_row.append(var[0])
        assess_name_row.append(var[3])
        counter += 1

    if choose:
        choice = int(input('Which item are you interested in? '))
        user_id = user_id_row[choice-1]
        assess_name = assess_name_row[choice-1]

        return user_id,assess_name
#3 view a competency level report for an individual user
def view_individual_competency(user_id):
    print(f"\n{'******************** COMPETENCY BY USER ********************':^120}\n\n")
    row = cursor.execute('SELECT U.user_id, U.first_name, U.last_name, CAR.assess_name, A.comp_name, CAR.score, CAR.date_taken FROM Users U JOIN Competency_Assessment_Results CAR ON U.user_id = CAR.user_id JOIN Assessments A ON CAR.assess_name = A.assess_name WHERE U.user_id LIKE ?', (user_id,)).fetchall()
    print(f"{'ID:':<5}{'First Name: ':<20}{'Last Name:':<20}{'Assessment Name:':<20}{'Competency Name:':<20}{'Score:':<5}{'Date Taken:':<20}\n{'-'*120}\n")

    for var in row:
        var = [str(x) for x in var]
        print(f"{var[0]:<5}{var[1]:<20}{var[2]:<20}{var[3]:<20}{var[4]:<20}{var[5]:<5}{var[6]:<20}")
    
    print(f"\n{'******************** SCORING ********************':^120}\n\n{'Competencies are measured and tracked on a scale from 0-4:':^120}\n\n{'0 - No competency - Needs Training and Direction':^120}\n{'1 - Basic Competency - Needs Ongoing Support':^120}\n{'2 - Intermediate Competency - Needs Occasional Support':^120}\n{'3 - Advanced Competency - Completes Task Independently':^120}\n{'4 - Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations':^120}\n\n")

#4 view a list of assessments for a given user
def view_assessments_user(assess_name):
    assess_name = f'%{assess_name}%'
    print(f"\n{'******************** ASSESSMENTS BY USER ********************':^65}\n\n")
    row = cursor.execute('SELECT U.user_id, U.first_name, U.last_name, CAR.assess_name FROM Users U JOIN Competency_Assessment_Results CAR ON U.user_id = CAR.user_id WHERE CAR.assess_name LIKE ?',(assess_name,)).fetchall()
    print(f"{'ID:':<5}{'First Name: ':<20}{'Last Name:':<20}{'Assessment Name:':<20}\n{'-'*65}\n")

    for var in row:
        var = [str(x) for x in var]
        print(f"{var[0]:<5}{var[1]:<20}{var[2]:<20}{var[3]:<20}")


 