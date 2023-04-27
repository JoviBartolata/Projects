------------------
SUDOKU
------------------
Game Final Project, 2022F-T1 AML 1214 - Python Programming 02 (DSMM Group 2)
    Jefford Seconde
    Jovi Bartolata
    Maricris Resma
    Luz Zapanta


------------------
File Description
------------------
User.py - file representing user class/object ← optional to be in a separate file
Game.py - functions associated with the game
Main.py - main file that will run the program
Login_Signup.py - functions associated with verifying a user, and
                - functions associated with creating a user and saving the information to a database
User_password_database.txt - username and password database for login verification. This is created during the game.
Save_data.txt - can be used to store and access saved information. This is created during the game.
puzzle_1.txt - file containg the default grids


------------------
Instructions
------------------
- Run main() to play the game.
- After successful log-in, a Python window will be opened. 
- During the actual game (board is diplayed), press:
    0 - To clear the cell
    ENTER - To check if the current board is complete
    QUIT or F6 - To exit the board


---------------------
High Level Game Flow 
---------------------

- Log-in / Sign-up:
    If player wants to sign-up, create an account first before proceeding to log-in.
    If player has an existing account, proceed to log-in.
    If log-in verification is successful, start the game.

- Main Menu:
    If player selects N - PLAY NEW GAME, go to level selection menu.
    If player selects O - PLAY PREVIOUSLY SAVED GAME, go to level selection menu.
    If player selects X - LOG OUT, end the game.

- Level Selection Menu:
    If player selects 1 - EASY, get either the default or saved board for this level depending on the option selected in the Main Menu.
    If player selects 2 - MEDIUM, get either the default or saved board for this level depending on the option selected in the Main Menu.
    If player selects 3 - HARD, get either the default or saved board for this level depending on the option selected in the Main Menu.
    If player selects B - GO BACK TO MAIN MENU, return to  Main Menu.

- During the Game:
    If player enters a value, check if the value is valid or not. If valid, display it in the cell.
    If player enters 0, clear the cell.
    If player presses Enter, check if the board is complete and correct. Then player need to press Enter again to go back to the board.
    If player presses Quit or F6, prompt Save options. If player selects Save, save the current session and go back to Main Menu.


-------------------------
puzzle_1.txt cheat sheet 
-------------------------
#1.1
level_easy_1 =[
        [0, 7, 0, 0, 2, 0, 0, 4, 6],
        [0, 6, 0, 0, 0, 0, 8, 9, 0],
        [2, 0, 0, 8, 0, 0, 7, 1, 5],
        [0, 8, 4, 0, 9, 7, 0, 0, 0],
        [7, 1, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 1, 3, 0, 4, 8, 0],
        [6, 9, 7, 0, 0, 2, 0, 0, 8],
        [0, 5, 8, 0, 0, 0, 0, 6, 0],
        [4, 3, 0, 0, 8, 0, 0, 7, 0],
    ]
level_easy_1_answer = [
        [8, 7, 5, 9, 2, 1, 3, 4, 6],
        [3, 6, 1, 7, 5, 4, 8, 9, 2],
        [2, 4, 9, 8, 6, 3, 7, 1, 5],
        [5, 8, 4, 6, 9, 7, 1, 2, 3],
        [7, 1, 3, 2, 4, 8, 6, 5, 9],
        [9, 2, 6, 1, 3, 5, 4, 8, 7],
        [6, 9, 7, 4, 1, 2, 5, 3, 8],
        [1, 5, 8, 3, 7, 9, 2, 6, 4],
        [4, 3, 2, 5, 8, 6, 9, 7, 1],
    ]

#2.1
level_med_1 = [
        [5, 0, 7, 2, 0, 0, 0, 9, 0],
        [0, 0, 6, 0, 3, 0, 7, 0, 1],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [1, 0, 0, 4, 9, 0, 0, 0, 7],
        [0, 0, 0, 5, 0, 8, 0, 0, 0],
        [8, 0, 0, 0, 2, 7, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 0, 9],
        [2, 0, 9, 0, 8, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 9, 3, 0, 8],
    ]
level_med_1_answer = [
        [5, 1, 7, 2, 6, 4, 8, 9, 3],
        [9, 2, 6, 8, 3, 5, 7, 4, 1],
        [4, 8, 3, 9, 7, 1, 5, 6, 2],
        [1, 3, 5, 4, 9, 6, 2, 8, 7],
        [7, 9, 2, 5, 1, 8, 4, 3, 6],
        [8, 6, 4, 3, 2, 7, 9, 1, 5],
        [3, 7, 8, 6, 4, 2, 1, 5, 9],
        [2, 5, 9, 1, 8, 3, 6, 7, 4],
        [6, 4, 1, 7, 5, 9, 3, 2, 8],
    ]

#3.1
level_hard_1 = [
        [0, 0, 6, 5, 0, 0, 0, 0, 8],
        [0, 9, 5, 0, 0, 0, 0, 2, 0],
        [7, 0, 0, 9, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 4, 0, 2, 7, 0],
        [0, 0, 0, 8, 7, 3, 0, 0, 0],
        [0, 7, 9, 0, 5, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 8, 0, 0, 9],
        [0, 5, 0, 0, 0, 0, 8, 1, 0],
        [3, 0, 0, 0, 0, 5, 4, 0, 0],
    ]

level_hard_1_answer = [
        [1, 3, 6, 5, 2, 4, 7, 9, 8],
        [8, 9, 5, 3, 6, 7, 1, 2, 4],
        [7, 2, 4, 9, 8, 1, 3, 5, 6],
        [5, 8, 3, 6, 4, 9, 2, 7, 1],
        [2, 6, 1, 8, 7, 3, 9, 4, 5],
        [4, 7, 9, 1, 5, 2, 6, 8, 3],
        [6, 4, 2, 7, 1, 8, 5, 3, 9],
        [9, 5, 7, 4, 3, 6, 8, 1, 2],
        [3, 1, 8, 2, 9, 5, 4, 6, 7],
    ]