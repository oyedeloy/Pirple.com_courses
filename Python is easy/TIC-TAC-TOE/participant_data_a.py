Participant_number = 2
Participant_data = []
Registered_participant = 0
output_file = open("participant_data.txt", "w") #Creating a file to write the output of the participant data
while(Registered_participant < Participant_number): #We want participants to be able to register if number < registered
    temp_part_data = []   # participant data will be stored in this list [Name, country of origin, age]
    Name = input("Please enter your name: ")
    temp_part_data.append(Name)
    Country = input("Please enter your country of origin: " )
    temp_part_data.append(Country)
    age = int(input("Please enter you age: "))
    temp_part_data.append(age)
    print(temp_part_data)
    #Next is to save temp_data into participant data
    Participant_data.append(temp_part_data)
    Registered_participant += 1
    print(Participant_data)
    
for participant in Participant_data:
    for data in participant:
        output_file.write(str(data)) #str(data) because we can only write strings to a file
        output_file.write(" ")
    output_file.write("\n")
        
        
        
    
        
    
output_file.close()
    
    
    