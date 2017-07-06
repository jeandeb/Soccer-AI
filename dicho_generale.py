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
        if( max_step) :
            MAX_STEP = max_step

        self.simu = tools_gen.init_game( self.strateq, self.stratad )

        self.data_gen = data.data_gen( self.nb_rand, self.nb_essai )

        self.data_alea = np.zeros(( self.nb_etat - 1,  7, 2 ))
        self.pos_alea = 0
        #(Vitadouballe, Vecadjoueur, Posjoueur, Vitjoueur, Vit, Tir, Proba)

        self.dicho = [[0., 0.], [0., 0.], [0.,float('inf')]]
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
        self.pos = tools_gen.generator( self.action, self.strateq, self.stratad, self.simu )
        tools_gen.generator_action( self.dicho, self.action, self.strateq[0] )
        self.data_gen.set_essai( self.strateq[0].vitesse, self.strateq[0].passe, 0 )

    def begin_round( self,team1,team2, state ):

        self.nb_action += 1
        self.last = self.simu.step

        if( self.nb_action%(self.nb_essai*self.nb_rand*2) == 0 ) : 

            #reinitilisation des donees de recherche
            if( self.nb_action > 1 ):
                #print "cpt = " + str(self.cpt)
                #print "dicho = " + str(self.dicho)
                tools_gen.set_data_alea( self.data_alea, self.dicho, self.action, self.pos, (self.cpt) )
                #print "data alea = " + str( self.data_alea)
                self.nb_action = -1
                self.data_gen.to_zero()
                self.dicho = [[0., 0.], [0., 0.], [0.,float('inf')]]
                self.cpt += 1

            self.pos = tools_gen.generator( self.action, self.strateq, self.stratad, self.simu )


        if( self.cpt >= self.nb_etat - 1 ) : 
            self.simu.end_match()
            return  

        if( self.nb_action%( self.nb_essai*2 ) == 0 and self.nb_action > 1) : 

            #print "dicho = " + str(self.dicho)
            #print "position = " + str( self.nb_action//(self.nb_rand*2)-1 )
            #print "courant = " + str(self.data_gen.state[self.nb_action//(self.nb_essai*2)-1])
            #print "tab_gen = " + str(self.data_gen.state)


            tools_gen.best_elem( self.data_gen.state[self.nb_action//(self.nb_essai*2)-1], self.dicho )
            tools_gen.generator_action( self.dicho, self.action, self.strateq[0] )
            self.data_gen.set_essai( self.strateq[0].vitesse, self.strateq[0].passe, self.nb_action )
    


        else : 
            tools_gen.positionne( self.pos, self.simu )

        #if( self.nb_action%(self.))

    def update_round( self, team1, team2, state ):

        boole = tools_gen.valide( state, self.action )

        if ( state.step > self.last + self.MAX_STEP ) or boole :
            self.simu.end_round()   


    def end_round( self,team1,team2, state ):

        if ( self.cpt > self.nb_etat - 1 ): 
            self.simu.end_match()  

        boole = tools_gen.valide( state, self.action )
        score = tools_gen.score( state, self.action )

        self.data_gen.set_score( score, self.nb_action )

        self.data_gen.calcul_proba( boole, self.nb_action  )











