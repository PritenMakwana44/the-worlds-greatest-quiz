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


print("Welcome to the worlds greatest quiz")
print("Instructions\n First login or register\n To play the game type true or false on each question\n The highest score is 100 points\n Each time you play there will be new questions!\n No cheating ;)")

def login_register():
    inital_question = input("Do you have an account? y/n: ")
    if inital_question == "n":
        print(f"Redirection to Registration...")
        print(f"...")
        print(f"...")
        while True:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            confirm_password = input("Confirm Password: ")
            print(f"Creating Account for {username}...")
            if password == confirm_password:
                
                update_worksheet = []
                login = SHEET.worksheet('login')
                update_worksheet.append(username)
                update_worksheet.append(password)
                login.append_row(update_worksheet)
                print(f"Account created Successfully!")
                inital_question ="y"
                break
            
            print("Passwords do not match!")
    
    if inital_question == "y":
        print(f"Please login")
        while True:
            login_username = input("Username: ")
            login_password = input("Password: ")
            print("Welcome {Username}")
            break
            





    


def main():
    login_register()


main()
