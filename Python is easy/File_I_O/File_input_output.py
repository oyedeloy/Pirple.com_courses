#format File = open("Filename", r(read), w(write), a(append))
                                #r+ to read and write at the same time
#it is very imortant to close the file after using it
#File.close()

Cities = ["Lagos", "Ibadan", "Kano", "Enugu","Akure"]
city_file = open("cityFile", "w") #If this file isn't there already, it will create it automatically and
                                  #overite it if it already exist
for city in Cities:
    city_file.write(city + "\n")
city_file.close()

city_file = open("cityFile", "r")
#print(city_file.read()) #The read method is not recommended if you have a huge amount of data.
#Let's instead, read the file line-by-line

#READING THE FILE LINE BY LINE USING FOR LOOP
#for  line in city_file:
    #print(line, end="")
    
#WE CAN RED INDIVIDUAL LINES
Firstline = city_file.readline() #When you use readline, the cusor moves to the next line after reading a line
print(Firstline)
Secondline = city_file.readline()
print(Secondline)
city_file.close()

#APPENDING
Finalspot = "Ilesa"
city_file = open("cityFile", "a") #That means we are witting at the very end
city_file.write(Finalspot)
city_file.close



