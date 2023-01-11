import gspread
from google.oauth2.service_account import Credentials
from difflib import SequenceMatcher

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
    # Currently only taking the first non-header value in the column
    question = questions.col_values(question_difficulty[user_difficulty])[1]

    return question


def get_input(question):
    """
    Ask the user to input the question and return the result
    """

    print("Type the following question, as quick as possible:")
    print(question)
    print()
    answer = input("Type here:\n")

    return answer


def calculate_accuracy(question, answer):
    """
    Calculate the similarity of the question and the answer and return as a
    percentage
    """

    # Calculate Similarity
    similarity = SequenceMatcher(lambda x: x == " ", question, answer)

    # Get the similarity score as a decimal
    decimal = similarity.ratio()

    # Convert the decimal to a percentage
    percentage = round(decimal * 100, 2)

    return percentage


user_question = get_question('hard')

user_input = get_input(user_question)

accuracy = calculate_accuracy(user_question, user_input)
print(accuracy)
