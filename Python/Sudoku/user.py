#!/usr/bin/python
""" User.py - file representing user class/object """
__author__ = "---"
__copyright__ = "Copyright Dec 2022, Game Final Project, 2022F-T1 AML 1214 - Python Programming 02 (DSMM Group 2)"
__email__ = " student@mylambton.ca"
__credits__= ""


# Import modules
import game as game
import os


''' -----------------------------------------------------------------------------------
 Puzzle()

 Description: class template for the default sudoku Puzzle contained in the game

 ----------------------------------------------------------------------------------- '''
class Puzzle():
    
    def __init__(self):
        self.easyGrid = []
        self.medGrid = []
        self.hardGrid = []

    # -----------------------------------------------------------------------------------
    # getDefaultGrid(self, inLevel: int)
    # 
    # Input:    inLevel - the difficulty level of the grid user wants to retrieve from whole Puzzle
    #   
    # Purpose:  This function returns the grid data of the default puzzle according to level requested
    #           
    # Output:   Corresponding grid list
    #           
    # -----------------------------------------------------------------------------------
    def get_default_grid(self, inLevel: int):
        if inLevel == game.LEVEL_EASY: return  self.easyGrid
        if inLevel == game.LEVEL_MEDIUM: return  self.medGrid
        if inLevel == game.HARD_LEVEL: return self.hardGrid
    
    # -----------------------------------------------------------------------------------
    #  getAllGridData(self, inFile)
    # 
    # Input:    inFile - input file from where the default sudoku puzzle is taken from
    #   
    # Purpose:  This function parses the input puzzle data file and assigns the corresponsing value to the puzzle grid values of all levels
    #           
    # Output:   None
    #           
    # -----------------------------------------------------------------------------------
    def get_all_grid_data(self, inFile):
        file=open(inFile,"r")
        for line in file:
            line_strip=line.strip()
            get_tag_data(self.easyGrid, file, line, line_strip,"easy")
            get_tag_data(self.medGrid, file, line, line_strip,"medium")
            get_tag_data(self.hardGrid, file, line, line_strip,"hard")

        

''' -----------------------------------------------------------------------------------
 Player()

 Description: class template for Players logged in in the game

 ----------------------------------------------------------------------------------- '''
