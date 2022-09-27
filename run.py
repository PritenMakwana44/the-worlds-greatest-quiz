import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_worlds_greatest_quiz')

bank = SHEET.worksheet('bank')
login = SHEET.worksheet('login')
username_col = login.col_values(1)
password_col = login.col_values(2)
points_col = login.col_values(3)
question_col = bank.col_values(1)
answer_col = bank.col_values(2)

print("Welcome to the worlds greatest quiz")
print("Instructions\n First login or register\n To play the game type true or false on each question\n The highest score is 100 points\n Each time you play there will be new questions!\n No cheating ;)")

def create_new_user():
    username_list = login.col_values(1)
    password_list = login.col_values(2)
    points_list = login.col_values(3)
    while True:
        username = input("Enter new Username: ")
        while username in username_list:
            print(f"'{username}' already exists")
            break
            username = input("Enter new Username: ")
        else:   
            password = input("Enter new Password: ")
            points = 0
            print(f"Creating Account for {username}...")
            update_worksheet = []                
            update_worksheet.append(username)
            update_worksheet.append(password)
            update_worksheet.append(points)
            login.append_row(update_worksheet)
            print(f"Account created Successfully!")
            break
      

def logon():

    username = input('username: ')
    points = 0
    username_list = login.col_values(1)
    password_list = login.col_values(2)
    points_list = login.col_values(3)
    for i in range(len(username_list)):
        if username_list[i] == username:
            password = input('Password: ')
            if password_list[i] == password:
                print('Success')
                points = points_list[i]
                print(f"You last scored: {points} points")
                break
                    
            else:
                print("Password Incorrect")
                    
        elif i == len(username_list)-1:
                print("Username not found")
                break

    question_answer()
    return username_list
    
                

def login_register():
    inital_question = input("Do you have an account? y/n: ")
    if inital_question == "n":
        create_new_user()
        
    
    if inital_question == "y":
        print(f"Please login")
        logon()
    
    else:
        login_register()

        
        
               
def question_answer(function):
    for count in range(10):
        question = random.choice(question_col)
        
        if question == "question":
            question_answer()
        
        else:
            print(question)

    
        answer_input = input('Enter True or False: ')
        for i in range(len(question_col)):
            if question_col[i] == question:
                
                if answer_col[i] == answer_input.upper():
                    print("correct")
                    break
                else:
                    print("Incorrect")
                    break
        
       







    


def main():
    login_register()
    print("...")
    print("Ready...")
    print("Steady...")
    print("Let's Begin!!!")
    

    question_answer(username_list)
   






main()

