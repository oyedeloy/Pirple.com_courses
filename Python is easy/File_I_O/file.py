#Finalspot = "Ilorin"
#city_file = open("cityFile", "a") #That means we are witting at the very end
#city_file.write(Finalspot + "\n")
#city_file.close

#This method automatically closes the file for you and you don't have to use the close keyword

with open("cityfile", "r") as city_file:
    for line in city_file:
        print(line, end="")