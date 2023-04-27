#!/usr/bin/python
""" Game.py - functions associated with the game """
__author__ = "---"
__copyright__ = "Copyright Dec 2022, Game Final Project, 2022F-T1 AML 1214 - Python Programming 02 (DSMM Group 2)"
__email__ = " student@mylambton.ca"
__credits__= ""


# Import modules
import pygame, sys
import user as user
pygame.init()


# -----------------------------------------------------------------------------------
# Declaration of Global constants here          
# -----------------------------------------------------------------------------------

# GUI related sizes
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
WINDOW_COLOR = (240, 240, 240)
GRID_LEN = 9
SUBGRID_LEN = 3
CELL_WIDTH = WINDOW_WIDTH / GRID_LEN
CELL_VALUE_COLOR = (255, 210, 255)
COLOR_BLACK = (0,0,0)
COLOR_ORANGE = (255,100,10)
SPACE_FROM_LEFT = 18    
SPACE_FROM_TOP = 14
NUM_BORDER_LINES = 10
SUDOKU_NUM_MAX = 9
SUDOKU_NUM_MIN = 1
VALUE_FONT_SIZE = 30
MESSAGE_FONT_SIZE = 20

# Game shortcuts
PLAY_NEW_GAME = pygame.K_n
PLAY_SAVED_GAME = pygame.K_o
LOG_OUT = pygame.K_x
GO_BACK = pygame.K_b
RESET_BOARD = pygame.K_F1
QUIT = pygame.K_F6
ENTER = pygame.K_RETURN
MAIN_MENU = pygame.K_F8

# Game level key shortcuts
EASY = pygame.K_1
MEDIUM = pygame.K_2
HARD = pygame.K_3

# Game level values
LEVEL_EASY = 1
LEVEL_MEDIUM = 2
HARD_LEVEL = 3


# -----------------------------------------------------------------------------------
# Declaration of Global variables here       
# -----------------------------------------------------------------------------------
value_display_font = pygame.font.SysFont("calibri", VALUE_FONT_SIZE,) #bold=True
message_font = pygame.font.SysFont("calibri", MESSAGE_FONT_SIZE)


# -----------------------------------------------------------------------------------
# init_player_data()
#   
# Purpose:  Initialize the current logged in player data
#           
# Output:  currPlayer object so we can access the saved data if any
#           
# -----------------------------------------------------------------------------------
def init_player_data(inPlayer):
    currPlayer   = user.Player(inPlayer)
    currPlayer.get_saved_game()
    return currPlayer



# -----------------------------------------------------------------------------------
# init_puzzle()
#   
# Purpose:  Initialize the default puzzle in the game in case user wants to start over
#           
# Output:  currPuzzle object so we can access different levels in the game
# 
# -----------------------------------------------------------------------------------
def init_puzzle(inFile):
    currPuzzle   = user.Puzzle()
    currPuzzle.get_all_grid_data(inFile)
    return currPuzzle



# -----------------------------------------------------------------------------------
# reset_puzzle()
#   
# Purpose:  Reset the sudoku puzzle 
#           
# Output:  currPuzzle object so we can access different levels in the game
# 
# -----------------------------------------------------------------------------------
def reset_puzzle(inPlayer: user.Player):
    resetPuzzle = init_puzzle("puzzle_1.txt") # Had to create new object from Puzzle because compiler makes gCurrSudokuBoard points to the same object as currPuzzle.<levelGrid> when user plays the game from scratch and not from saved game 
    inPlayer.currPlayGrid = resetPuzzle.get_default_grid(inPlayer.currLevel)
      
      
      
# -----------------------------------------------------------------------------------
# init_sudoku_window()
#   
# Purpose:  Initialize the screen on which to display the sudoku grid
#           
# Output:   
#           
# -----------------------------------------------------------------------------------
def init_sudoku_window(inUserName):
    gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Current player: " + inUserName + "| F1-RESET | F6-QUIT")
    return gameWindow



