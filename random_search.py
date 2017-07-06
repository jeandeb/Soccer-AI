import tools
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
import random

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
NB_ESSAI = 5
nb_rand = 50

import numpy as np
import logging

logger = logging.getLogger("simuExpe")


class Experience(object):

    MAX_STEP = 50

    def __init__( self, x, y, strat, goal=None ):
    	self.x = x
        self.y = y
        self.strat = strat 

        if( goal ) : 
            self.simu = tools.init_game( self.strat, goal )
            self.goal = goal
        else : 
            self.simu = tools.init_game( self.strat )
            self.goal = False

        self.data = data.data_rand( nb_rand, NB_ESSAI )
        self.nb_rand = nb_rand
        self.strat = strat
        self.simu.listeners += self
        self.dicho = [0.,0.,0.,float('inf')]

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else :
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):
        self.nb_tirs = -1
        self.nb_essai = -1
        self.cpt = 0

        position = Vector2D( self.x, self.y )   
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D() 
        self.simu.state.ball.position = position.copy()

        self.strat[0].passe = tools.shoot_rand_search( self.dicho )
        self.data.set_essai( self.strat[0].passe, 0 )

    def begin_round( self,team1,team2, state ):

        position = Vector2D( self.x, self.y )   
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D() 
        self.simu.state.ball.position = position.copy()

        if self.goal : 

            self.simu.state.states[(2,0)].position = Vector2D( 140, 45 )

        self.nb_tirs += 1
        self.last = self.simu.step

        if( self.cpt >= self.nb_rand ) : 
            self.simu.end_match()
            return

        if( self.nb_tirs%(NB_ESSAI*2) == 0 and self.nb_tirs > 1 ):

            tools.best_tab( self.data.state[self.nb_tirs//(NB_ESSAI*2)-1], self.dicho )
            self.strat[0].passe = tools.new_shoot( self.dicho )
            self.data.set_essai( self.strat[0].passe, self.nb_tirs )
            self.cpt += 1

                

    def update_round( self, team1, team2, state ):

        boole = tools.valide_tir( state )
        if( state.step > self.last + self.MAX_STEP ) or boole:
            self.simu.end_round()

    def end_round( self,team1,team2, state ):


        if( self.nb_tirs >= nb_rand*NB_ESSAI*2-1 ) : 
            self.simu.end_match()

        boole = tools.valide_tir( state )
        score = tools.score( state )

        self.data.set_score( score, self.nb_tirs )

        self.data.calcul_proba( boole, self.nb_tirs  )