class Player():
    def __init__(self, userName):
        self.userName = userName
        self.easyGrid = []
        self.medGrid = []
        self.hardGrid = []
        self.currPlayGrid = []
        self.isNewGame = True 
        self.currLevel = 0 # 0 means no game  previously played in the current session 
        
    # -----------------------------------------------------------------------------------
    # getSavedGrid(self, inLevel: int)
    # 
    # Input:    inLevel - the difficulty level of the grid user wants to retrieve from whole Puzzle
    #   
    # Purpose:  This function returns the saved grid data of the Player() according to level requested
    #           
    # Output:   Corresponding grid list
    #           
    # -----------------------------------------------------------------------------------
    def get_saved_grid(self, inLevel: int):
        if inLevel == game.LEVEL_EASY: return self.easyGrid
        if inLevel == game.LEVEL_MEDIUM: return self.medGrid
        if inLevel == game.HARD_LEVEL: return self.hardGrid

    # -----------------------------------------------------------------------------------
    # saveGame(self)
    #   
    # Purpose:  This functions saves a copy of the user's current game session.
    #           
    # Output: Creates Save_data.txt
    #
    # -----------------------------------------------------------------------------------
    def save_game(self):
                                
        # Delete all user data from the game database
        with open("Save_data.txt", "r") as input:
            with open("Save_data_temp.txt", "w") as output: # Create a temporary file for the updated database
                drop = "N"
                for line in input:
                    # Delete all records between <username> and <\username> tags
                    if line.strip() == "<" + self.userName + ">":
                        drop = "Y"
                    if drop == "N":
                        output.write(line)
                    if line.strip() == "<\\" + self.userName + ">":
                        drop = "N"                              
                        
        os.remove("Save_data.txt")                          # Delete the old database
        os.rename("Save_data_temp.txt","Save_data.txt")     # Save the temp file as the new database  

        # Convert grid data from list to string         
        def convert_to_string(inGrid):
            stringGrid = ""
            for item in inGrid:
                stringGrid = stringGrid + str(item).strip("[]").replace(",","") + "\n"
            return stringGrid

        # If the user is currently playing Easy, use the current session's data to populate the Easy level in the database
        # Otherwise, use the last saved data in the database
        if self.currLevel == game.LEVEL_EASY: sEasyGrid = convert_to_string(self.currPlayGrid)
        else: sEasyGrid = convert_to_string(self.easyGrid)
        
        # If the user is currently playing Medium, use the current session's data to populate the Medium level in the database
        # Otherwise, use the last saved data in the database
        if self.currLevel == game.LEVEL_MEDIUM: sMedGrid = convert_to_string(self.currPlayGrid)
        else: sMedGrid = convert_to_string(self.medGrid)
        
        # If the user is currently playing Hard, use the current session's data to populate the Hard level in the database
        # Otherwise, use the last saved data in the database
        if self.currLevel == game.HARD_LEVEL: sHardGrid = convert_to_string(self.currPlayGrid)
        else: sHardGrid = convert_to_string(self.hardGrid)
        
        # Recreate user's records in the database using the updated data
        gameDatabase = open("Save_data.txt","a")
        newLine = ["<" + self.userName + ">\n" +
                   "<easy>\n" + sEasyGrid + "<\easy>\n"
                   "<medium>\n" + sMedGrid + "<\medium>\n"
                   "<hard>\n" + sHardGrid + "<\hard>\n"
                   "<\\" + self.userName + ">\n"]
        gameDatabase.writelines(newLine)
        gameDatabase.close()

    # -----------------------------------------------------------------------------------
    # getSavedGame()
    #   
    # Purpose:  This function parses the Save_data.txt file and returns the player's 
    #           saved grid data for all levels
    #           
    # Output: None
    #           
    # -----------------------------------------------------------------------------------
    def get_saved_game(self):
        # If Save_data.txt does not exist yet, create the file
        if os.path.exists("{0}\{1}".format(os.getcwd(),"Save_data.txt")) == False:
            with open("Save_data.txt", "w") as file:
                pass
        # Access the file
        file=open("Save_data.txt","r")
        for line in file:
            line_strip=line.strip()
            # For records between <username> and <\username> tags
            if line_strip == "<" + self.userName + ">":
                for line in file:
                    line_strip=line.strip()
                    get_tag_data(self.easyGrid, file, line, line_strip,"easy")
                    get_tag_data(self.medGrid, file, line, line_strip,"medium")
                    get_tag_data(self.hardGrid, file, line, line_strip,"hard")
                    if line_strip == "<\\" + self.userName + ">":
                        break

    
# -----------------------------------------------------------------------------------
# get_tag_data(inGrid, inFile, inLine, inLine_strip, inTag)
# 
# Input:
#       inGrid - grid you want to overwrite data onto
#       inFile - file to read sudoku puzzle data from
#       inLine - current line pointed at in the inFile
#       inLine_strip - string data from line without newline tag
#       inTag - the tag (referring to level of difficulty) for the type of puzzle you want to retrieve
# 
# Purpose:  Parse the file to get the data corresponding to the tag and save it onto the inGrid
#           
# Output:   
#           
# -----------------------------------------------------------------------------------
def get_tag_data(inGrid, inFile, inLine, inLine_strip, inTag):
            # For records between <level> and <\level> tags
            if inLine_strip == ("<" + inTag + ">"):
                for inLine in inFile:
                    inLine_strip=inLine.strip()
                    if inLine_strip == "<\\" + inTag + ">": 
                        break
                    else:
                        line_split=inLine_strip.split()             # Split into separate character elements
                        line_spli_int = list(map(int, line_split))  # Convert into list of int
                        inGrid.append(line_spli_int)