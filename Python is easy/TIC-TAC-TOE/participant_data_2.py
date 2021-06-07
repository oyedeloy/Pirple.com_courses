

#Reading from the file
input_file = open ("participant_data.txt", "r")
input_list = [] #Stores all the data we want to read
for line in input_file:
    temp_data = line.strip("\n").split()
    print(temp_data)
    input_list.append(temp_data)
    print(input_list)
    




Age = {}
for part in input_list:
    temp_age = int(part[-1])
    if temp_age in Age:
        Age[temp_age] +=1
    else:
        Age[temp_age] = 1

input_file.close()



    
    
    