Features
The tool will be a console application and will support the following features:

To Do:

Login and logout. The tool should keep track of user emails and passwords to allow 
for secure login. The passwords should be hashed so that they are not stored in the 
database in plain-text.

Two User Types and their access to features.
    A user is an individual that can only view their own competency and assessment 
    data. They should have the ability to edit their own user data such as changing 
    their name and editing their own password.
    A manager is an individual that can manage users. They should be able to:
    view all users in a list
    search for users by first name or last name
        view all user competencies by user
        view a report of all users and their competency levels for a given competency
        view a competency level report for an individual user
        view a list of assessments for a given user
        # Add
        #     add a user
        #     add a new competency
        #     add a new assessment to a competency
        #     add an assessment result for a user for an assessment 
        #     (this is like recording test results for a user)
        Edit
            edit a user's information
            edit a competency
            edit an assessment
            edit an assessment result
        Delete
            delete an assessment result

Export reports to CSV
    Competency report by competency and users
    Competency report for a single user

Import assessment results from CSV
    The ability to import assessment results from a CSV file
        The CSV file would contain columns user_id, assessment_id, score, date_taken


The entities, or objects, that we want to store in the database would be:
Users - The users that we are tracking and/or are logging into the system

Competencies - The competencies we want to track. See Competencies and 
Initial Competency List below.

Assessments - The tests or measurement tools that we use to measure competency levels. 
See Competency Assessments and Competency Scale below. Each assessment relates to a 
single competency, however, each competency may have several assessments.

Assessment Results - The results of the tests or measurements for individual users 
on specific dates. Users may take each assessment multiple times, so there will likely 
be multiple Assessment Results per user, however, each Assessment Result relates to 
a single user.


For this project, you will need to provide:
A database schema design document, like an Entity-Relationship Diagram (ERD). 
These are the same diagrams we have been creating in class that show the entities, 
their columns with their respective data types and keys and constraints 
(PRIMARY, FOREIGN, UNIQUE, NOT NULL, DEFAULT), and any relationships between tables.

A working application that meets the requirements in this document. It should be a 
working console application (terminal app).

A CSV file that can be imported into the application to add assessment results

A database file (SQLite) that contains the data from your executions of the 
application. You should have plenty of test data in here for testing your application 
as well as for grading.

Instructions on how to use your application. This doesn't have to be fancy, just a 
text or markdown document (README.md) that describes how your application should work.

A GitHub repository that you can push all of the above code and documentation to. 
This is how you will turn in the assignment.


Competencies
Competency is a skill or demonstration of having sufficient knowledge or ability in a 
particular subject. The competency data should at least be:

name - the name of the competency as shown in the list below under 
Initial Competency List
Computer Anatomy
Data Types
Variables
Functions
Boolean Logic
Conditionals
Loops
Data Structures
Lists
Dictionaries
Working with Files
Exception Handling
Quality Assurance (QA)
Object-Oriented Programming
Recursion
Databases

date_created - the date the competency was added to the application


Competency Assessment Data
The software should store the following information about an assessment:

name - the name of the assessment, like Data Structures Competency Measurement 
or Verbal Communication Interview

date created - the date the assessment was added to the database



Competency Assessment Results
When a user takes an assessment, it should be recorded as a Competency 
Assessment Result, which should record:

user - the user that took the assessment (probably a user_id in the database)

assessment - the assessment that the user took (probably an assessment_id in 
the database)

score - the resulting score (0-4)

date taken - the date and time the assessment was taken

manager - the manager, if any, that administered the test. (probably a user_id in 
the database)

Users can retake competency assessments as many times as they would like, so they 
may have multiple Assessment Results for any given assessment.


Users
A user is an individual that will be taking competency assessments. This could 
be an employee or even a manager.

The software should keep track of the following data for users:

first name

last name

phone

email - this will also be their login username

password - this should be hashed (never stored in plain text)

active - whether this user is active or not (inactive users cannot login)

date created - the date this user was created in the system

hire date - the date this user was hired

user type - Either a user or a manager. This would be used to determine the 
access the user has to the system.

You will probably also want to keep track of a user id of some sort.


Reports
There are two primary reports this application should provide:

User Competency Summary

Competency Results Summary for all Users


User Competency Summary
This is a summary of all the competency scores for a user. It should contain:

User information like name, email

List of all competencies with their corresponding scores, if the user has one.
    If the user has more than one assessment result for a given competency, use 
    the most recent as their score.
Average competency score, across all assessment results.
    This is a simple average, so, add up all the assessment results, divide by 
    the number of competencies and you get the overall average competency score
    If a user doesn't have a score for a given competency, use 0 for that competency 
    score.


Competency Results Summary
This is a results summary for all users. It is a bit like the opposite of the User 
Competency Summary. This report is for a single competency, like Data Structures, 
and will list all users with their competency scores for that competency. This should 
provide:

Competency information like name

Average competency score for this competency across all users.
    Add all competency scores from the most recent assessment results for each active 
    user and divide by the number of active users.

List of Users with the following information:
    Name
    
    Competency Score - The score from the most recent assessment result for this 
    user and this competency. Write 0, if never taken.
    
    Assessment - the most recent assessment taken, if any. blank, if none.
    
    Date Taken - the date the most recent assessment was taken, if any.


CSV Export
Your application should allow for CSV export of at least two lists. For example, 
you may want to export the User list or the Competencies list. You will produce 
a valid CSV file containing the information from the list.

Include a Header Row with field names in your CSV file.


CSV Import
Your application should provide the ability to import a CSV file for Assessment 
Results. This CSV file would contain the following columns:

user_id

assessment_id

score

date_taken

and any others you think might be helpful.

This import will read the CSV file and add records to the Assessment Results table 
in the database.