"""
Import's for usuage of gspread, random and sleep functions.
"""

import gspread
from google.oauth2.service_account import Credentials
import random
from time import sleep

"""
Scope to connect to Google services
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Variables to access Google sheets
"""

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_worlds_greatest_quiz')

"""
Variables to access worksheets and columns
"""
bank = SHEET.worksheet('bank')
login = SHEET.worksheet('login')
username_col = login.col_values(1)
password_col = login.col_values(2)
points_col = login.col_values(3)
question_col = bank.col_values(1)
answer_col = bank.col_values(2)

"""
start program function welcomes users and gives instructions via print statements
Sleep function delays the printing
"""

def start_program():
    print("Welcome To The Worlds Greatest Quiz")
    sleep(1)
    print("Instructions")
    sleep(1)
    print("...")
    sleep(1)
    print("First Login or Regiester")
    sleep(1)
    print("...")
    sleep(1)
    print("To play the game type True or False on each question")
    sleep(1)
    print("...")
    sleep(1)
    print("Each time you play there will be new questions!")
    sleep(1)
    print("...")
    sleep(1)
    print("No cheating ;)")
    sleep(1)
    print("...")
    print(" ")

"""
Create new new user function. 
Variables - get list from login worksheet for columns for username, password and points
Input then specified for user to create username.
"""

def create_new_user():
    username_list = login.col_values(1)
    password_list = login.col_values(2)
    points_list = login.col_values(3)
    username = input("Enter New Username:")

    """
    For username checks. If there are any invalidity of the username it raises errors i.e there is any spaces in the username - print statements indicate errors.
    if statement then used to keep prompting for a valid username until criteria is met. i.e if username doesn't exist in system already.
    """

    while True:
        try:
            while len(username.strip()) == 0:
                raise ValueError
            for s in username:
                if(s.isspace()) == True:
                    raise ValueError

        except ValueError:
            print(f"There must be no spaces in your username.")
            print(f"Please try again.")
            create_new_user()
        if username in username_list:
            print(f"'{username}' already exists")
            username = input("Enter New Username:")
        else:
            print("Username Accepted...")
            break

    """
    Once username is accepted a passoword input comes up.
    Again loops and if statements are used to check if password is valid.
    If invalid password box keeps prompting.

    
    If username and passwords are accepted then worksheet is updated and 0 points are assigned to user.
    Ends with a print statement indicating success and then prompts for user to login via the logon function.

    """

    password = input("Enter New Password: ")
    while True:
        for s in password:        
                if (s.isspace()) == True:
                    print(f"Please fill in a valid password")
                    password = input("Enter New Password: ")
                    
            
        if(len(password.strip()) == 0):
            print(f"Please fill in a valid password")
            password = input("Enter New Password: ")
        
        
        else:
            points = 0
            print(f"Creating Account For {username}...")
            update_worksheet = []                
            update_worksheet.append(username)
            update_worksheet.append(password)
            update_worksheet.append(points)
            login.append_row(update_worksheet)
            print(f"Account Created Successfully!")
            logon()
            break   


"""
Function for logon
Prints instruction to login then prompts for input.
Variables are local to grab columns from login sheet.
"""
def logon():
    print(f"Please Login")
    print("...")

    username = input('Username: ')
    points = 0
    username_list = login.col_values(1)
    password_list = login.col_values(2)
    points_list = login.col_values(3)
    """
    Loops through username list according to length of list
    if there is a username match then it asks you for password.
    if password is correct then it prints the amount of points user has.
    if password is incorrect then it prompts to try again or if username doesn't exist then again it prompts

    note question_answer(username) which links to function and allows use of username
    """
    for i in range(len(username_list)):
        if username_list[i] == username:
            password = input('Password: ')
            if password_list[i] == password:
                print('Success')
                points = points_list[i]
                print(f"Current points scored by {username} is: {points} Points")
                question_answer(username)
                play_again(username)
                break
                    
            else:
                print("Password Incorrect")
                login_register()
                    
        elif i == len(username_list)-1:
                print("Username Not Found!")
                login_register()
                break
    
    
