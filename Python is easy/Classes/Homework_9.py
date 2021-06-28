#CREATING THE "VEHICLE" CLASS

class Vehicle:
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        
   
   #GETTERS
    def get_make(self): #The follwing methods allow us to get values of the make, model, year, and weight of vehicles.
       return self.Make
    def get_model(self):
        return self.Model
    def get_year(self):
        return self.Year
    def get_weight(self):
        return self.Weight 
    def get_need_maintenance(self):        
        if self.NeedsMaintenance == True:
            print ("it requires maintenance")
        else:
            print("it does not require maintenance")
        #return self.NeedsMaintenance
            
    def trip_since_maintenance(self):
        return self.TripsSinceMaintenance
    
   
   
   #SETTERS
    def set_make(self,xmake): #The follwing methods allow us to set the make, model, year, and weight of vehicles.
        self.Make = xmake
    def set_model(self,xmodel):
        self.Model = xmodel
    def set_year(self,xyear):
        self.Year = xyear
    def set_weight(self,xweight):
        self.Weight = xweight  
    def Repair(self):         #This method allows us to set the trip maintenance to zero and needsmaintenance to false.
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False 

#CREATING THE "CARS" CLASS       
        
class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0): #The "Cars" class will inherit all the attributes of the "Vehicle" class.
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
    def Drive(self):  #Calling this method means the car will be driven.
        is_driving = True
    def Stop(self,mileage):   #calling this method means you drove the car and you came to a stop.
        self.mileage = mileage
        is_driving = False #This method increments the mileage everytime the car is driven
        self.TripsSinceMaintenance += int(self.mileage)
        if self.TripsSinceMaintenance > 100: #Once the TripMaintenance counter exceeds 100,
            self.NeedsMaintenance = True
    def __str__(self,):
        return (self.Make + " " +  self.Model + " " + str(self.Year) + " Model," + " it weighs " + str(self.Weight) + " lbs, ")
    
    
#CREATING THE "PLANE" CLASS

class planes(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0): #The "planes" class will inherit all the attributes of the "Vehicle" class.
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
    def Fly(self):  #Calling this method means the plane will be flown.
        is_driving = True
    def Land(self,mileage):   #calling this method means you flew the plane and you landed.
        
    


#CREATING THREE DIFFERENT CARS    

car_1 = Cars("Toyota","Corolla",2015,2000)
car_2 = Cars("Honda","Accord",2018,1950)
car_3 = Cars("Ford","Escape",2018,2500)

#Driving car_1 three times @40miles each
car_1.Drive() 
car_1.Stop(40) #Car_1_Trip_1
car_1.Drive() 
car_1.Stop(40) #Car_1_Trip_2
car_1.Drive() 
car_1.Stop(40) #Car_1_Trip_3

#Driving car_2 four times @15miles each
car_2.Drive() 
car_2.Stop(15) #Car_2_Trip_1
car_2.Drive() 
car_2.Stop(15) #Car_2_Trip_2
car_2.Drive() 
car_2.Stop(15) #Car_2_Trip_3
car_2.Drive() 
car_2.Stop(15) #Car_2_Trip_4

#Driving car_1 three times @35miles each
car_3.Drive() 
car_3.Stop(35) #Car_3_Trip_1
car_3.Drive() 
car_3.Stop(35) #Car_3_Trip_2
car_3.Drive() 
car_3.Stop(35) #Car_3_Trip_3

car_1_trip = car_1.trip_since_maintenance() 
car_2_trip = car_2.trip_since_maintenance() 
car_3_trip = car_3.trip_since_maintenance()    


print("---------------------CAR1 INFORMATION---------------------\n")
print("Car_1 is a " + str(car_1) + "\nit's been driven " + str(car_1_trip) + " miles")
car_1_status = car_1.get_need_maintenance() 
print("\n---------------------CAR2 INFORMATION---------------------\n")
print("Car_2 is a " + str(car_1) + "\nit's been driven " + str(car_2_trip) + " miles")
car_2_status = car_2.get_need_maintenance()
print("\n---------------------CAR3 INFORMATION---------------------\n")
print("Car_3 is a " + str(car_3) + "\nit's been driven " + str(car_3_trip) + " miles")
car_3_status = car_3.get_need_maintenance()

   







    
    
        
    
        