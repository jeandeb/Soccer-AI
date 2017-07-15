import dicho_generale
import tools_gen
import pickle
import sys
import numpy as np
from Projet_2I013 import strategy


GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90
NB_ESSAI = 10
NB_RAND = 100
NB_ETAT = 50
X = GAME_HEIGHT/2
Y = 110

strat = tools_gen.LearningStrat()
static = tools_gen.StaticStrategy()
action = [ 'Tir', [False,False], [False,True] ]
#[nom,Entrees:Balle,Joueur2,Sortie:[Vj,Tj]]


strateq = [strat]
stratad = [static]



expe = dicho_generale.Experience( stratad, strateq, NB_ESSAI, NB_RAND, NB_ETAT, action )

if( (len(sys.argv) > 1) and (sys.argv[1] == "show") ) :
	show = True
else : 
	show = False


expe.start( show )

print expe.data_alea

if( (len(sys.argv) > 2) and (sys.argv[2] == "yes") or (len(sys.argv) > 1) and (sys.argv[1] == "yes")) :
	pickle.dump( expe.data_alea, open( "pickle_files/surexepe_tir500.p", "wb" ) )