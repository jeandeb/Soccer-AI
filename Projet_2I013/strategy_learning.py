# -*- coding: utf-8 -*-<
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D




GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 # Acceleration maximale de la balle



class ShootingLearningStrat( Strategy ) : 
    def __init__(self,shoot=None):
        self.name = "simple action"
        self.norm = 2.0
    def compute_strategy(self,state,id_team,id_player):
        shoot = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.player_state(id_team,id_player).position
        shoot = shoot.normalize()*self.norm
        return SoccerAction(Vector2D(),shoot)





class StaticStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "shooting_learning" )

    def compute_strategy( self, state, id_team, id_player ):

        return SoccerAction( Vector2D(), Vector2D() )