# -----------------------------------------------------------------------------------
# highlight_selected_cell()
#   
# Purpose:  Highlight currently selected cell block (selection coming from keyboard input or mouse click)
#           
# Output:   
#           
# -----------------------------------------------------------------------------------
def highlight_selected_cell(windowSurface, inRow, inCol):
        lineThickness = 3
        # Top border (draw right to left)
        startPos = (inCol*CELL_WIDTH + CELL_WIDTH, inRow*CELL_WIDTH)
        endPos = (inCol*CELL_WIDTH, inRow*CELL_WIDTH)
        pygame.draw.line(windowSurface, COLOR_ORANGE, startPos, endPos, lineThickness)

        # Left border (draw top to bottom)
        startPos = endPos
        endPos = (inCol*CELL_WIDTH, inRow*CELL_WIDTH + CELL_WIDTH)
        pygame.draw.line(windowSurface, COLOR_ORANGE, startPos, endPos, lineThickness)  

        # Bottom border (draw left to right)
        startPos = endPos
        endPos = (inCol*CELL_WIDTH + CELL_WIDTH, inRow*CELL_WIDTH + CELL_WIDTH)
        pygame.draw.line(windowSurface, COLOR_ORANGE, startPos, endPos, lineThickness)

        # Right border (draw bottom to top)
        startPos = endPos
        endPos = (inCol*CELL_WIDTH + CELL_WIDTH, inRow*CELL_WIDTH)
        pygame.draw.line(windowSurface, COLOR_ORANGE, startPos, endPos, lineThickness)  



# -----------------------------------------------------------------------------------
# create_grid_lines()
#   
# Purpose:  This functions is used draw the elements that make up the grid:
#           1) Border Lines that make up the whole 9x9 grid with 81 cells
#           2) 3x3 subgrids
#           
# Output:   9x9 Grid is displayed
#           
# -----------------------------------------------------------------------------------
def create_grid_lines(windowSurface):
    # Populate the window surface with a thick border for the 3x3 grid and normal thickness for the others
    for i in range(0,NUM_BORDER_LINES):
        # Apply different thickness for border lines that make up the 3x3 subgrids
        if i % 3 == 0 :
            lineThickness = 4 # Subgrid border thickness
        else:
            lineThickness = 1 # Other border lines lines
        # lineThickness = 1
        # Draw the row border lines
        startPos = (0, i * CELL_WIDTH)
        endPos = (WINDOW_WIDTH, i * CELL_WIDTH)
        pygame.draw.line(windowSurface, COLOR_BLACK, startPos, endPos, lineThickness)

        # Draw the column border lines
        startPos = (i * CELL_WIDTH, 0)
        endPos = (i * CELL_WIDTH, WINDOW_HEIGHT)
        pygame.draw.line(windowSurface, COLOR_BLACK, startPos, endPos, lineThickness)     



# -----------------------------------------------------------------------------------
# create_grid_cells()
#   
# Purpose:  This functions is used to draw the square cells that have a value in the 
#           current grid so the 2d grid list can be visualized in the UI as a board
#           
# Output:   No return
#           Cell with values are displayed basically to view the current sudoku board UI
#           
# -----------------------------------------------------------------------------------
def create_grid_cells(windowSurface, inGrid):
    # Populate the surface with colored rect objects for cells with a existing value (non zero)
    for  rowIdx in range (0,GRID_LEN):
        for  colIdx in range (0,GRID_LEN):
            if inGrid[rowIdx][colIdx]!= 0:
                # Highlight those with values
                pygame.draw.rect(windowSurface, CELL_VALUE_COLOR, (colIdx * CELL_WIDTH, rowIdx * CELL_WIDTH, CELL_WIDTH + 1, CELL_WIDTH + 1))
               
                # Blit(overlap) the display text onto the window screen
                displayTxt = value_display_font.render(str(inGrid[rowIdx][colIdx]), 1, COLOR_BLACK)
               
                # This will shift the view of column and row
                windowSurface.blit(displayTxt, (colIdx*CELL_WIDTH + SPACE_FROM_LEFT , rowIdx*CELL_WIDTH + SPACE_FROM_TOP))



# -----------------------------------------------------------------------------------
# display_error_message(windowSurface)
# Input:    windowSurface 
#   
# Purpose:  Display error message when player returns (press enter) but the sudoku is not yet completed
#           
# Output:   errorMessage displayed
#
#           ------
#           Sorry, Sudoku Board is not yet complete.
#           
#           Press ENTER to go back to your board.
#           ------
#
# -----------------------------------------------------------------------------------
def display_error_message(windowSurface):
    isGameContinue = True
    while isGameContinue:   # Keep the display until user presses Enter
        
        windowSurface.fill(WINDOW_COLOR)
        errMessage = message_font.render(str("Sorry, Sudoku Board is not yet complete."), 1, (0, 0, 0))
        windowSurface.blit(errMessage, (10, 5))  
        errMessage = message_font.render(str("Press ENTER to go back to your board."), 1, (0, 0, 0))
        windowSurface.blit(errMessage, (10, 45))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If user presses Enter, go back to the board / current session
                if event.key == ENTER:
                    isGameContinue = False



