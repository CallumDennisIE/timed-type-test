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

    def __init__(self):
        self.max_time = 30
        self.num_rounds = 3
        self.start_time = None
        self.answer_time = None
        self.menu_options = {'1': 'play',
                             '2': 'add',
                             '3': 'exit'}
        self.difficulty_options = {'1': 'easy', '2': 'hard'}

    def output_options(self, options):
        """Displays the selections availble to a user

        Args:
            options (dict): A dictionary of options availble to the user.
            The key is the order of the option.
            The value a string indicating the option name.

        """
        for option in options:
            print(f"{option}) {options[option].capitalize()}")

    def validate_options(self, options, option_input):
        """Validates input to see if it is in the options dictionary.

        Args:
            options (dict): A dictionary of options, to be validated against.
            option_input (string): A value to test if in the options
            dictionary.

        Returns:
            bool: If the input value is in the options dictionary.
            output (string/None): The validated input value
        """

        if option_input in options:
            option_input = options[option_input]
            return True

        return False

    def get_col_length(self, sheet, column):
        """ Gets the length of the selected column.

        Args:
            sheet (Class): The Google Sheet, that contaisn the column.
            column (int): The number of the cuolumn, that will be measured.

        Returns:
            length (int): The number of rows in the column.
        """

        length = len(sheet.col_values(column))

        return length

    def play_menu(self):
        """Displays the menu at game start and asks for user input.

        Returns:
            menu_input (string): The users option selected on the menu.
        """
        valid = False

        while not valid:
            print("Timed Type Test Menu:")

            self.output_options(self.menu_options)

            menu_input = input("Enter your menu option:\n").lower()

            valid = self.validate_options(self.menu_options, menu_input)
            if not valid:
                print("Please enter a valid option on the menu\n")

        if menu_input == "1":
            self.play_game()
        elif menu_input == "2":
            self.add_question()

        return menu_input

    def play_game(self):
        """Calls all the necessary functions to play the game.
        """
        game_difficulty = self.get_difficulty()

        if game_difficulty == '1':
            self.max_time = 30

        elif game_difficulty == '2':
            self.max_time = 15

        # Number of questions is the column length -1, to avoid the column name
        num_questions = self.get_col_length(SHEET.worksheet('questions'),
                                            game_difficulty) - 1

        if num_questions >= self.num_rounds:
            for rnd in range(1, self.num_rounds+1):
                print(f"\nRound {rnd} / {self.num_rounds}")

                user_question = self.get_question(game_difficulty, rnd)

                user_input = self.get_input(user_question)

                accuracy = self.calculate_accuracy(user_question, user_input)

                speed, time_taken, time_left = self.calculate_speed()

                self.output_results(user_question, user_input, time_left,
                                    time_taken, speed, accuracy)
        else:
            print("Not enough questions on the selcted diffculty")
            print("Please add more and try again.")

        self.play_menu()

    def add_question(self):
        """Calls all the necessary functions to add a question.
        """
        input_question, input_difficulty = self.get_input_question()

        self.add_input_question(input_question, input_difficulty)

        self.play_menu()

    def get_input_question(self):
        """Gets the selected difficulty and the question that the user would
        like to input and returns them.

        Returns:
            user_question (string): The question that the user wants to add to
            the existing questions.
            difficulty (int): A number, corresponding to the selected
            difficulty
        """

        print("Which difficulty question are you adding:\n")
        difficulty = self.get_difficulty()

        user_question = input(
            'Please enter the question you would like to add: \n')

        return user_question, difficulty

    def add_input_question(self, question, difficulty):
        """ Updates the Google Sheet, with the question in the correct column,
        depending on difficulty

        Args:
            question (string): The question that the user wants to add to
            the existing questions.
            difficulty (int): A number, corresponding to the selected
            difficulty
        """

        questions = SHEET.worksheet('questions')
        # The column number is equal to the difficulty number value
        column = difficulty

        # Row is length of the selected column + 1, to include the column name
        row = self.get_col_length(questions, column) + 1

        questions.update_cell(row, column, question)

    def get_difficulty(self):
        """Displays the possible difficulty options to the user and gets the
        users input

        Returns:
            valid_difficulty (string): The difficulty selected by the user,
            that has been validated.
        """
        print("\nGame Difficulty:")

        valid = False
        while not valid:
            self.output_options(self.difficulty_options)

            difficulty = input("Please enter the game difficulty:\n")

            valid = self.validate_options(self.difficulty_options, difficulty)

            if not valid:
                print("Please enter a valid difficulty\n")
            else:
                valid_difficulty = difficulty

        return valid_difficulty

    def get_question(self, user_difficulty, row):
        """Get a question from the Google Sheet, based on the difficulty
        selected by the user.

        Args:
            user_difficulty (string): The difficulty that the user sets
            the game to.
            row (int): The row, to get the question from.

        Returns:
            question (string): A question from the Google Sheet
        """

        # Store the worksheet as a variable
        questions = SHEET.worksheet('questions')

        # Get the question from the correct difficulty, specified by the user
        # Currently only taking the first non-header value in the column
        question = questions.col_values(user_difficulty)[row]

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


new_game = Game()
new_game.play_menu()
