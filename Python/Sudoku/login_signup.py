#!/usr/bin/python
""" login_signup.py - login_signup file """
__author__ = "---"
__copyright__ = "Copyright Dec 2022, Game Final Project, 2022F-T1 AML 1214 - Python Programming 02 (DSMM Group 2)"
__email__ = " student@mylambton.ca"
__credits__= ""


# Import the os module
import os


# -----------------------------------------------------------------------------------
# SignUp()
#   
# Purpose:  This functions help user register to the database so user can log in in the future
#           
# Output:   Prompts user with option to signup
#           
# -----------------------------------------------------------------------------------
def sign_up():
    
    print("\n--- Sign-up ---")

    # Username creation
    def createUsername():
        inUsername = input("Input Username: ")      # User input
        
        # If username contains a comma or space, ask user to enter a different username
        if ("," in inUsername) or (" " in inUsername):
            print("Invalid value. Username should NOT contain comma and space. Please try again.\n")
            inUsername = createUsername()
            
        # If username and password have valid values, match username against the database
        elif os.path.exists("{0}\{1}".format(os.getcwd(),"User_password_database.txt")) == True:
            userDatabase = open("User_password_database.txt","r")   # Open the database
            records = userDatabase.readlines()                      # Read contents of the database
              
            for record in records:                      # For every record in the database
                savedUserName = record.split(",")[0]    # Get saved username
                               
                # If username already exists, ask user to enter a different username
                if inUsername == savedUserName:
                    userDatabase.close()
                    print("Username already exists. Please choose another one.\n")
                    inUsername = createUsername()
                    
        return inUsername
            
    # Password creation
    def createPassword():
        inPassword = input("Input Password: ")      # User input
        
        # If password contains a comma or space, ask user to enter a different password
        if ("," in inPassword) or (" " in inPassword):
            print("Invalid value. Password should NOT contain comma and space. Please try again.\n")
            inPassword = createPassword()
            
        return inPassword
    
    # Create and verify username and password    
    inUsername = createUsername()
    inPassword = createPassword()
        
    # Append username and password to the database 
    userDatabase = open("User_password_database.txt","a")
    newLine = [inUsername,",",inPassword,"\n"]
    userDatabase.writelines(newLine)
    userDatabase.close()
    
    print("\nSucessfully created a new account.")



# -----------------------------------------------------------------------------------
# LogIn()
#   
# Purpose:  This functions help user log in to play game if user is valid
#           
# Output:   
#           - Returns the username (inUsername) if verification is successful
#           - Returns False if verification is unsuccessful
#           - Returns None if User Password Database does not exist      
# -----------------------------------------------------------------------------------
def log_in():
    
    print("\n--- Log-In ---")

    # User inputs
    inUsername = input("Username: ").strip()
    inPassword = input("Password: ").strip()
    
    # If User Password Database exists, open the file
    if os.path.exists("{0}\{1}".format(os.getcwd(),"User_password_database.txt")) == True:
        userDatabase = open("User_password_database.txt","r")   # Open the database
        records = userDatabase.readlines()                      # Read contents of the database
        counter = 0                                             # Counter is used to check if the loop has reached the end of file
        
        # For every record in the database
        for record in records:
            savedUserName = record.split(",")[0].strip()    # Get saved username
            savedPassword = record.split(",")[1].strip()    # Get saved password
                
            # If username and password are correct
            if (inUsername == savedUserName) and (inPassword == savedPassword):
                userDatabase.close()                                            # Close the database
                print("{0}{1}{2}".format("\nWelcome, ",inUsername,"!"))         # Welcome user
                return inUsername                                               # Return the username entered by user
            
            # Otherwise, continue looping and adding 1 to the counter
            counter += 1                                                        
        
        # If there is no match in any of the records (i.e., end of file has been reached), ask user to try again
        if counter == len(records):
            inRetry = input("\nAuthentication failed. Would you like to try again? (Y/N) ")
            # Continue looping as long as user wants to retry
            if inRetry.upper() == "Y":
                loginResult=log_in()
                return loginResult
            # Exit loop if user no longer wants to retry
            else:
                print("\nSee you next time!")
                return False

    # If User Password Database does not exist, prompt user to sign up first to create the initial database
    else:
        print("\nUsername does not exist. Please sign up first.")
        return None