# -----------------------------------------------------------------------------------
# display_success_message(windowSurface)
# 
# Input:    windowSurface 
#   
# Purpose:  This function displays the success message if sudoku was completed
#           
# Output:   successMessage are displayed
#
#           ------
#           Congratulations!
#           You have successfully completed the game.
#
#           Press ENTER to go back to your board.
#           ------
#
# -----------------------------------------------------------------------------------
def display_success_message(windowSurface):
    isGameContinue = True

    while isGameContinue:   # Keep the display until user presses Enter
        
        windowSurface.fill(WINDOW_COLOR)
        successMessage = message_font.render(str("Congratulations!"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 5))  
        successMessage = message_font.render(str("You have successfully completed the game."), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 25))  
        successMessage = message_font.render(str("Press ENTER to go back to your board."), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 65))  
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               # If user presses Enter, go back to the board / current session
                if event.key == ENTER:
                    isGameContinue = False



# -----------------------------------------------------------------------------------
# display_save_message(windowSurface, inPlayer :sudoku_data.Player)
# 
# Input:    windowSurface
#           inPlayer :sudoku_data.Player
#   
# Purpose:  Displays the save options if user closes current session / grid
#           
# Output:   saving options are displayed
#
#           ------
#           Do you want to save this level's current session?
#           Y - Yes, save this session.
#           N - No, don't save this session.       
#           ------
#
# -----------------------------------------------------------------------------------
def display_save_message(windowSurface, inPlayer :user.Player):
    isGameContinue = True

    while isGameContinue:   # Keep the display until user chooses an option
        
        windowSurface.fill(WINDOW_COLOR)
        displayMessage  = message_font.render(str("Do you want to save this level's current session?"), 1, (0, 0, 0))
        windowSurface.blit(displayMessage , (10, 5))  
        displayMessage  = message_font.render(str("Y - Yes, save this session."), 1, (0, 0, 0))
        windowSurface.blit(displayMessage , (10, 25))  
        displayMessage  = message_font.render(str("N - No, don't save this session."), 1, (0, 0, 0))
        windowSurface.blit(displayMessage , (10, 45))  
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If user enters Y, save current session
                if event.key == pygame.K_y:
                    inPlayer.save_game()
                    isGameContinue = False
                # If user enters N, end the loop
                elif event.key == pygame.K_n:
                    isGameContinue = False



# -----------------------------------------------------------------------------------
# display_main_menu(windowSurface, inPlayer :sudoku_data.Player)
# 
# Input:    windowSurface
#           inPlayer :sudoku_data.Player
#   
# Purpose:  This function displays the MAIN MENU
#           
# Output:   isLoggedIn = True if user has chosen to play game and False is user chooses to log out
#           
#           main menu is displayed:
#           ------
#           N - PLAY NEW GAME
#           O - PLAY PREVIOUSLY SAVED GAME
#           X - LOG OUT      
#           ------
#
# -----------------------------------------------------------------------------------
def display_main_menu(windowSurface, inPlayer :user.Player):
    isOptionSelected = False
    isLoggedIn = True

    while not(isOptionSelected):    # Keep displaying the main menu until user chooses an option
        
        windowSurface.fill(WINDOW_COLOR)
        successMessage = message_font.render(str("N - PLAY NEW GAME"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 5))  
        successMessage = message_font.render(str("O - PLAY PREVIOUSLY SAVED GAME"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 25))  
        successMessage = message_font.render(str("X - LOG OUT"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 45))    
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                
                # If user chooses to play a New Game (N)
                if event.key == PLAY_NEW_GAME: 
                    inPlayer.isNewGame = True
                    # Go to level selection menu
                    if select_level(windowSurface, inPlayer) == True:
                        isOptionSelected =  True
                # If user chooses to play a Saved Game (O)
                if event.key == PLAY_SAVED_GAME: 
                    inPlayer.isNewGame = False
                    # Go to level selection menu
                    if select_level(windowSurface, inPlayer) == True:
                        isOptionSelected =  True 
                # If user chooses to Log Out (X)
                if event.key == LOG_OUT: 
                    isLoggedIn = False
                    isOptionSelected =  True

    return isLoggedIn



