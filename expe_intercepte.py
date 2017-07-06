import dicho_generale
import tools_gen
import pickle
import sys
import numpy as np
from Projet_2I013 import strategy

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90
NB_ESSAI = 20
NB_RAND = 100
NB_ETAT = 100
X = GAME_HEIGHT/2
Y = 110

strat = tools_gen.LearningStrat()
static = tools_gen.StaticStrategy()
action = [ 'Intercepte', [True,False], [True,False] ]
#[nom,Entrees:Balle,Joueur2,Sortie:[Vj,Tj]]


strateq = [strat]
stratad = [static]



expe = dicho_generale.Experience( stratad, strateq, NB_ESSAI, NB_RAND, NB_ETAT, action )

if( (len(sys.argv) > 1) and (sys.argv[1] == "show") ) :
	show = True
elif (len(sys.argv) > 1) and (sys.argv[1] == "yes"): 
	pickle.dump( expe.data_alea, open( "pickle_files/surexepe_intercepte.p", "wb" ) )
	show = False
else : 
	show = False


expe.start( show )

print expe.data_alea

if( (len(sys.argv) > 2) and (sys.argv[2] == "yes") ) :
	pickle.dump( expe.data_alea, open( "pickle_files/surexepe_intercepte.p", "wb" ) )