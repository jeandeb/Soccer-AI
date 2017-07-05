import data
import random
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math

NB_GENER = 100
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10

class LearningStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "simple action"
        self.passe = Vector2D()
        self.vitesse = Vector2D()
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(self.vitesse,self.passe)

class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()



def init_game( strateq, stratad) : 

	cpt = 0
	team1 = SoccerTeam( "IA" )

	for i in strateq : 
		cpt += 1
		team1.add( "J" + str(cpt), i )

	cpt = 0

	team2 = SoccerTeam( "AD" )

	for i in stratad : 

		cpt += 1
		team2.add( "A" + str(cpt), i )

	simu = Simulation( team1, team2, max_steps=100000000 )

	return simu

#def generator()




