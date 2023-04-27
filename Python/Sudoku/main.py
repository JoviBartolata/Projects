#!/usr/bin/python
""" Main.py - main file that will run the program """
__author__ = "---"
__copyright__ = "Copyright Dec 2022, Game Final Project, 2022F-T1 AML 1214 - Python Programming 02 (DSMM Group 2)"
__email__ = " student@mylambton.ca"
__credits__= ""


# Import modules
import game as game
import login_signup as login_signup
import user as user
import os

# Change the current working directory
os.chdir(r'Python\Sudoku')


# -----------------------------------------------------------------------------------
# main()
#   
# Purpose:  Entry point of game application
#           
# Output:   game application is run
#           Return None
#           
# -----------------------------------------------------------------------------------
def main():
    # Initialize values
    inLogin = "Y"
    newSignup = "N"
    
    while inLogin.upper() == "Y":   # Loop while user wants to log in
        
        if newSignup == "Y":    # If log-in is executed right after sign-up, do not print initial message
            pass
        else:
            inLogin = input("\nHello! Do you have an existing account with us? (Y/N) ").strip()
        
        # If user has an existing account
        if inLogin.upper() == "Y":
            loginResult = login_signup.log_in()   # Verify log-in information
            
            # If User Password Database does not exist, ask if user would like to sign up
            if loginResult == None:
                inSignup = input("\nWould you like to sign up? (Y/N) ").strip()
                # If user wants to sign up, invoke the SignUp function
                if inSignup.upper() == "Y":
                    login_signup.sign_up()
                    inLogin = "Y"
                    newSignup = "Y"
                # If user doesn't want to sign up, end the session.
                else:
                    print("\nGoodbye!")
                    break
                
            # If log-in verification is unsuccessful, end the session
            elif loginResult == False:
                break
            
            # If log-in verification is successful, start the game
            else:
                print("Please go to the newly opened Python window to start playing.")
                currPlayer = user.Player(loginResult)    # Create player object
                game.start_game(currPlayer.userName)            # Invoke game functions
                        
        # If user does not have an existing account, ask if user would like to sign up
        elif inLogin.upper() == "N":
            inSignup = input("\nWould you like to sign up? (Y/N) ").strip()
            # If yes, invoke the SignUp function. If sign-up is successful, proceed to log-in verification.
            if inSignup.upper() == "Y":
                login_signup.sign_up()
                inLogin = "Y"
                newSignup = "Y"
            # If user doesn't want to sign up, end the session.
            else:
                print("\nGoodbye!")
                break

        # If user input is invalid (not Y or N), end the session
        else:
            print("\nGoodbye!")
            break




''' Place where we call the main function to execute the game application '''
main()
''' -----------------------------------------------------------------------------'''