# -----------------------------------------------------------------------------------
# select_level(windowSurface, inPlayer :sudoku_data.Player)
# 
# Input:    windowSurface
#           inPlayer :sudoku_data.Player
#   
# Purpose:  This function displays the menu for game difficulty level selection
#           
# Output:   isLevelSelected = True if user has chosen a level to play and False if
#           otherwise and user chooses to go back to main menu
#           
#           level selection menu is displayed:
#           ------
#           1 - EASY
#           2 - MEDIUM
#           3 - HARD
#           B - GO BACK TO MAIN MENU
#           
#           Sorry, there is no saved game for <level>.   
#           ------
#
# -----------------------------------------------------------------------------------
def select_level(windowSurface, inPlayer :user.Player):
    isOptionSelected = False
    isLevelSelected = True
    withSavedGame = True
    
    # Keep displaying the level selection menu until:
    #   - user chooses to return to previous menu
    #   - user selects a level with valid data (for saved game option)
    while not(isOptionSelected) or not(withSavedGame):
        
        windowSurface.fill(WINDOW_COLOR)
        successMessage = message_font.render(str("1 - EASY"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 5))  
        successMessage = message_font.render(str("2 - MEDIUM"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 25))  
        successMessage = message_font.render(str("3 - HARD"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 45))  
        successMessage = message_font.render(str("B - GO BACK TO MAIN MENU"), 1, (0, 0, 0))
        windowSurface.blit(successMessage, (10, 65)) 
        windowSurface.blit(message_font.render(str(""), 1, (0, 0, 0)), (10, 105))
        # If user selects a level with no saved data, display error message
        if withSavedGame == False:
            windowSurface.blit(errorMessage, (10, 105))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If user chooses Easy (1)
                if event.key == EASY: 
                    init_game_session(LEVEL_EASY, inPlayer)     # Initialize game for easy level
                    isOptionSelected = True
                    withSavedGame = True
                    # If there is no saved game (i,e. grid is blank), define error message and go back to level selection menu
                    if inPlayer.currPlayGrid == []:
                        withSavedGame = False
                        errorMessage = message_font.render(str("Sorry, there is no saved game for Easy."), 1, (255, 0, 0))
                # If user chooses Medium (2)
                if event.key == MEDIUM: 
                    init_game_session(LEVEL_MEDIUM, inPlayer)     # Initialize game for medium level
                    isOptionSelected = True
                    withSavedGame = True
                    # If there is no saved game (i,e. grid is blank), define error message and go back to level selection menu
                    if inPlayer.currPlayGrid == []:
                        withSavedGame = False
                        errorMessage = message_font.render(str("Sorry, there is no saved game for Medium."), 1, (255, 0, 0))
                # If user chooses Hard (3)
                if event.key == HARD: 
                    init_game_session(HARD_LEVEL, inPlayer)     # Initialize game for hard level
                    isOptionSelected = True
                    withSavedGame = True 
                    # If there is no saved game (i,e. grid is blank), define error message and go back to level selection menu
                    if inPlayer.currPlayGrid == []:
                        withSavedGame = False
                        errorMessage = message_font.render(str("Sorry, there is no saved game for Hard."), 1, (255, 0, 0))
                # If user chooses to Go Back to Main Menu (B), exit the loop
                if event.key == GO_BACK: 
                    isLevelSelected = False
                    isOptionSelected = True
                    withSavedGame = True

    return isLevelSelected



# -----------------------------------------------------------------------------------
# init_game_session(inLevel :int, inPlayer :sudoku_data.Player)
# 
# Input:    inLevel :int
#           inPlayer :sudoku_data.Player
#   
# Purpose:  This function initializes the game level session to be played by assigning the corresponding 
#           puzzle to be played in the current game session
#           
# Output:   None
#           
# -----------------------------------------------------------------------------------
def init_game_session(inLevel :int, inPlayer :user.Player):
    
    # Initialize the default puzzle object in the game with specific input file
    defaultPuzzle = init_puzzle("puzzle_1.txt")

    # Level selected by user
    inPlayer.currLevel = inLevel
    
    # If it is a new game, get a default grid for the chosen level
    if inPlayer.isNewGame: 
        inPlayer.currPlayGrid = defaultPuzzle.get_default_grid(inLevel)
    # If user chooses to continue a saved game, get the grid from the database
    else: 
        inPlayer.currPlayGrid = inPlayer.get_saved_grid(inLevel)



