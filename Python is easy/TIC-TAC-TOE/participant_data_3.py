#getting stats from the data
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
print(Age)

Oldest = 0
youngest = 100
most_occuring_age = 0
counter = 0
for age_temp in Age:
    if age_temp > Oldest:
        Oldest = age_temp
    if age_temp < youngest:
        youngest = age_temp
    if Age[age_temp] > counter:
        counter = Age[age_temp]
        most_occuring_age = age_temp
        
    
        
        
print(Oldest)
print(youngest)
print(most_occuring_age)
        
    



input_file.close()
