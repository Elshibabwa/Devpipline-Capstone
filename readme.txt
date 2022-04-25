CAPSTONE PROJECT OVERVIEW

Login and logout:

The program will keep track of user emails and passwords to allow for secure login. The passwords are be hashed so that they are not stored in the database in plain-text.

The program has two User Types and their access to features.

    [1] USER - is an individual that can only view their own competency and assessment data, and edit their own user data.

    Here is a list of user usernames:

    elle@gmail.com 
    amee@gmail.com 
    tanya@gmail.com

    The password for all user logins above: 1234


    [2] MANAGER - is an individual that can manage users.
    
    Here is a list of user usernames:

    bcrave@devpipline.com
    sarah@devpipline.com
    bennyboy@devpipline.com

    The password for all user logins above: one2three
    
    Managers are able to:

        * view all users in a list
        * search for users by first name or last name
        * view a report of all users and their competency levels for a given competency
        * view a competency level report for an individual user
        *  view a list of assessments for a given use
        * add a user
        * add a new competency
        * add a new assessment to a competency
        * add an assessment result for a user for an assessment (this is like recording test results for a user)
        * edit a user's information
        * edit a competency
        * edit an assessment
        * edit an assessment result
        * delete an assessment result
        * Export reports to CSV as:
            - Competency report by competency and users
            - Competency report for a single user
        * Import assessment results from CSV
        
