# exercice pour calculer la moyenne de combien de fois le robot doit ce dépelacer pour atteindre les bords d'un plateau d'echecs

import random 
import numpy as np # type: ignore
class Robot:
    def __init__(self, ):   #plateau):
        self.posx = 0
        self.posy = 0
        #self.plateau=plateau    # je fais ça quand je veux utiliser les attributs de la classe plateu das robot
    
    def droite (self):
        self.posx +=1
    
    def gauche (self):
        self.posx -=1
    
    def haut (self):
        self.posy +=1
    
    def bas (self):
        self.posy -=1

    def reinitialiser_pos(self):
        self.posx = 0
        self.posy = 0

class Plateau:
    def __init__(self,M,N):   # N=longeur , M=Largeur
        self.M = M
        self.N = N


M=5
N=5
Plat=Plateau(M,N)
Bot=Robot()

move_tab=[]
#while True:
for i in range (10000):
    move=0
    while ((Bot.posx <= Plat.M) and (Bot.posy <= Plat.N)):
        rand_val= random.randint(1,4)
        if ( rand_val== 1):
            Bot.droite()
            move+=1
            
        elif (rand_val == 2) and (Bot.posx > 0):
            Bot.gauche()
            move+=1

        elif (rand_val == 3):
            Bot.haut()
            move+=1
        elif (rand_val == 4) and (Bot.posy > 0):
            Bot.bas()
            move+=1
    move_tab.append (move)
    Bot.reinitialiser_pos()
moyenne = np.mean(move_tab)
print ( "moyenne = ", int(moyenne) )  
#print (move_tab)  
#  break 

 


        





















