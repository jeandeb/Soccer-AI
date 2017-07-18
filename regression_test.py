import tools
import tools_gen
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import math
import resource
import gc

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain

import numpy as np
import logging

#logger = logging.getLogger("simuExpe")

class Experience(object):

    MAX_STEP = 60

    def __init__( self, stratad, strateq, nb_essai, nb_rand, nb_etat, action, max_step=None ):
        #nbessai par action (tir,...)
        #nb_rand d'actions aleatoires differentes par situation
        #nb_etat de situation differentes

        self.stratad = stratad
        self.strateq = strateq
        self.nb_essai = nb_essai
        self.nb_rand = nb_rand
        self.nb_etat = nb_etat + 1
        self.action = action

        self.simu = tools_gen.init_game( self.strateq, self.stratad )
        self.simu.listeners += self

        #[Vitesse(a,n), Passe(a,n), [proba,score]]

        if( max_step) :
            MAX_STEP = max_step

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else :
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):

        self.nb_action = -1
        self.cpt = 0
        self.pos = tools_gen.generator( self.action, self.strateq, self.stratad, self.simu )

    def begin_round( self,team1,team2, state ):

        #gc.collect()
        self.nb_action += 1
        self.last = self.simu.step

        if( self.nb_action%(self.nb_essai*self.nb_rand*2) == 0 ) : 

            #reinitilisation des donees de recherche
            if( self.nb_action > 1 ):
                self.cpt += 1

            self.pos = tools_gen.generator( self.action, self.strateq, self.stratad, self.simu )

        if( self.cpt >= self.nb_etat - 1 ) : 
            self.simu.end_match()
            return  

        if not ( self.nb_action%( self.nb_essai*2 ) == 0 and self.nb_action > 1) : 
            tools_gen.positionne( self.pos, self.simu )

    
    def update_round( self, team1, team2, state ):

        #gc.collect()
        boole = tools_gen.valide( state, self.action )
        if ( state.step > self.last + self.MAX_STEP ) or boole :
            self.simu.end_round()   

    def end_round( self,team1,team2, state ):

        if ( self.cpt > self.nb_etat - 1 ): 
            self.simu.end_match()  
            return

        boole = tools_gen.valide( state, self.action )

