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
            username = input("Enter new Username: ")
            username_list = login.col_values(1)
            while username in username_list:
                print(f"'{username}' already exists")
                break
                username = input("Enter new Username: ")
            else:   
                password = input("Enter new Password: ")
                print(f"Creating Account for {username}...")
                update_worksheet = []                
                update_worksheet.append(username)
                update_worksheet.append(password)
                login.append_row(update_worksheet)
                print(f"Account created Successfully!")
                inital_question ="y"
                break
    
    
    if inital_question == "y":
        print(f"Please login")
        username_list = login.col_values(1)
        password_list = login.col_values(2)
        login_username = input("Username: ")
        for i in range(len(username_list)):
            if username_list[i] == login_username:
                login_password = input('Password: ')
            else:
                print("username not found")
                if password_list[i] == login_password:
                    print('Success')
                else:
                    print('fail')

        



    


def main():
    login_register()


main()