"""
function which asks if user has an account or not. 
It then allows user to interact in order to go to the correct function accordingly. 
If you have an account and answer y - then you go to logon function
if you don't and answer n - it goes to create_new_user function
"""

def login_register():
    inital_question = input("Do You Have An Account? y/n: ")
    if inital_question == "n":
        create_new_user()
        
    
    if inital_question == "y":
        logon()
    
    else:
        login_register()

        
"""
Function for question and answer with a username paramenter
username variable declared as is cell for username
answer and question lists delcared with removal of headings

"""
               
def question_answer(username):
    
    qa_username = username
    qa_username_cell = login.find(qa_username)
    answer_list = answer_col
    if "answer" in answer_list: answer_list.remove("answer")
    question_list = question_col
    if "question" in question_list: question_list.remove("question")


    print("...")
    print("Ready...")
    print("Steady...")
    print("Let's Begin!!!")
    
    """
    random number gen into list with 10 random numbers accoring to length of list of questions.
    usage of loop and iteration to generate list of numbers.
    new question list declared.

    Then question is asked one at a time while using the random num list as an index. The num list will never be above the number of questions in a list.
    After each question true or false is asked. the case is transformed into upper so it can match spreadsheet true or false checks.
    statements are used to reject any other answers other then true or false in higher or lower case.
    After each question correct or incorrect is printed and 10 points are added to the score of user if correct. 

    10 questions are presented via the loop. 
    At the end of the quiz the amount of points your on now in total is printed.
    """
    question_list_length = len(question_list)
    random_number_gen = []
    random_number_gen = random.sample(range(question_list_length), 10)
    new_question_list = []

    for index, value in enumerate(question_list):
        for num in random_number_gen:
            if num == index:
                new_question_list.append(value)
    
    new_question_list_length = len(new_question_list)
    count = 0
    while count < new_question_list_length:
        question_cell = bank.find(new_question_list[count])
        answer_cell = bank.cell(question_cell.row, question_cell.col + 1).value
        print(f" ")
        print(new_question_list[count])
        count +=1
        answer_input = input('Enter True or False: ').upper()
        print(f" ")
        print(f"Result:")
        while True:
            if answer_input.upper() == 'TRUE': 
                if answer_cell.upper() == answer_input.upper():
                    print("Correct! - 10 points :)")
                    increment = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
                    increment = increment + 10
                    login.update_cell(qa_username_cell.row, qa_username_cell.col + 2, increment)
                    break
                    
                elif answer_cell.upper() != answer_input.upper():
                    print("Incorrect - 0 points :(")
                    break
                
            elif answer_input.upper() == 'FALSE': 
                if answer_cell.upper() == answer_input.upper():
                    print("Correct! - 10 points :)")
                    increment = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
                    increment = increment + 10
                    login.update_cell(qa_username_cell.row, qa_username_cell.col + 2, increment)
                    break
                    
                elif answer_cell.upper() != answer_input.upper():
                    print("Incorrect - 0 points :(")
                    break

            else:
                print("Invalid Input")
                answer_input = input('Enter True or False: ').upper()

        print(f" ")
    get_points = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
    print(f"You now have {get_points} points")
    play_again(username)


"""
Scoreboard function finds the highest score in points list and tells the user what the highest amount of points are to beat!

"""
    

def scoreboard():
    points_list = points_col
    points_list.remove("points")
    points_list = [int(i) for i in points_list]
    points_list.sort()
    print(f"All time highest Score: {points_list[-1]} Points")


"""
Main function activates all functions needed i.e start program, login register and scoreboard.
Main function is then run so all functions needed within run.
"""

"""
function for play again function. 

At the end of the game if they would like to play again then the option is there. 
username parameter is used and linked into logon function - this pushes the username without need for input

"""
def play_again(username):
    p_a_username = username
    print(p_a_username)
    question_play_again = input("Would you like to play again? y/n: ")

    if question_play_again == "y":
        question_answer(p_a_username)

    elif question_play_again == "n":
        print("Goodbye!") 
    
    else:
        print("Invalid Input")
        play_again(p_a_username)






def main():
    start_program()
    login_register()
    scoreboard()

main()

