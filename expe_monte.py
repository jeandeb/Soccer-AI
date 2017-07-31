import montecarlo_simulation
import tools_monte
import pickle
import sys
import numpy as np
from Projet_2I013 import strategy


GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90
NB_DIV = 25
NB_EXPLO = 20000
X = GAME_HEIGHT/2
Y = 110

strat = tools_monte.MonteStrat()
static = strategy.FonceurStrategy()

#[nom,Entrees:Balle,Joueur2,Sortie:[Vj,Tj]]


strateq = [strat]
stratad = [static]



expe = montecarlo_simulation.Experience( stratad, strateq, NB_EXPLO, NB_DIV )

if( (len(sys.argv) > 1) and (sys.argv[1] == "show") ) :
	show = True
else : 
	show = False


expe.start( show )

if( (len(sys.argv) > 2) and (sys.argv[2] == "yes") or (len(sys.argv) > 1) and (sys.argv[1] == "yes")) :
	pickle.dump( expe.q_tab, open( "pickle_files/surexepe_monte" + str(NB_EXPLO)+ ".p", "wb" ) )