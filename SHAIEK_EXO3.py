	
from abc import ABCMeta, abstractmethod
 
""" You can use classes below or create your own 👍️"""
 
class UnmannedVehicule(metaclass=ABCMeta):
    def __init__(self, name):
        self.name=name
    @abstractmethod    
    def mission(self):
        print("Mission en cours__UnmannedVehicule")
    

 
class AerialVehicule(metaclass=ABCMeta):
    """ A vehicle made for aerial areas."""
    def __init__(self):
        self.typeField="Arial"

class GroundVehicule(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    def __init__(self):
        self.typeField="Ground"

class UnderseaVehicule(metaclass=ABCMeta):
    """ A vehicle made for underwater sea."""
    def __init__(self):
        self.typeField="UnderSea" 

class UAV(UnmannedVehicule,AerialVehicule):
    """Unmanned Aerial Vehicule"""
    def __init__(self, name):
        super().__init__(name)
        AerialVehicule.__init__(self)

    def mission(self):
        print("Mission en cours__UAV")
    def use(self):
        print("Utilisation__UAV")
    
    def __str__(self):
        return f"Ce véhicule est : {self.name} et c'est un véhicule : {self.typeField}"

class UUV(UnmannedVehicule,UnderseaVehicule):
    """Unmanned Undersea Vehicule"""
    def __init__(self, name):
        super().__init__(name)
        UnderseaVehicule.__init__(self)

    def mission(self):
        print("Mission en cours__UUV")
    def use(self):
        print("Utilisation__UUV")
    
    def __str__(self):
        return f"Ce véhicule est : {self.name} et c'est un véhicule : {self.typeField}"

class UGV(UnmannedVehicule,GroundVehicule):
    """Unmanned Ground Vehicule"""
    def __init__(self, name):
        UnmannedVehicule.__init__(self,name)
        GroundVehicule.__init__(self)

    def mission(self):
        print("Mission en cours__UGV")
    def use(self):
        print("Utilisation__UGV")
    def __str__(self):
        return f"Ce véhicule est : {self.name} et c'est un véhicule : {self.typeField}"



uuv_bot=UUV("uuv_vehicule")
print(uuv_bot)
uav_bot=UAV("uav_vehicule")
print(uav_bot)
ugv_bot=UGV("ugv_vehicule")
print(ugv_bot)
