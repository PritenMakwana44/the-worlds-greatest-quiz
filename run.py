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
    
    username = input("Enter new Username:")
    
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
            username = input("Enter new Username:")
        else:
            print("Username Accepted...")
            break


    password = input("Enter new Password: ")
    while True:
        for s in password:        
                if (s.isspace()) == True:
                    print(f"Please fill in a valid password")
                    password = input("Enter new Password: ")
                    
            
        if (len(password.strip()) == 0):
            print(f"Please fill in a valid password")
            password = input("Enter new Password: ")
                    
            
                    
        else:
            points = 0
            print(f"Creating Account for {username}...")
            update_worksheet = []                
            update_worksheet.append(username)
            update_worksheet.append(password)
            update_worksheet.append(points)
            login.append_row(update_worksheet)
            print(f"Account created Successfully!")
            logon()
            break
            
def logon():
    print(f"Please login")
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
                question_answer(username)
                break
                    
            else:
                print("Password Incorrect")
                login_register()
                    
        elif i == len(username_list)-1:
                print("Username not found")
                login_register()
                break
    
    
                

def login_register():
    inital_question = input("Do you have an account? y/n: ")
    if inital_question == "n":
        create_new_user()
        
    
    if inital_question == "y":
        logon()
    
    else:
        login_register()

        
               
def question_answer(username):
    
    qa_username = username
    qa_username_cell = login.find(qa_username)
    question_list = question_col
    question_list.remove("question")

    print("...")
    print("Ready...")
    print("Steady...")
    print("Let's Begin!!!")
   
    for count in range(10):
        question = random.choice(question_list)
        question_cell = bank.find(question)
        answer_cell = bank.cell(question_cell.row, question_cell.col + 1).value

        for i in range(len(question_list)):
            if question_list[i] == question:
                print(question)
                
                answer_input = input('Enter True or False: ').upper()
                if answer_input.upper() != 'TRUE' or 'FALSE':
                    print("Invalid Input")
                    answer_input = input('Enter True or False: ').upper()
                if answer_input.upper() == 'TRUE': 
                    if answer_cell.upper() == answer_input.upper():
                        print("correct")
                        increment = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
                        increment = increment + 10
                        login.update_cell(qa_username_cell.row, qa_username_cell.col + 2, increment)
                        break
                    elif answer_cell.upper() != answer_input.upper():
                        print("Incorrect")
                        break
                    
                if answer_input.upper() == 'FALSE': 
                    if answer_cell.upper() == answer_input.upper():
                        print("correct")
                        increment = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
                        increment = increment + 10
                        login.update_cell(qa_username_cell.row, qa_username_cell.col + 2, increment)
                        break
                    elif answer_cell.upper() != answer_input.upper():
                        print("Incorrect")
                        break
                
                        
                    
                
                    
       
    get_points = int(login.cell(qa_username_cell.row, qa_username_cell.col + 2).value)
    print(f"You now have {get_points} points")
    

    

def main():
    login_register()
   

   






main()

