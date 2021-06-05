#Finding index/position of a particular item in a list

participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
position = 0
for name in participants:
    if name == "Joe":
        break    #After breaking, skip to the end of the loop without executing the rest of the script.
    position += 1
print(position)

#Another way to do it

for CurrentIndex in range(len(participants)):
    if participants[CurrentIndex] == "Joe":
        break
print(CurrentIndex)

for number in range(11):
        if number%3 == 0:
            print(number)
            print(str(number) + " is divisible by 3")
            continue #When you say continue, it skips the rest part of the loop below and goes back to the top
        print(number)
        print(str(number) + " is not divisible by 3")
        
        
#Let's try and use ENUMERATION


for name in (participants):
    print(f"name_is {name}")
    
print("\n\nFinding index using enumeration")

for index_no, name in enumerate (participants):
    print(f"Index {index_no} is {name}")
    
    
    
        
    