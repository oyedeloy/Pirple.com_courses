myUniqueList = []
my_leftovers = []

def add_to_list(Number):
    global myUniqueList
    if Number not in myUniqueList:
        output = True
        print(output)
    elif Number in myUniqueList:
        output = False
        print(output)
    if output == True:
        myUniqueList.append(Number)
        print (myUniqueList)
    elif output == False:
        my_leftovers.append(Number)
        print(my_leftovers)
        
       
    
add_to_list(2)
add_to_list(35)
add_to_list(13)
add_to_list(2)
add_to_list(22)
add_to_list(33)
add_to_list(18)
add_to_list(6.5)
add_to_list("helloworld")
add_to_list(22)
add_to_list(33)
add_to_list(18)
add_to_list(6.5)
add_to_list("helloworld")



print(myUniqueList)
print(my_leftovers)

#myUniqueList.append(4)

    
    