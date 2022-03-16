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
    print("There are a total of 20 questions, you can skip a question anytime by typing 'skip', you have 2 attempts to give a correct answer")
    input("Press any key to start the game")
    return True 


def check_answer(question, answer, attempts, score):
    if quiz[question]['answer'].lower() == answer.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def play_game():
    while True:
        score = 0
        for question in quiz:
            attempts = 2
            while attempts > 0:
                print(quiz[question]['question'])
                answer = input("Your answer: ")
                if answer == "skip":
                    break
                check = check_answer(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
            
        break
    print(f"Your final score is {score}!\n\n")

intro = intro_message()
play_game()