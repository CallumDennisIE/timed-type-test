import gspread
import time
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


class Game:
    """
    The class for each game session that is started.
    """

    def __init__(self, max_time):
        self.max_time = max_time
        self.start_time = None
        self.answer_time = None
        self.menu_options = {'play': '1',
                             'add': '2', 
                             'exit': '3'}

    def play_menu(self):
        """Displays the menu at game start and asks for user input.

        Returns:
            menu_input (string): The users option selected on the menu.
        """
        valid = False

        while not valid:
            print("Timed Type Test Menu:")
            
            for option in self.menu_options:
                print(f"{self.menu_options[option]}) {option.capitalize()}")

            menu_input = input("Enter your menu option:\n")

            valid = self.validate_menu(menu_input)
            if not valid:
                print("Please enter a valid option on the menu\n")

        return menu_input

    def validate_menu(self, user_input):
        """Validates the users input on the starting menu, 
        checks to see if the value is one of the availble options.

        Args:
            user_input (user_input): The option selected by the user on the
            starting menu

        Returns:
            valid (bool): A boolean, if the value is a vlid value or not.
        """

        # Validate if the user input is a valid option.
        if user_input.lower() in self.menu_options or user_input in \
                self.menu_options.values():
            return True

        return False

    def get_question(self, user_difficulty):
        """Get a question from the Google Sheet, based on the difficulty
        selected by the user.

        Args:
            user_difficulty (string): The difficulty that the user sets
            the game to.

        Returns:
            question (string): A question from the Google Sheet
        """

        # Dictionary to pair column numbers with difficulty
        question_difficulty = {'easy': 1, 'hard': 2}

        # Store the worksheet as a variable
        questions = SHEET.worksheet('questions')

        # Get the question from the correct difficulty, specified by the user
        # Currently only taking the first non-header value in the column
        question = questions.col_values(
            question_difficulty[user_difficulty])[1]

        return question

    def get_input(self, question):
        """Ask the user to input the question and return the result.

        Args:
            question (string): The value will be output to the user, for them
            to copy.

        Returns:
            answer (string): The users answer to the question argument.
        """

        # The time before the question was asked
        self.start_time = time.time()

        print("Type the following question, as quick as possible:")
        print(question)
        print()
        answer = input("Type here:\n")

        # The time after the question was asked
        self.answer_time = time.time()
        return answer

    def calculate_accuracy(self, question, answer):
        """Calculate the similarity of the question and the answer and return
        as a percentage.

        Args:
            question (string): The question that will have the answer tested
            against it, to calculate the similarirty.
            answer (string): The value that will be tested against the
            question, to calculate the similarity.

        Returns:
            percentage (float): The percentage value of the similarity between
            the provided question and answer.
        """

        # Calculate Similarity
        similarity = SequenceMatcher(lambda x: x == " ", question, answer)

        # Get the similarity score as a decimal
        decimal = similarity.ratio()

        # Convert the decimal to a percentage
        percentage = round(decimal * 100, 2)

        return percentage

    def calculate_speed(self):
        """Calculate the speed of the users answer, using the start and answer
        time, then calculate the time remainign from the maxium time.

        Returns:
            speed (float): The percentage value of the time taken divided by
            the maximum time.
            time_taken (int): The time the user took to answer the question.
            time_left (int): The time taken subtracted from the max time.
        """
        # Calculate time taken to answer the question
        time_taken = self.answer_time - self.start_time

        # Round the seconds taken to the nearest full second
        time_taken = round(time_taken)

        time_left = self.max_time - time_taken

        # Calculate the percentage of time taken from max time
        speed = round((time_taken / self.max_time) * 100, 2)

        # Reverse the percentage to get score out of 100
        speed = 100 - speed

        return speed, time_taken, time_left

    def output_results(self, question, answer, time_left, time_taken, speed, 
                       accuracy):
        """Output the game results that are passed in.

        Args:
            question (string): The question from the google Sheet, that the
            user had to answer.
            answer (string): The users answer to the question argument.
            time_left (int): The time taken subtracted from the max time.
            time_taken (int): The time the user took to answer the question.
            speed (float): The percentage value of the time taken divided by
            the maximum time.
            accuracy (float): The percentage value of the similarity between
            the provided question and answer.
        """
        print(f"\nQuestion: {question}\nAnswer: {answer}\n")
        print(f"Time left: {time_left} Seconds")
        print(f"Time taken: {time_taken} Seconds")
        print(f"Speed: {speed}%")
        print(f"\nAccuracy: {accuracy}%")


new_game = Game(30)

new_game.play_menu()

user_question = new_game.get_question('hard')

user_input = new_game.get_input(user_question)

accuracy = new_game.calculate_accuracy(user_question, user_input)

speed, time_taken, time_left = new_game.calculate_speed()

new_game.output_results(user_question, user_input, time_left, time_taken, 
                        speed, accuracy)
