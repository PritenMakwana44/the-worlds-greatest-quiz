import gspread
from google.oauth2.service_account import Credentials
import random
from time import sleep


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
    print("...")
    sleep(1)
    print("No cheating ;)")
    sleep(1)
    print("...")
    print(" ")



def create_new_user():
    username_list = login.col_values(1)
    password_list = login.col_values(2)
    points_list = login.col_values(3)
    
    username = input("Enter New Username:")
    
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


    password = input("Enter New Password: ")
    while True:
        for s in password:        
                if (s.isspace()) == True:
                    print(f"Please fill in a valid password")
                    password = input("Enter New Password: ")
                    
            
        if (len(password.strip()) == 0):
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
            
def logon():
    print(f"Please Login")
    print("...")

    username = input('Username: ')
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
                print(f"You Last Scored: {points} Points")
                question_answer(username)
                play_again_question(username)
                break
                    
            else:
                print("Password Incorrect")
                login_register()
                    
        elif i == len(username_list)-1:
                print("Username Not Found!")
                login_register()
                break
    
    
                

def login_register():
    inital_question = input("Do You Have An Account? y/n: ")
    if inital_question == "n":
        create_new_user()
        
    
    if inital_question == "y":
        logon()
    
    else:
        login_register()

        
               
def question_answer(username):
    
    qa_username = username
    qa_username_cell = login.find(qa_username)
    answer_list = answer_col
    answer_list.remove("answer")
    question_list = question_col
    question_list.remove("question")

    print("...")
    print("Ready...")
    print("Steady...")
    print("Let's Begin!!!")
    

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
    

def scoreboard():
    points_list = points_col
    points_list.remove("points")
    points_list = [int(i) for i in points_list]
    points_list.sort()
    print(f"All time highest Score: {points_list[-1]} Points")

def play_again_question(username):
    play_again = input("Do you want to play again? y/n: ")

    if play_again == "y":
        question_answer(username)
    
    else:
        print("Goodbye!")







def main():
    start_program()
    login_register()
   
    
   

   






main()

