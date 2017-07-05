import tools
import tools_gen
import data
from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import math

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain

import numpy as np
import logging

logger = logging.getLogger("simuExpe")

class Experience(object):


    def __init__( self, stratad, strateq, nb_essai, nb_rand, nb_etat, action ):
        #nbessai par action (tir,...)
        #nb_rand d'actions aleatoires differentes par situation
        #nb_etat de situation differentes

        self.stratad = stratad
        self.strateq = strateq
        self.nb_essai = nb_essai
        self.nb_rand = nb_rand
        self.nb_etat = nb_etat
        self.action = action

        self.simu = tools_gen.init_game( self.strateq, self.stratad )

        self.data_dicho = data.data_rand( self.nb_rand, self.nb_essai )

        self.data_alea = np.zeros(( self.nb_etat,  7, 2 ))
        self.pos_alea = 0
        #(Vitadouballe, Vecadjoueur, Posjoueur, Vitjoueur, Vit, Tir, Proba)

        self.dicho = [[0., 0.], [0., 0.], [0., 0.]]
        #[Vitesse(a,n), Passe(a,n), [proba,score]]

        self.simu.listeners += self
 

    def start( self, visu = True ):

        if visu :
            show_simu( self.simu )
        else :
            self.simu.start()
      
    def begin_match( self,team1,team2, state ):

        self.nb_action = -1
        self.cpt = 0
        #tools_gen.generator( self.data_alea, self.action, self.strateq, self.stratad )

    def begin_round( self,team1,team2, state ):

        self.nb_action += 1
        self.last = self.simu.step

        if( self.cpt >= self.nb_etat ) : 
            self.simu.end_match()
            return  

        if( self.nb_action%(self.nb_essai*self.nb_rand) == 0 and self.nb_essai > 1 ) :
            a =0


    def update_round( self, team1, team2, state ):
        a = 0     


    def end_round( self,team1,team2, state ):
        a = 0     


    def gener_entree():
        return

    def gener_sortie():
        return










