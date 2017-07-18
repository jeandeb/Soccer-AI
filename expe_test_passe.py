import regression_test
import tools_gen
import pickle
import sys
import numpy as np
import math
from Projet_2I013 import strategy, tools
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90
NB_ESSAI = 2
NB_RAND = 1
NB_ETAT = 10
MAX_STEP = 120
X = GAME_HEIGHT/2
Y = 110

passe_tab = pickle.load( open( "Regression_model/surexepe_passe200.p", "rb" ))

class PasseTestStrategy(Strategy):

    def __init__(self):
        super(PasseTestStrategy,self).__init__("Test")

    def compute_strategy(self,state,id_team,id_player):

    	prop =  tools.properties(state,id_team,id_player )
        basic_action = tools.basic_action(prop )

        
        vit_ad = state.states[(1,1)].vitesse
        vec = (state.states[(1,1)].position+vit_ad) - prop.my_position
        tab = [[vec.norm, vec.angle]]
        #print tab 
        valeurs = passe_tab.predict( tab )
        print valeurs
        print vit_ad.norm

        return SoccerAction( Vector2D( angle=valeurs[0][0], norm=valeurs[0][1]), Vector2D(angle=vec.angle+math.pi, norm=valeurs[0][3]) )
        

static = tools_gen.StaticStrategy()
strat = tools_gen.LearningStrat()
test = PasseTestStrategy()

action = [ 'Passe', [False,True], [False,True] ]
#[nom,Entrees:Balle,Joueur2,Sortie:[Vj,Tj]]


strateq = [test, strat]
stratad = [static]


if( (len(sys.argv) > 1) ) :
	NB_ETAT = int(sys.argv[1])


expe = regression_test.Experience( stratad, strateq, NB_ESSAI, NB_RAND, NB_ETAT, action )



expe.start( True )

print expe.data_alea

if( (len(sys.argv) > 3) and (sys.argv[3] == "yes") or (len(sys.argv) > 2) and (sys.argv[2] == "yes")) :
	pickle.dump( expe.data_alea, open( "pickle_files/surexepe_passe" + str(NB_ETAT)+ ".p", "wb" ) )




