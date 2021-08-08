"""
This code generates random make, models, engine capacity, and prices of cars and then tabulates them.
"""

from random import choice
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

def create_cars(num_cars): #This function creates a specified number of cars and a specified number of makes randomly
    Cars = list()
    
    for car_index in range(1, num_cars+1):
        
        Car = dict()
    
    #THE CHOICE LIBRARY        
    #Generate random car make by selecting from a list of makes using the choice library
    
    #CHOICE OF CAR VENDOR
        Car["vendor"] = choice(["Ford", "Chevy", "Dodge", "Toyota", "Honda"])
        if Car["vendor"] == "Ford":
            Car["Make"] = choice(["Escape", "Edge", "Exlorer"])
            Car["Engine Capacity"] = choice(["2.5 Litres", "3.0 Litres", "3.5 Litres"])
            Car["Price"] = choice([10000, 12000, 15000])
        elif Car["vendor"] == "Chevy":
            Car["Make"] = choice(["Trail Blazer", "Yukon", "Express"])
            Car["Engine Capacity"] = choice(["3.5 Litres", "4.0 Litres", "4.7 Litres"])
            Car["Price"] = choice([11000, 13000, 14000])
        elif Car["vendor"] == "Dodge":
            Car["Make"] = choice(["Ram", "Caliber", "Durango"])
            Car["Engine Capacity"] = choice(["2.7 Litres", "3.7 Litres", "4.2 Litres"])
            Car["Price"] = choice([9000, 12000, 17000])
        elif Car["vendor"] == "Toyota":
            Car["Make"] = choice(["Camry", "Corolla", "Rav4"])
            Car["Engine Capacity"] = choice(["2.5 Litres", "3.0 Litres", "3.5 Litres"])
            Car["Price"] = choice([14000, 15000, 16000])
        elif Car["vendor"] == "Honda":
            Car["Make"] = choice(["Civic", "Accord", "Pilot"])
            Car["Engine Capacity"] = choice(["2.0 Litres", "2.5 Litres", "3.3 Litres"])
            Car["Price"] = choice([10000, 12000, 15000])
            
                
            #Add Car to the list of cars
            
        Cars.append(Car)
    return Cars
if __name__  == '__main__':
    Created_cars =create_cars(4)

# PRINTING USING PPRINT TO PRINT DEVICES IN A RAW FORMAT
print("\n----- CARS AS A LIST OF DICTIONARY---------------")
pprint(Created_cars)

# PRINTING USING FOR LOOP ENUMERATE

print("\n----- PRINT USING FOR LOOP AND ENUMERATE---------------\n")
for index_no, car in enumerate(Created_cars):
    print("Car_" + str(index_no+1), car)
    
# PRINTING SORTED TABLE OF CARS USING THE TABULATE MODULE
print("\n----- SORTED DEVICES IN TABULAR FORMAT -------------\n")
print(tabulate(sorted(Created_cars, key=itemgetter("Make", "Engine Capacity", "Price")), headers="keys"))
#print(tabulate(sorted(devices, key=itemgetter("vendor")), headers="keys"))


    


