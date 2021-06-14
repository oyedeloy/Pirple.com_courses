
from termcolor import colored, cprint


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

CurrentField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]
draw_board(CurrentField)