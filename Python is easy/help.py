


""" List Assignment """

#Defining an empty list

mUniqueList = []
print(mUniqueList)

# function to add elements to the previously defined list
def add_list(Number):
    output = mUniqueList.append(Number)
    return output

# The list is now complete with 4 numerical elements

Add_1 = add_list(10)
Add_2 = add_list(25)
Add_3 = add_list(69)
Add_4 = add_list(78)
print(mUniqueList)

# """ Now that our List (mUniqueList) has certain elements, Let us try to add another element to it
# and check if the value that we are trying to add to mUniqueList is already present in it or no.
# The following set of code intends to add a new number to the list. If the number is already present,
# it should return "The value is already present in the list". Or else it has to go ahead and use the
# (add_list) function defined above to append the list. """

Add_New = 60
def Check_List(Number):
    if Add_New in mUniqueList:
        output = "The value is already present in the list"
    else:
        output = add_list(Add_New)
        return output

Updated_List = Check_List(Add_New)
print(Updated_List)

for c in range(5):
    print(c)
    
    
for row in range(5):
       if row&2 == 0:
           for column in range(1, 6):
               if column%2 == 1:
                   if column!=5:
                       print(" ",end="")
                   else:
                       print(" ")
               else:
                    print("|",end="") 
       else:
            print("-----")
            





