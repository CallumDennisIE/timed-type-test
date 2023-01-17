# Timed Type Test - Testing
[View the project README here.](README.md)

## Contents
* [Automated Testing](#automated-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Solved Bugs](#solved-bugs)

## Automated Testing:
The code was tested using the [PEP8CI Python Linter](https://pep8ci.herokuapp.com/).
This was successful as the results show:
```
All clear, no errors found
``` 

[Back to top!](#timed-type-test---testing)

## Bugs:
### Known Bugs
#### Negative Speed:
If the user takes too long answering the question and the time takes longer than the maximum time, then the speed score will be a negative. This should be remedied by setting the speed score to 0 if speed is less than 0.

#### Menu Input - String:
The menu system will only allow the number to be inputted instead of allowing the number and the corresponding string. For example the option '1) Easy', will only allow '1' to be the correct input rather than also allowing 'Easy'. This was due to the validation of the menu dictionaries causing errors, and therefore the string validation was removed due to time constraints.

[Back to top!](#timed-type-test---testing)