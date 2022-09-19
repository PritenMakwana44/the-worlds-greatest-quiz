import gspread
from google.oauth2.service_account import Credentials

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

print("Welcome to the worlds greatest quiz")
print("Instructions\n First login or register\n To play the game type true or false on each question\n The highest score is 100 points\n Each time you play there will be new questions!\n No cheating ;)")

def login_register():
    inital_question = input("Do you have an account? y/n: ")
    if inital_question == "n":
        while True:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            confirm_password = input("confirm Password: ")
            if password == confirm_password:
                login.append_row(username)
                login.append_row(password)
                inital_question ="y"
                break
            
            print("Passwords do not match!")
    
    if inital_question == "y":
        while True:
            login_username = input("username: ")
            login_password = input("password: ")
            print("welcome back!")
            break
            





    


def main():
    login_register()


main()

        
        


