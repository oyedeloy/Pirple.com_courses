
from pprint import pprint


#shoeColor = {ShoeSize:Quantity}
Blackshoes = {42:2, 41:3, 40:40, 39:1, 38:0}
print(Blackshoes)
while (True): #Infinite loop, equivalant of True = True
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if Blackshoes[purchaseSize] < 0:
        break        
    if Blackshoes[purchaseSize] > 0:        
        Blackshoes[purchaseSize] -= 1
    else:
        print("No longer in stock")
    print(Blackshoes)
    
    

