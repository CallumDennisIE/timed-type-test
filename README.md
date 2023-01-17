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