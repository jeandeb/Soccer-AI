import random_search
import tools
import pickle
import sys
import numpy as np
from Projet_2I013 import strategy

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 
NB_GENER = 10
X = GAME_HEIGHT/2
Y = 110

strat1 = tools.PasseLearningStrat()
goal = strategy.GoalStrategy()

expe = random_search.Experience( Y, X, [ strat1 ], goal=None )

expe.start( False )

print expe.data.state
print expe.dicho

if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( expe.data.state, open( "pickle_files/experand.p", "wb" ) )