
#Tic-Tac-Toe Field

#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4

def tic_tak(rows, columns): 
    if rows != 3 or columns !=3: 
        print("\n----- YOUR INPUT IS OUT OF RANGE, BOARD CANNOT BE PRINTED -----")
        output = False
        print(output)
              
    else:
        print("\n\n----- PRINTING BOARD -----")
        print(" ")
        
        for row in range(rows+2): #                       
                       
                                                       #Rows will take the value 0, 1, 2, 3, 4, 5
            if row%2 == 0:
                #print(" | | ")                        #Instead of this print statement, we can make it more rubust by
                       #12345                          #printing either a vertical line or a space.
                                                       
                                                       
                for column in range(1, columns+3):     #There are 5 colums to be printed, even numbers are vertical
                    if column%2 == 1:                  #lines, while odd numbers are space.
                        if column != 5:
                            print(" ",end="")          #the "end" keyword prevents it from printing on a new line
                        else:
                            print(" ")  
                    else:
                        print("|",end="")  
            else:
                print("-----")
    if rows == 3 and columns ==3:
        output = True
        print("\n----- PRINTING OUTPUT-----")
        print(output)
        
         
tic_tak(3, 3)                       
    