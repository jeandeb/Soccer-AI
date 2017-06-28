import tools
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
NB_ESSAI = 3 

import numpy as np
import logging

logger = logging.getLogger("simuExpe")

class Experience(object):

    MAX_STEP = 40

    def __init__( self, nb_gener, strat ):
    	
     	self.data = data.data( nb_gener, NB_ESSAI, 3 )
     	self.strat = strat
     	self.simu = tools.init_game( self.strat )
     	self.simu.listeners += self
     	self.nb_gener = nb_gener
     	self.position = Vector2D()

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else :
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):
     
        self.last = 0
        self.step_action = -1
        self.cpt = 0
        self.pos = tools.generator( len( self.strat ), self.simu )
        self.strat[0].passe = tools.shoot_vect_rand( self.pos )

    def begin_round( self,team1,team2, state ):

    	self.step_action += 1
    	self.last = self.simu.step

    	if( self.step_action%(NB_ESSAI*2) == 0 ):
    		self.strat[0].passe = tools.shoot_vect_rand( self.pos )
    		self.data.set_essai( self.strat[0].passe, self.step_action )

    		if( self.step_action%(NB_ESSAI*NB_ESSAI*2) == 0 ) :
    			self.pos = tools.generator( len( self.strat ), self.simu )
    			self.cpt+= 1
    			#print self.cpt

    	else :
    		tools.positionne( self.pos, self.simu ) 


    def update_round( self, team1, team2, state ):

		direction = tools.dir( self.pos )
		norm = direction.norm
		angle = direction.angle    	
		boole = tools.valide( state, self.pos )
		self.data.calcul_proba( boole, norm, angle, self.step_action )

		if ( state.step > self.last + self.MAX_STEP ) or boole:
			self.simu.end_round()

    def end_round( self,team1,team2, state ):
        
		if ( self.cpt > self.nb_gener ): 
			self.simu.end_match()






