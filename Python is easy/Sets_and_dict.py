Sets = {"Lagos", "Ibadan", "Abuja", "Lagos"}
print(Sets) #repeated elements will be removed when you print a set
            #Sets are not ordered
            
if "Lagos" in Sets:
    print("yes")
    
CountryList = []
for x in range(5):
    Country = input("Enter your country: ")
    CountryList.append(Country)
    
CountrySet = set(CountryList) #The set keyword turns the List into a set
print(CountryList)
print(CountrySet)



#DICTIONARIES
Dictionary = {"Key":"Value", "Key2":"Value2", "Key3":"Value3"} #We access the elements by keys and not by index
CountryDictionary = {}
for country in CountryList:
    if country in CountryDictionary:
        CountryDictionary[country] += 1 #Counting the number of times each country appears in the list
    else:
        CountryDictionary[country] = 1
print(CountryDictionary)