class Vehicle:
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.Make = Make
        self.Model = Model
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        
    def set_make(self,xmake):
        self.Make = xmake
    def set_model(self,xmodel):
        self.Model = xmodel
    def set_year(self,xyear):
        self.Year = xyear
    def set_weight(self,xweight):
        self.Weight = xweight   
        
        
class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
    def Drive(self):
        is_driving = True
    def Stop(self):
        is_driving = False
        
    
        