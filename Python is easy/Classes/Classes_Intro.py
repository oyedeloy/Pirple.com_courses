#class Classname:
    #def __init__(self):    #We are creating a function inside of a class
                           #This function will initialize all the class attributes
                           #The self keyword means the class will always refer to itself
        
        #self.attribute = 0
    #def another_function(self): #we can create another function
        #Action(s)
        
class Team:
    def __init__(self,Name = "Name",Origin = "Origin"):
        self.team_name = Name  #We have created a variable "Team_name" which is now part of the class.   
        self.team_origin = Origin 
        
    def define_team_name(self, Name):
        self.team_name = Name
        
    def define_team_origin(self, Origin):
        self.team_origin = Origin
        
#Below, we have created Two instances of the clas "Team" 
#The both have Team_name and Team_origin attribute
#They also have the define_team_name and the define_team_origin methods         

Team_1 = Team("Tigers", "Chicago")

Team_2 = Team("hawks", "New York")  

Team_3 = Team()   #If name or origin is not provided, it defaults to the name and origin provided in the __init__ definition
    
    

print(Team_1.team_name) 
Team_1.define_team_name("Dolphins") #This changes the teamname
print(Team_1.team_name)
print(Team_1.team_origin) 
Team_1.define_team_origin("Chicago")
print(Team_1.team_origin)    
print(Team_2.team_name)
print(Team_2.team_origin)
Team_2.define_team_name("Eagles")
print(Team_2.team_name)
print(Team_3.team_name)
print(Team_3.team_origin)

        

