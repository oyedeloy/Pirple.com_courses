
import sys
from termcolor import colored, cprint
# | | | | | |   0
# ------------- 1
# | | | | | |   2
#-------------  3
# | | | | | |   4
#-------------  5
# | | | | | |   6
#-------------  7
# | | | | | |   8
#-------------  9
# | | | | | |   10
#01234567891011

def draw_board(field):
    for row in range(11):
        if row%2 == 0:
            practical_row = int(row/2)
            for column in range(13): #0,1,2,3,4,5,6,7,8,9,10.11
                                    #0,.,1,.,2 matching playing field to current field
                                    #corresponding to coulmns divided by 2
                
                if column%2 == 0: #This occurs for columns 0, 2, 4
                    practical_column = int(column/2) #0, 1, 2 This will enable us to map to the indexes in the current field
                    if column!=12:
                        print(field[practical_column][practical_row],end="")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|",end="") 
        else:
            print("-------------")

#draw_board()

#Defining winning fomular


    

#Transposing into list data structure

#There are 2 players and we need to check whose turn it is.
player = 1


#when a palyer drops a piece ina column for the first time, it should go to row 1

#The moves made by each player will be saved in a list
#CurrentField = [element1, element2, element3, element4, element5, element6, element7] each element corresponds to columns 1, 2, and 3 respectively
#Each columns have six field, that means we need to store 6 values for each element in the list.
#one way to do this is to create another list in the list as shown below.
CurrentField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]
draw_board(CurrentField)

row_dict ={0:5, 1:5, 2:5, 3:5, 4:5, 5:5, 6:5} #each element in this dict correspond to the number of pieces in each column
                                              #At the start of the game, each column has 0 pieces
                                              #Row started from 5 to make sure that the board is printed from bottom up
                                              #This dictionary is used to feed values into the move row variable whenever a layer specifies a column




            
        

Game_over = False         
while not Game_over:
    
    print("Players turn: ", player)
    move_column  = int(input("Please enter a column\n\n"))
    move_row = row_dict[move_column]
    row_dict[move_column]-=1   #The row decreases whenever a player drops a piece into the column.    
              
    if player == 1:
        
        #make move for player 1
        if CurrentField[move_column][move_row] == " ":
            CurrentField[move_column][move_row] = "x"
            
        #Check for horizontal win
        for c in range(4):
            for r in range(6):
                  if CurrentField[c][r] == CurrentField[move_column][move_row] and CurrentField[c+1][r] == CurrentField[move_column][move_row] and CurrentField[c+2][r] == CurrentField[move_column][move_row] and CurrentField[c+3][r] == CurrentField[move_column][move_row]:
                    player = 1
                    Game_over = True
                    print(f"player {player} " + "wins Congrats " + "\n")
        #Check for vertical win
        
        for c in range(7):
            for r in range(3):
                  if CurrentField[c][r] == CurrentField[move_column][move_row] and CurrentField[c][r+1] == CurrentField[move_column][move_row] and CurrentField[c][r+2] == CurrentField[move_column][move_row] and CurrentField[c][r+3] == CurrentField[move_column][move_row]:
                   
                    player = 1
                    Game_over = True
                    print(f"player {player} " + "wins Congrats " + "\n")   
                    
        #Check for negative diagonal win
        for c in range(4):
            for r in range(3):
                  if CurrentField[c][r] == CurrentField[move_column][move_row] and CurrentField[c+1][r+1] == CurrentField[move_column][move_row] and CurrentField[c+2][r+2] == CurrentField[move_column][move_row] and CurrentField[c+3][r+3] == CurrentField[move_column][move_row]:
                   
                    player = 1
                    Game_over = True
                    print(f"player {player} " + "wins Congrats " + "\n")         
        
            
        #after player 1 moves, its player 2 turn to move
        player = 2    
            
        
        
    else:
        #make move for player 2
        if CurrentField[move_column][move_row] == " ":
            CurrentField[move_column][move_row] = "o"
        
        #Check for horizontal win
        for c in range(4):
            for r in range(6):
                  if CurrentField[c][r] == CurrentField[move_column][move_row] and CurrentField[c+1][r] == CurrentField[move_column][move_row] and CurrentField[c+2][r] == CurrentField[move_column][move_row] and CurrentField[c+3][r] == CurrentField[move_column][move_row]:
                    player = 2
                    Game_over = True
                    print(f"player {player} " + "wins Congrats " + "\n")
        #Check for vertical win
        
        for c in range(7):
            for r in range(3):
                  if CurrentField[c][r] == CurrentField[move_column][move_row] and CurrentField[c][r+1] == CurrentField[move_column][move_row] and CurrentField[c][r+2] == CurrentField[move_column][move_row] and CurrentField[c][r+3] == CurrentField[move_column][move_row]:
                    player = 2
                    Game_over = True
                    print(f"player {player} " + "wins Congrats " + "\n")
        
                
        #after player 2 moves, its player 1 turn to move
            player = 1
        
    draw_board(CurrentField)
    
#We need to map the current field to the tic tac toe field  
   


