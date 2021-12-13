# Read Me for CSC3131 project
## Data Hope
The idea behind this project is to create a web app where charities can store their
data in a database so that they do not have to rely on Spreadsheets to store 
data which should be stored in a database such as their member's information.
## What is in this project
In this project there are the following web pages
1) Registration - where a user registers an account
2) Log in - the user can log into their account
3) Home - the user can navigate between the pages
4) Update Info - where the user updates their account information
5) Add Data - where the user can add new columns or add records to the database
6) Get Data - where the user can see the data from their table displayed to them
## Set Up 
To start the project in powershell you need to:
1) Make sure you are in the correct directory
2) Initialise the virtual environment by typing the following: 
   1) py -3 -m venv venv 
   2) venv\Scripts\activate
3) Now you need to initialise the FLASK app, type the following:
   1) $env:FLASK_APP = "DataHope"
   2) $env:FLASK_ENV = "development"
4) (IF FIRST TIME USING) need to initialise the database
   1) $ flask init-db
5) Now run flask
   1) flask run
6) You will then be given the port of where it is running, copy and paste 
    into your web browser and add /auth/register to take you to the registration page
7) TO get to dashboard add /dashboard
