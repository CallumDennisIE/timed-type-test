# Timed Type Test

## Contents
* [About](#about)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
* [Design](#design)
* [Features](#features)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
* [Testing](#testing)
* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)

## About
Timed Type Test is a typing game, aimed at people that want to improve their typing skills. The game shows the user a sentence, the user then has to input the sentence as accuratley as they can and as quick as possible. The game has different difficulties and will show the users speed and accuracy scores. Timed Type Test also allows users to add their own sentences, to increase replayability.

[View the live project here.](https://timed-type-test.herokuapp.com/)

[Back to top!](#timed-type-test)

## User Experience
### User Stories
#### User who wants to keep replaying the game:
- I want to be able to add my own questions in the program.
#### User who wants to improve their typing skills:
- I want to be shown how close I was to getting the answer right.
#### User that wants to compete with friends:
- I want to be able to know my score.

[Back to top!](#timed-type-test)

## Design
### Flowchart:
A flowchart was created in this project to plan out the possible functions that would be needed. The functions highlighted in blue are the ones utilised in the final project. As shown, some functionaility in the project was not included due to time constraints, for example adding to a highscore sheet. As the highscore system did not impact the primary gameplay loop, it was not a priority.
<details>
<summary>Click for Image: Flowchart</summary>

![Flowchart](/assets/images/readme/flowchart.png)

</details>

[Back to top!](#timed-type-test)

## Features

### Menu:
The project uses a menu system that allows users to select between playing the game, adding a question to the avaible questions or exiting the code.

### Add a Question:
The user can add a question to the Google Sheet, allowing them to then play that question later in the game. The user will be asked for the difficulty of the question and then asked to input their question. This will then be added to the next row of the difficulty column in the Google Sheet.

### Play the game:
When the user plays the game, they are asked which game difficulty they would like to play. This decides which column of questions is taken from the Google Sheets. The game will then start 3 rounds of the game, if there is not enough questions in the selected diffculty, the user will be prompted to add more questions to play.

If there is enough questions, then a sentence will be diplayed to the user, the user will have to input the provided sentence as accuratley and as quick as possible. The score out of 100 is shown for both accuracy and speed on all questions, as well as the time taken and the time left.

[Back to top!](#timed-type-test)

## Technologies Used
### Languages Used
- Python

### Frameworks, Libraries & Programs Used
- [Git](https://git-scm.com/):
    - Git commands were used for version control.
- [GitHub](https://github.com/):
    - Project was hosted on GitHub and GitHub Pages hosted the live site.
- [Gitpod](https://www.gitpod.io/):
    - The project was developed using Gitpod development environment.
- [Heroku](https://www.heroku.com/)
    - The project was deployed using Heroku.
- [Lucidchart](https://www.lucidchart.com/pages/)
    - The flowchart was created using Lucidchart.
- [Python difflib](https://docs.python.org/3/library/difflib.html)
    - The Python difflib module was used to calculate similarity between the sentence and user input.
- [Python time](https://docs.python.org/3/library/time.html)
    - The Python time module was used to calculate the time taken for the user's input.
- [gspread API](https://docs.gspread.org/en/latest/)
    - The Python gspread API was used to access Google Sheets
- [Python Credentials](https://pypi.org/project/credentials/)
    - Credentials was used to generate a credentials file for Google OAuth

[Back to top!](#timed-type-test)

## Deployment & Local Development
### Deployment
### Local Development

[Back to top!](#timed-type-test)

## Testing
[View the project testing document here.](TESTING.md)

## Credits
### Code
The following code was taken from the [difflib Python documentation](https://docs.python.org/3/library/difflib.html#sequencematcher-examples):

```
similarity = SequenceMatcher(lambda x: x == " ", question, answer)
```

[Back to top!](#timed-type-test)