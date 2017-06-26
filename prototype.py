import tools
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
#from Projet_2I013 import basic_strategy

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
NB_ESSAI = 3

import numpy as np
import logging

logger = logging.getLogger("simuExpe")

class Experience(object):

    MAX_STEP = 40

    def __init__( self, nb_gener, strat ):
    	
     	self.data = np.zeros(( nb_gener, 4 ))
     	self.strat = strat
     	self.simu = tools.init_game( self.strat )
     	self.simu.listeners += self
     	self.nb_gener = nb_gener

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else:
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):
     
        self.last = 0
        self.step_tir = 0.0

    def begin_round( self,team1,team2, state ):

       tools.generator( len( self.strat ), self.simu )
       self.last = self.simu.step

    def update_round( self,team1,team2, state ):

        if ( state.step > self.last + self.MAX_STEP ):
            self.simu.end_round()

    def end_round( self,team1,team2, state ):
        

        if self.step_tir < NB_ESSAI :
                self.step_tir += 1.
                return
        self.step_tir = 0.0

		if ( self.cpt > self.nb_gener ): 
			self.simu.end_match()


