import tools
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import math

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
NB_ESSAI = 20
NB_DICHO = 80

import numpy as np
import logging

logger = logging.getLogger("simuExpe")


class Experience(object):

    MAX_STEP = 30

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

        self.data = data.data_dicho( NB_ESSAI, NB_DICHO )
        self.nb_dicho = NB_DICHO
        self.strat = strat
        self.simu.listeners += self
        self.dicho = [[3*math.pi/2,0.0,0.0],[math.pi/2,8.0,0.0]]


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
        self.strat[0].passe = tools.shoot_rand( self.dicho )

    def begin_round( self,team1,team2, state ):

        position = Vector2D( self.x, self.y )   
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D() 
        self.simu.state.ball.position = position.copy()

        if self.goal : 

            self.simu.state.states[(2,0)].position = Vector2D( 140, 45 )

        self.nb_tirs += 1
        self.last = self.simu.step

        #print "cpt =" + str(self.cpt)
        if( self.cpt >= self.nb_dicho ) : 
            self.simu.end_match()
            return

        #print self.nb_tirs

        if( self.nb_tirs%(NB_ESSAI*NB_ESSAI*2) == 0 and self.nb_tirs != 0 ) :
                #print "dicho"
                #print self.dicho
                #print self.data.state
                tools.best_two( self.data.state, self.dicho )
                self.cpt += 1
                

        if( self.nb_tirs%(NB_ESSAI*2)-1 == 0 ):
            #print "set essai"
            self.strat[0].passe = tools.shoot_rand( self.dicho )
            self.data.set_essai( self.strat[0].passe, self.nb_tirs )


    def update_round( self, team1, team2, state ):

        boole = tools.valide_tir( state )
        if( state.step > self.last + self.MAX_STEP ) or boole:
            self.simu.end_round()

    def end_round( self,team1,team2, state ):

        
        if( self.cpt >= self.nb_dicho ) : 
            self.simu.end_match()

        boole = tools.valide_tir( state )
        self.data.calcul_proba( boole, self.nb_tirs  )











