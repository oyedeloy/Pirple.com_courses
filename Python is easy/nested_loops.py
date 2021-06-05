#Tic-Tac-Toe Field

#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4


for row in range(5): #                    #Rows will take the value 0, 1, 2, 3, 4, 5
    if row%2 == 0:
        #print(" | | ")                   #Instead of this print statement, we can make it mo rubust by
               #12345                     #printing either a vertical line or a space.
                                          #There are 5 columns to be printed, even numbers are vertical
                                          #lines, while odd numbers are space.
        for column in range(1, 6):
            if column%2 == 1:
                if column != 5:
                    print(" ",end="")         #the "end" keyword prevents it from printing on a new line
                else:
                    print(" ",)  
            else:
                print("|",end="")  
    else:
        print("-----")      
        
print("\n")        
        
for row in range(5):
    if row%2 == 0:
        for column in range(1, 6):
            if column%2 == 1:
                if column!=5:
                    print(" ",end="")
                else:
                    print(" ",)
            else:
                print("|",end="") 
    else:
        print("-----")                 
                                     
    
        
    