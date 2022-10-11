# The Worlds Greatest Quiz
The worlds greatest quiz is a true or false quiz with an account functionality to store points. 
The game has been built with python and deployed with Heroku.
The aim of the game is to get the most points of all time by continously playing the game.

[Link to my code via Github pages](https://github.com/PritenMakwana44/the-worlds-greatest-quiz/)

[Link to my Application deployed by Heroku](https://the-worlds-greatest-quiz.herokuapp.com/)

![Responsive](/readme-resources/images/res-app.png)

## How To Play
First you will need to register or logon when starting the game. 
Then the quiz will start, it's as simple as typing "T" for true or "F" for false for each question.
There are 10 questions and you get 10 points for right answers and 0 for wrong. 
At the end of each game you will be asked if you want to play again.
The aim is to answer the most questions right to build your points so you have the most questions points of all time.

## Features
### Existing Features
* Account Register/login
    * Question is asked if you have an existing account.
    * y takes you to logon page.
    * n takes you to register page.

![Account-prompt](/readme-resources/images/account-prompt.png)

* Register
    * You have to create a valid username.
    * Checks if username exists already. It will error if there are spaces.
    * Once confirmed it will then ask for a password again can't have spaces.
    * Both usernames and passwords have error messages which feedback.
    * Once account is created it will set the new users points to 0 and take you to the logon page.

![create-new-user](/readme-resources/images/create-new-user.png)

* Logon
    * Type username to login to existing account.
    * If username doesn't exist then an error comes up.
    * If username is found then a password box comes up. Again if password is valid then it will take user straight into game.

![create-new-user](/readme-resources/images/login-question.png)

* Quiz
    * The quiz has 10 questions which are all diffrent.
    * Each question has a true or false answer.
    * If you answer correct then you get a prompt and 10 points are added to your account.
    * If incorrect then you get 0 points.
    * If you type anything apart from t or f for true and false then you get a error message.
    * At the end of the 10 questions you can either play again or thre is an option to exit the game.

![questions](/readme-resources/images/questions.png)

![invalid-question-input](/readme-resources/images/invalid-input.png)

![play-again](/readme-resources/images/play-again.png)

### Future Features
* All time point leaders scoreboard.
    * The idea is to have a full scoreboard which shows top 10 users with the amount of points they have.
    * There could be an option to go to this scoreboard at the end of every game. 
* More Graphics and colours.
    * Adding some graphics to make the game look a bit more fun. Make making the title 3d.
    * Adding a red colour if answer is wrong and a green if it's right.
* Showing your current tally of points.
    * From logon onwards points can be shown as you get answers right or wrong to make it more competative.
* Question Catagories
    * There can be a diffrent set of questions on diffrent themes if wanted. 
    * However I think that it would be best to leave the questions mixed as that's what makes it unqiue! So this is up for question.
* Add question per round.
    * Function which allows user to add question at the end of every game to make the quiz more fun.
    * The user will never see their own question.
    * Question is submitted then reviewed before being added.

## Data Model
I chose not to use classes as felt they wouldn't fit in so well. Instead I chose to use Gspread and a googlesheet to keep the project simple.
a Googlesheet is used to store data such as login username, password and points. Then the bank of questions and answers. Although a Googlesheet wouldn't be best as the data grows, the way in which it's been created means the structure is now there. The database can be swapped to a industrial strength solution later on.

## Testing
* Firstly the template constructed by Code Institute have add-ons which checks that the code remains at a pep8 standard. Hence no errors are in my code apart from 3 add-on issues. The errors are known and do not effect code in anyway so can be ignored.
* Tested each part of my code especially inputs by typing invalid charecters or no charecters etc... All is working correctly.
* Checked Google spreadsheet to make sure data is updating correctly.
* Tested from both Gitpod terminal and Heroku site. 

## bugs

### Solved Bugs
### Remaining bugs

## Validator Testing

## Deployment

## Credits










structure of login_register function:
https://python-forum.io/thread-6106.html
append to row:
https://docs.gspread.org/en/latest/
help with while loop:
https://www.toolsqa.com/python/python-while-loop/

help with line 60 bug:
https://www.howtouselinux.com/post/get-last-element-of-a-list-in-python#:~:text=The%20best%20way%20to%20get,gets%20the%20second%20to%20last.

random:
https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
https://www.w3schools.com/python/module_random.asp

codensed if code: 
https://stackoverflow.com/questions/4915920/how-to-delete-an-item-in-a-list-if-it-exists

sleep:

https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=Make%20your%20time%20delay%20specific,after%20a%20slight%20delay.%22)

while loop:
https://www.geeksforgeeks.org/iterate-over-a-list-in-python/

for loop:
https://www.w3schools.com/python/python_for_loops.asp


enumerate: 
https://realpython.com/python-enumerate/
https://www.geeksforgeeks.org/python-accessing-index-and-value-in-list/