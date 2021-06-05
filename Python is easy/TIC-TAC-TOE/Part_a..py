#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4



def draw_board(field):
    for row in range(5):
        if row%2 == 0:
            practical_row = int(row/2)
            for column in range(5): #0,1,2,3,4
                                    #0,.,1,.,2 matching playing field to current field
                                    #corresponding to coulmns divided by 2
                
                if column%2 == 0: #This occurs for columns 0, 2, 4
                    practical_column = int(column/2) #0, 1, 2 This will enable us to map to the indexes in the current field
                    if column!=4:
                        print(field[practical_column][practical_row],end="")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|",end="") 
        else:
            print("-----")


#draw_board()

#There are 2 players and we need to check whose turn it is.
player = 1
#The moves made by each player will be saved in a list
#CurrentField = [element1, element2, element2] each element corresponds to columns 1, 2, and 3 respectively
#Each columns have three field, that means we need to store 3 values for each element in the list.
#one way to do this is to create another list in the list as shown below.
CurrentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_board(CurrentField)
while True:
    print("Players turn: ", player)
    move_row  = int(input("Please enter a row\n\n"))
    move_colu  = int(input("Please enter a column\n\n"))
    if player == 1:
        #make move for player 1
        if CurrentField[move_colu][move_row] == " ":
            CurrentField[move_colu][move_row] = "x"
            #after player 1 moves, its player 2 turn to move
            player = 2
    else:
        #make move for player 2
        if CurrentField[move_colu][move_row] == " ":
            CurrentField[move_colu][move_row] = "o"
        #after player 2 moves, its player 1 turn to move
            player = 1
    draw_board(CurrentField)
#We need to map the current field to the tic tac toe field     
        
    