# -----------------------------------------------------------------------------------
# check_sudoku_complete(inGrid, rowIdx: int, colIdx: int)
#  
# Input:    inGrid
#           rowIdx: int
#           colIdx: int
#   
# Purpose:  Verify that the board is complete and correct (no repetitions as per sudoku rules)
#           But since we already dont allow user to input if there are any repetitions then simply 
#           check that no cell is empty(value = zero)
#           
# Output:   - return True if the sudoku was completed successfully 
#           - return False if the sudoko board wasnt completed 
#           
# -----------------------------------------------------------------------------------
def check_sudoku_complete(inGrid, rowIdx: int, colIdx: int):
    for  rowIdx in range (0,GRID_LEN):
        for  colIdx in range (0,GRID_LEN):
            if inGrid[rowIdx][colIdx] == 0:
                return False
    return True



# -----------------------------------------------------------------------------------
# check_valid_input(inGrid: list, inRow: int, inCol: int, userInVal)
# 
# Input:inGrid: list - current board 
#       inRow: int - current row where user typed in a value
#       inCol: int - current column where user typed in a value
#       userInVal - User inpput value
# 
# Purpose:  Function to check validity of user input
#           where Valid values should satisfy all 4 below:
#           1) range is within 1 to 9
#           2) number not yet existing in the same column
#           3) number not yet existing in the same row 
#           4) number not yet existing in the 3x3 subgrid group
# 
# Output:   Return True when value is valid
#           Return False when value is not valid
# -----------------------------------------------------------------------------------
def check_valid_input(inGrid: list, inRow: int, inCol: int, userInVal):
    global GRID_LEN  
    global SUBGRID_LEN
    nSubColStartIdx = 0
    nSubRowStartIdx = 0
    
    # Browse through each column and row and check if the input value already exists in the same column and row in the whole grid
    for idx in range(0,GRID_LEN):
        if (userInVal == inGrid[inRow][idx]) or (userInVal == inGrid[idx][inCol]):
            return False

    # Use // to divide the col and row with integral result (discard remainder) in order to get the position of subGrid
    # where the selected cell belongs
    nSubRowStartIdx = (inRow//SUBGRID_LEN)*SUBGRID_LEN
    nSubRowStopIdx =  nSubRowStartIdx + SUBGRID_LEN
    nSubColStartIdx = (inCol//SUBGRID_LEN)*SUBGRID_LEN
    nSubColStopIdx = nSubColStartIdx + SUBGRID_LEN

    # Check if the value already exists in the other cells within the current subgrid (3x3) group where the selection belongs
    for rowIdx in range (nSubRowStartIdx, nSubRowStopIdx):
        for colIdx in range(nSubColStartIdx, nSubColStopIdx):
            if inGrid[rowIdx][colIdx] == userInVal:
                return False
    return True



# -----------------------------------------------------------------------------------
# within_grid(inLocation) 
# 
# Input:    inLocation - the potential row or column the user want to go to when a key is pressed
#   
# Purpose:  This helps check when the new inLocation would be outside of the grid or not
#           hence to help restrict the user to only make selections within the existing cells
#           in the sudoku grid are in displayed in the window screen
#           
# Output:   return True if row/column position is within the grid area(0,1,2,3,4,5,6,7,8)
#           return False if row/column position is outside of the grid area
#           
# -----------------------------------------------------------------------------------
def within_grid(inLocation):
    if inLocation in range (0,GRID_LEN):
        return True
    else:
        return False



# -----------------------------------------------------------------------------------
# start_game(inPlayerUserName)
# 
# Input:    inPlayerUserName :sudoku_data.Player.userName
#   
# Purpose:  Starts to execute the initialization and game, called by main function
#           
# Output:   Main Menu is at first displayed
#           
# -----------------------------------------------------------------------------------
def start_game(inPlayerUserName :user.Player):
    nRow = 0
    nCol = 0

    isUserLoggedIn = True   
    isGameRunning = True  
    sUserInputVal = -1

    # Initialize the player data
    currPlayer = init_player_data(inPlayerUserName) 

    # Initialize pygame sudoku window 
    windowSurface = init_sudoku_window(currPlayer.userName)

    while isUserLoggedIn:   # Loop while user has not yet chosen to log out (isUserLoggedIn = False)
        
        # Go to main menu first so user can choose what he/she wants to do
        isUserLoggedIn = display_main_menu(windowSurface, currPlayer)
        
        if isUserLoggedIn: isGameRunning = True
           
        while isGameRunning:    # Loop while current session is active
            windowSurface.fill(WINDOW_COLOR)
            for event in pygame.event.get():
                
                # If player clicks the Quit icon (X)
                if event.type == pygame.QUIT:
                    display_save_message(windowSurface,currPlayer)  # Prompt save options
                    isGameRunning = False                           # Exit the loop / current session and go back to main menu
                
                # If player uses mouse cursor to select a cell
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tMousClick = pygame.mouse.get_pos() # Get the position of the cell cell where mouse click was done
                    nCol = tMousClick[0]//CELL_WIDTH    # Divide with cell width and remove remainder to get only the row number
                    nRow = tMousClick[1]//CELL_WIDTH    # Divide with cell width and remove reaminder to get only the column number
                
                # If player uses keyboard to navigate the grid
                if event.type == pygame.KEYDOWN:
                    
                    # F6 is shortcut for Quit 
                    if event.key == pygame.K_F6:
                        display_save_message(windowSurface,currPlayer)  # Prompt save options
                        isGameRunning = False                           # Exit the loop / current session and go back to main menu
                        
                    # Left, Right, Up, Down keys
                    if event.key == pygame.K_LEFT and within_grid(nCol-1):
                        nCol-= 1
                    if event.key == pygame.K_RIGHT and within_grid(nCol+1):
                        nCol+= 1
                    if event.key == pygame.K_UP and within_grid(nRow-1):
                        nRow-= 1
                    if event.key == pygame.K_DOWN and within_grid(nRow+1):
                        nRow+= 1
                        
                    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 keys                     
                    if event.key == pygame.K_0:
                        sUserInputVal = 0
                    if event.key == pygame.K_1:
                        sUserInputVal = 1
                    if event.key == pygame.K_2:
                        sUserInputVal = 2   
                    if event.key == pygame.K_3:
                        sUserInputVal = 3
                    if event.key == pygame.K_4:
                        sUserInputVal = 4
                    if event.key == pygame.K_5:
                        sUserInputVal = 5
                    if event.key == pygame.K_6:
                        sUserInputVal = 6
                    if event.key == pygame.K_7:
                        sUserInputVal = 7
                    if event.key == pygame.K_8:
                        sUserInputVal = 8
                    if event.key == pygame.K_9:
                        sUserInputVal = 9
                    
                    # K_RETURN is same as user pressing Enter                        
                    if event.key == ENTER: 
                        # If user has pressed enter to say he/she is done, verify if the current sudoku board is complete and correct 
                        if check_sudoku_complete(currPlayer.currPlayGrid , 0, 0):
                            display_success_message(windowSurface)  # If the board is correct, display success message
                        else: 
                            display_error_message(windowSurface)    # If the board is incorrect, display error message

                    # Reset the board when user presses F1
                    if event.key == RESET_BOARD:
                        resetPuzzle = init_puzzle("puzzle_1.txt")   # Had to create new object from Puzzle because compiler makes gCurrSudokuBoard point to the same object as currPuzzle.<levelGrid> when user plays the game from scratch and not from saved game 
                        currPlayer.currPlayGrid = resetPuzzle.get_default_grid(currPlayer.currLevel)  # Get default grid

            # Allow to display input onto the board if input is valid
            if sUserInputVal != -1: 
                # Update the cell with valid input value from player
                if check_valid_input(currPlayer.currPlayGrid , int(nRow), int(nCol), sUserInputVal)== True:
                    currPlayer.currPlayGrid[int(nRow)][int(nCol)]= sUserInputVal
                # If the the input is invalid, allow player to clear the cell
                elif sUserInputVal == 0:
                    currPlayer.currPlayGrid[int(nRow)][int(nCol)]= 0  
                else:
                    pass
                sUserInputVal = -1   
            
            create_grid_cells(windowSurface, currPlayer.currPlayGrid)
            create_grid_lines(windowSurface) 

            # If cell is currently selected then show it by highlighting the edges
            highlight_selected_cell(windowSurface, nRow, nCol)   

            pygame.display.update() 
        
        # Reinitialize / refresh player data after closing the current session
        currPlayer = init_player_data(inPlayerUserName)
            
    # Close window when user chooses to log out
    pygame.quit()  
    sys.exit()
