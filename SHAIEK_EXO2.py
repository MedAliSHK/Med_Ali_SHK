import random 
import numpy as np # type: ignore
from time import sleep

class Robot():
    name = "<unnamed>"
    power = False
    current_speed = 0
    battery_level = 0
    states = ['shutown', 'running']
    
    def __init__(self, name="<undefined>",battery_level=80):
        self.name=name
        self.battery_level=battery_level
        

    def turn_on_robot(self):
        self.power=True

    def turn_off_robot(self):
        self.power=False

    def charger_robot (self):
        if self.power==True:
            print("charge du robot allume")
        else:
            print("charge du robot eteint")
        while self.battery_level < 100:
            if self.battery_level >90:
                sleep((100-self.battery_level)/10)
                self.battery_level =100
                print("La batterie du robot est a : ",self.battery_level, "%")
            else:
                sleep(1)
                self.battery_level +=10
                print("La batterie du robot est a : ",self.battery_level, "%")

    def get_speed(self):
        return self.current_speed

    def set_speed (self,speed):
        if(speed <0):
            print("la vitesse ne peut pas etre negative")
            speed=0
        self.current_speed+=speed

    def stop_robot(self):
        self.current_speed=0    

    

 
class Human():   
    def __init__(self, sexe="undefined",aliments_manges=[]):
        self.sexe=sexe
        self.aliments_manges=aliments_manges

    def eat (self,food):
        print ("eatiiiiing")
        if isinstance(food, str):
            self.aliments_manges.append(food)
        
        elif isinstance(food,list):
            for i in food:
                self.aliments_manges.append(i)

        else:
            print("l'aliments a manger ne peut pas etre un entier")
            
    def digest (self):
        print("digestion en cours")
        self.aliments_manges.pop(0)
        
    
 
class Cyborg(Robot, Human):   
 
    def __init__(self, name, sexe):   
        # initiate Robot parent class
        Robot.__init__(self, name)
        # initiate Human parent class
        Human.__init__(self, sexe)

    def __etat__(self):
        print ("Robot : ",self.name, "||","Sexe : ",self.sexe, "||","battery_level : ",self.battery_level, "||","aliments manges: ",self.aliments_manges)
    
    def fun (self):
        print("fuuuun")
        self.name="CR7"
        self.battery_level=9999
        self.eat(["5*UCL","5*ballon_d_or","Liga","golden_boot","etc..."])

 
cyborg = Cyborg('Deux Ex Machina', 'M')
 
print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charger_robot()
cyborg.__etat__()
cyborg.eat('banana')
cyborg.__etat__()
cyborg.eat(['coca', 'chips'])
cyborg.__etat__()
cyborg.digest()
cyborg.__etat__()
cyborg.fun()
cyborg.__etat__()
