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
    
        
Pet_1 = Pet("Mikky",3,False,True)
print(Pet_1.get_name())
print(Pet_1.get_playful())
Pet_1.set_name("Brown")
print(Pet_1.get_name())