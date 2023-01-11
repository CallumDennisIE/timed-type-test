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
SHEET = GSPREAD_CLIENT.open('timed_type_test_questions')


def get_question(user_difficulty):
    """
    Get a question from the Google Sheet, based on the difficulty selected by
    the user.
    """

    # Dictionary to pair column numbers with difficulty
    question_difficulty = {'easy': 1, 'hard': 2}

    # Store the worksheet as a variable
    questions = SHEET.worksheet('questions')

    # Get the question from the correct difficulty, specified by the user
    question = questions.col_values(question_difficulty[user_difficulty])

    return question


user_question = get_question('hard')
print(user_question)
