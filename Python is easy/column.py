player = 1

CurrentField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]
#draw_board(CurrentField)

for index, column in enumerate(CurrentField):
    print(index, column)                    
         
def row_counter():
    for column in range(len(CurrentField)):
        for row in range(6):
            if CurrentField[column][row] == " ":
                move_row = row
            #print(row,end="")
            return row
      
        
        