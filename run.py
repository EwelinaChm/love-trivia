import gspread
from google.oauth2.service_account import Credentials
from questions import quiz

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scores')


def intro_message():
    print("Welcome to LOVE TRIVIA game! \nAre you ready to test your knowledge?")
    print("There are a total of 20 questions, you can skip a question anytime by typing 'skip', you have 3 attempts to give a correct answer")
    input("Press any key to start the game")
    return True 


intro = intro_message()
print(intro)