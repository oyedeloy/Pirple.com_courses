class Pet:
    def __init__(self,n,a,h,p):
        self.name = n  #This makes name an attribute of Pet.
        self.age = a
        self.hunger = h
        self.playful = p
    #getters: Everything below will be a get function
    #A get function gives you the value back
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_hunger(self):
        return self.hunger
    def get_playful(self):
        return self.playful
    
    
    #Setters
    def set_name(self,xname):
        self.name = xname
    def set_age(self,xage):
        self.age = age
    def set_hunger(self,xhunger):
        self.hunger = xhunger
    def set_playful(self,xplayful):
        self.playful = xplayful
    
        
class Cat(Pet): 
    def __init__(self,name,age,hunger,playful,place): #The Dog class will inherit attributes and methods from the Pet class
        Pet.__init__(self,name,age,hunger,playful)
        self.fav_to_sit = place
        
        
    def wants_to_play(self):
        if self.playful == True:
            return("Dog wants to play with " + self.fav_toy)
    def wants_to_sit(self):
        if self.playful == False:
            return("Cat wants to sit in " + self.fav_to_sit)
        else:
            return "Cat wants to paly"
    def __str__(self):
        return (self.name + " likes to sit in " + self.fav_to_sit)
            
        



class Dog(Pet): 
    def __init__(self,name,age,hunger,playful,breed,fav_toy): #The Dog class will inherit attributes and methods from the Pet class
        Pet.__init__(self,name,age,hunger,playful)
        self.breed = breed
        self.fav_toy = fav_toy
        
    def wants_to_play(self):
        if self.playful == True:
            return("Dog wants to play with " + self.fav_toy)
        else:
            return "Dog doesn't want to play"
        
Mikky_dog = Dog("Mikky",5,False,True,"Alsatian","Stick")
play = Mikky_dog.wants_to_play()
print(play)

ordinary_cat = Cat("Pussy",3,False,False,"the lobby")
sit = ordinary_cat.wants_to_sit()
print(sit)
print(ordinary_cat)

        
