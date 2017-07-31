
#LANCER DEPUIS LE REPERTOIRE PARENT
import tools_gen
from Projet_2I013 import tools 
import tools_monte

import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
import resource
import numpy as np
import logging

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain

#logger = logging.getLogger("simuExpe")

class Experience(object):

    MAX_STEP = 500

    #INITIALISATIO
    def __init__( self, stratad, strateq, nb_explo, nb_div, max_step=None ):

    	self.nb_explo = nb_explo
    	self.nb_div = nb_div
    	self.returns = np.zeros(( nb_div, nb_div, nb_div, 2, 2, 5, 2 ))
    	self.q_tab = np.zeros(( nb_div, nb_div, nb_div, 2, 2, 5 ))

    	#Etat discret : Position dans le tableau q_tab
    	self.state = [0, 0, 0, 0, 0]
    	self.new_state = [0, 0, 0, 0, 0]
    	#[balle, j1, j2, balle=j1?, sens_balle]

    	self.strateq = strateq
    	self.strat = 0
    	self.new_strat = 0
    	self.simu = tools_gen.init_game( self.strateq, stratad )
    	self.simu.listeners += self

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else :
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):

        self.cpt = 0
        self.pos = tools_monte.generator( self.state, self.simu )
        self.state = tools_monte.set_state( self.simu )
 

    def begin_round( self,team1,team2, state ):

        self.cpt += 1
        #print self.cpt
        self.last = self.simu.step
        self.pos = tools_monte.generator( self.state, self.simu )
        self.state = tools_monte.set_state( self.simu )
        self.strat = tools_monte.best_strat( self.q_tab, self.state )
        tools_monte.set_strat( self.new_strat, self.strateq, state )
        

    def update_round( self, team1, team2, state ):

        self.new_state = tools_monte.set_state( self.simu )

        if (self.state != self.new_state) :

            self.new_strat = tools_monte.best_strat( self.q_tab, self.new_state )
            tools_monte.set_returns( self.state, self.new_state, self.returns, self.q_tab, self.strat, self.new_strat )
            tools_monte.set_strat( self.new_strat, self.strateq, state )
            #tools_monte.set_q( self.q_tab, self.returns, self.strat )

            self.state = self.new_state

            self.strat = self.new_strat

        if ( state.step > self.last + self.MAX_STEP ) :
            self.simu.end_round()   

    def end_round( self,team1,team2, state ):

        if ( self.cpt > self.nb_explo - 1 ): 
            self.simu.end_match()  
            return









