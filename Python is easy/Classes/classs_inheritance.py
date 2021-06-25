class Team:
    def __init__(self,Name = "Name",Origin = "Origin"):
        self.team_name = Name  #We have created a variable "Team_name" which is now part of the class.   
        self.team_origin = Origin 
        
    def define_team_name(self, Name):
        self.team_name = Name
        
    def define_team_origin(self, Origin):
        self.team_origin = Origin
        
#class inheritance
#class Inheritance_name(parent_class)

class Players(Team): #Every team has plsyers and the class Players will be a part of the bigger team class
    def __init__(self,player_name,player_point,team_name,team_origin):
        Team.__init__(self,team_name,team_origin) #You also have to initialise the parent class
        self.player_name = player_name
        self.player_point = player_point #Assuming that every player start with 0 points
                             #These attributes belong to the player class
                             
    #lets make a method for the players class
    def scored_point(self):
        self.player_point +=1
    def set_name(self,Name):
        self.player_name = Name
    def __str__(self): #__str__ allows us to call players directly without specifying a method
        return self.player_name + " has scored "  + str(self.player_point) + " points"
    
Player_1 = Players("drogba",0,"chealsea","London")
print(Player_1.player_name)
print(Player_1.player_point)
Player_1.define_team_name("BCC_Lion")
print(Player_1.team_name)
print(Player_1.team_origin) #The Player class inherited all the attribute of the team
Player_1.scored_point()
print(Player_1.player_point)
Player_1.set_name("makalele")
print(Player_1.player_name)
print(Player_1)