import tools
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import math

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
NB_ESSAI = 3 
NB_DICHO = 3

import numpy as np
import logging

logger = logging.getLogger("simuExpe")

class Experience(object):

    MAX_STEP = 40

    def __init__( self, x, y, strat ):
    	self.x = x
        self.y = y
        self.strat = strat
        self.simu = tools.init_game( self.strat )
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

    def begin_round( self,team1,team2, state ):

        if self.nb_essai >= 2*NB_ESSAI-1 : 
            self.nb_essai = -1

        self.nb_tirs += 1
        self.nb_essai += 1
        self.last = self.simu.step
        #print 1

        position = Vector2D( self.x, self.y )   
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D() 
        self.simu.state.ball.position = position.copy()


        if self.cpt >= NB_DICHO-1 : 
            self.cpt = 0

        if( self.nb_essai < 0 ): 
            print "set essai"
            self.strat[0].passe = tools.shoot_rand( self.dicho )
            #print self.strat[0].passe
            self.data.set_essai( self.strat[0].passe, self.nb_tirs )

            self.cpt += 1
            if( self.cpt < 1 ):
          
                self.dicho = tools.best_two( self.data.state, self.dicho )
                #print self.dicho
        print self.nb_essai

    def 

    def update_round( self, team1, team2, state ):

        boole = tools.valide_tir( state )
        self.data.calcul_proba( boole, self.nb_essai, self.nb_tirs  )
        if( state.step > self.last + self.MAX_STEP ) or boole:
            self.simu.end_round()

    def end_round( self,team1,team2, state ):
 
		if ( self.cpt > self.nb_dicho ): 
			self.simu.end_match()









